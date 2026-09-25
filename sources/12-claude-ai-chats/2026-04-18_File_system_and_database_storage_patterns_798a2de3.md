# File system and database storage patterns

created: 2026-04-18T17:22:41.144305Z  uuid: 798a2de3-596c-4254-ac4f-b10cb311725e  export: new
messages: 32  total_chars: 89146  human_chars: 1351


---
**HUMAN** (2026-04-18T17:22):

Is directly using file system plus database to save files a good idea

---
**ASSISTANT** (2026-04-18T17:23):

  The user is asking about a filesystem plus database architecture for file storage, which makes sense given they're building infrastructure tools. I'm thinking through the tradeoffs of this pattern—storing actual file bytes on disk while keeping metadata like paths, hashes, ownership, and timestamps in the database. This is a solid, commonly-used approach, so let me consider when it actually works well and where the complications arise.

The filesystem-plus-database pattern shines when files are large, you need streaming access, want to leverage OS-level tools like rsync, or when read-heavy workloads benefit from filesystem caching. It's also much cheaper than storing everything in a database. But the real challenges are atomicity issues—writes to the filesystem and database aren't transactional, so you risk orphaned files or dangling pointers if one succeeds and the other fails. You also have to manage backup and replication complexity across two separate systems, enforce permissions consistently, handle multi-server scaling (local filesystems don't work here), and deal with deletion races where files linger on disk after being marked deleted in the database. Object storage like S3 or MinIO paired with database metadata often solves these problems more elegantly.

Given that Ren's working on something like FUSE-based versioning, they're clearly thinking about this at a deeper level. The pattern works fine for their use case, but the key is handling the atomicity problem upfront—write the file first, then update the database, and have a garbage collection process to clean up orphans. For smaller files or simpler scenarios, just storing BLOBs in the database might be worth reconsidering. Content-addressed storage with hashes as filenames is another solid approach if deduplication and immutability matter.Yes, it's a perfectly reasonable and very common pattern — files on disk, metadata (path, hash, owner, size, mime, timestamps) in the DB. Most production systems start here. The main reason it works: databases are bad at large blobs (bloats backups, kills cache efficiency, slow streaming), while filesystems are great at exactly that, and the DB is great at the indexed lookup and relational glue.

The thing that bites people is the lack of transactional atomicity between the two stores. If you write the row first and the file write fails, you have a dangling pointer. If you write the file first and the row insert fails, you have an orphan blob. The standard fix is write-file-then-row with content-addressed names (hash as filename, so writes are idempotent and dedup is free) plus a periodic GC sweep that deletes files with no referencing row after some grace period. Deletes should be soft in the DB first, then a separate worker reaps the physical file. Don't try to make it ACID — accept eventual consistency and design the reaper.

When to reach for something else: if you'll ever run more than one app server, local FS becomes the bottleneck — switch to object storage (S3/R2/MinIO) with the same metadata-in-DB pattern. If files are tiny (<10KB) and always read with their parent row, BLOB-in-DB can actually be simpler. And given your FUSE-versioning interests, worth noting that content-addressed FS layout (like git's objects/) gives you cheap snapshots and dedup essentially for free, which composes really well with a metadata DB pointing at content hashes rather than paths.

---
**HUMAN** (2026-04-18T17:25):

Can we modify a file system every time a file is dropped, in every sub folder, triggering a event that can be caught

---
**ASSISTANT** (2026-04-18T17:26):

 Yes — this is a solved problem on every major OS, and the API you want depends on the platform.

**Linux:** `inotify` is the kernel API; it watches a directory for create/modify/delete/move events. The catch: it doesn't recurse — you have to add a watch per subdirectory yourself, and re-add for any new subdir created. Libraries like `watchdog` (Python), `chokidar` (Node), `notify` (Rust) wrap this and handle the recursion bookkeeping for you. There's a per-user watch limit (`/proc/sys/fs/inotify/max_user_watches`, often 8192 or 65536) that you'll hit on large trees — bump it. The newer `fanotify` (kernel 5.1+) supports recursive mount-wide watching natively and is what you'd reach for at scale.

**macOS:** `FSEvents` is recursive by default and very efficient — it taps into a kernel-level log of filesystem changes per volume. Same wrapper libs above abstract this.

**Windows:** `ReadDirectoryChangesW` with the `bWatchSubtree` flag gives you recursive watching out of the box.

**FUSE (relevant to your OpenClaw versioning work):** if you control the filesystem itself, you don't need to watch — you *are* the event source. Every `write`, `create`, `rename`, `unlink` is a function call you implement. This is strictly better than inotify for your use case: no race conditions, no missed events during high churn, no watch limits, and you get the operation *before* it commits, so you can version, hash, or reject atomically. The tradeoff is FUSE has overhead (userspace round-trip per syscall) and only works on paths mounted through your filesystem.

**Things that bite people regardless of API:**
- Editors don't "modify" files — many (vim, VSCode) write to a temp file then rename over the original, so you'll see create+rename, not modify. Handle rename events.
- Events can coalesce or arrive out of order under load. Debounce.
- A "file dropped" (large copy) fires events while the file is still being written. Either wait for size to stabilize or watch for the `CLOSE_WRITE` event on Linux.
- Network filesystems (NFS, SMB) often don't propagate events at all. inotify only sees local changes.

For your stack: if this is for OpenClaw artifact tracking, FUSE is the right answer. If it's for watching a regular working directory, `chokidar` or `watchdog` will get you running in an afternoon.

---
**HUMAN** (2026-04-18T17:30):

How big is fuse overhead

---
**ASSISTANT** (2026-04-18T17:30):

 Short answer: per-syscall latency roughly **2–10× native** for metadata ops, throughput **20–50% lower** for bulk I/O on a well-tuned FUSE fs, and it can get much worse if your handlers are slow or you don't use the right mount options.

The cost comes from the architecture: every syscall on a FUSE mount is a context switch from kernel → FUSE driver → userspace daemon → back. Native ext4 stays in kernel. Concretely:

**Metadata ops (stat, open, readdir, getattr):** these are where FUSE hurts most. A `stat` on ext4 is ~1µs; on FUSE it's typically 10–50µs even with a no-op handler. If you're doing `find` over a million files, you'll feel it. The kernel caches attrs and dentries (controlled by `entry_timeout` and `attr_timeout` mount options), so repeated stats can be nearly free — but the first walk is slow.

**Sequential read/write:** much better than people expect. With `-o big_writes` (default in modern libfuse), `max_write=1MB+`, and `writeback_cache`, you can hit 70–90% of native throughput on large files. The 4KB-per-roundtrip default is what makes naive FUSE filesystems feel slow; bumping the block size closes most of the gap.

**Random small I/O:** painful. Each 4KB read is a roundtrip. SQLite on FUSE is noticeably slower than SQLite on ext4 for this reason.

**Real numbers from published benchmarks:** the Bento/EuroSys-era FUSE studies show ~5% overhead on sequential reads of large files with caching, jumping to 50%+ on metadata-heavy workloads like untarring the Linux kernel source or running `git status` on a big repo. Rust-based FUSE (fuser) and the newer io_uring FUSE backend (kernel 6.x) cut this further.

**For OpenClaw versioning specifically:** the overhead profile is actually favorable. You're capturing writes (where you'd be doing hash + store work anyway, dwarfing the FUSE roundtrip), not doing high-frequency random reads. The dominant cost will be your versioning logic — Merkle hashing, content-addressed storage writes — not FUSE itself. The thing to watch: if agents do lots of `stat`/`readdir` while exploring (Claude Code does this constantly), tune `attr_timeout=60` and `entry_timeout=60` aggressively, since agent-written files don't change out-of-band.

If you want to skip FUSE overhead entirely and you're on Linux 5.4+, **eBPF + fanotify** can intercept filesystem events at the kernel level with near-zero overhead, but you can only observe, not transform. For a versioning layer that needs to actually intercept writes, FUSE is still the pragmatic choice.

---
**HUMAN** (2026-04-18T17:31):

eBPF + fanotify explain

---
**ASSISTANT** (2026-04-18T17:31):

 These are two separate kernel mechanisms that get paired because they cover complementary gaps.

**fanotify** is the "grown-up" inotify. Same idea — get notified about filesystem events — but with three properties that matter:

1. **Recursive mount-wide watching** with `FAN_MARK_FILESYSTEM` (kernel 4.20+). One watch covers the entire mount, no per-directory bookkeeping, no watch-limit problem.
2. **Permission events** (`FAN_OPEN_PERM`, `FAN_ACCESS_PERM`): the kernel pauses the syscall and asks your userspace daemon "allow or deny?" before letting it proceed. This is how antivirus and DLP products work on Linux. You can actually *block* operations, not just observe them after the fact.
3. **Content events** post-5.1 include create/delete/move/modify (`FAN_CREATE`, `FAN_DELETE`, etc.), closing the historical gap where fanotify only saw open/access/close.

What fanotify *can't* do: transform data. You can allow or deny a write, but you can't rewrite the bytes the way FUSE can. And the permission-event model means your daemon is in the hot path — if it's slow, every open on the system stalls.

**eBPF** is unrelated mechanically — it's a way to load small, verified programs into the kernel that run on hooks (syscalls, tracepoints, kprobes, LSM hooks). For filesystem stuff the relevant hooks are `tracepoint/syscalls/sys_enter_openat`, the VFS layer kprobes, and (most powerfully) the **BPF LSM** hooks (kernel 5.7+), which let you write security policy that runs inline with operations like `file_open`, `inode_create`, `path_unlink`.

The "eBPF + fanotify" pairing usually means one of two architectures:

- **eBPF for cheap observation, fanotify for enforcement.** eBPF programs filter and aggregate events in-kernel — you can watch every open() on the system and only forward "interesting" ones (matching a path prefix, a UID, an extension) to userspace via a ring buffer. Then fanotify handles the few cases where you need to actually block. This avoids fanotify's hot-path cost for the 99% of events you only want to log.

- **BPF LSM as a fanotify replacement.** If you're on 5.7+ you can do permission decisions entirely in eBPF without a userspace round-trip. Much faster than fanotify permission events, but the policy has to be expressible in eBPF (no calling out to a Python daemon to think about it).

**For your OpenClaw versioning use case**, honestly, neither is a great fit. Both are observation/enforcement layers — they tell you what happened or block it, but neither lets you transform writes the way FUSE does. If an agent writes a file and you want to: hash it, dedupe it, store it content-addressed, update a Merkle DAG, *and* let the agent see a normal file on read — you need to be the filesystem. FUSE.

Where eBPF+fanotify *would* fit: a lightweight "agent activity audit log" sidecar that records every file an agent touches, with no transformation. Cheap, kernel-fast, no FUSE overhead, no risk of breaking the workspace if your daemon crashes. Worth considering as a separate layer alongside FUSE versioning rather than instead of it.

---
**HUMAN** (2026-04-18T17:33):

Are there platform independent ways to do it? Like in js or rust

---
**ASSISTANT** (2026-04-18T17:34):

  The user is asking about cross-platform filesystem watching in JavaScript or Rust, building on our earlier discussion about FUSE and kernel-level approaches. Since they're working on OpenClaw and understand the technical depth, I should give them concrete options without oversimplifying, keeping it concise for mobile.

For watching, `chokidar` abstracts the platform differences in Node.js, while Rust's `notify` crate does the same thing across Linux, macOS, and Windows. If they need FUSE-style filesystem interception, that's trickier — FUSE itself has ports like WinFsp and macFUSE, but they'd likely need to abstract over separate backends like `fuser` for Unix systems and either WinFsp or Windows' native ProjFS for Windows. The practical answer is that file watching is well-solved cross-platform, but true filesystem interception requires OS-specific implementations.Yes, the watching layer is well-abstracted; the FUSE layer less so but still doable.

**For event watching (cross-platform, mature):**

- **Rust: `notify` crate.** The standard. Wraps inotify (Linux), FSEvents (macOS), ReadDirectoryChangesW (Windows), kqueue (BSD). Has `PollWatcher` as a fallback for network filesystems where native events don't propagate. Pair it with `notify-debouncer-full` for the editor-rename-coalescing problem. This is what most Rust tooling (cargo-watch, etc.) uses.
- **JS: `chokidar`.** Same idea, same abstraction. Handles all the platform quirks — atomic-write detection, polling fallback, recursion. ~every Node tool that watches files (webpack, nodemon, vite) is using it under the hood. The newer `parcel-watcher` (native bindings, used by Parcel) is faster on large trees if perf matters.

Both give you a uniform API: subscribe to a path, get `add`/`change`/`unlink` events, done. Platform differences mostly disappear except for edge cases (Windows file locking, macOS case-insensitivity).

**For FUSE-style interception (cross-platform, messier):**

There's no single library, but there's a portable *pattern*: write to an abstraction trait and back it with the per-OS implementation.

- **Linux/macOS:** `fuser` (Rust) or `node-fuse-bindings` (JS, less maintained). macOS needs macFUSE installed by the user, which is friction.
- **Windows:** **WinFsp** is the FUSE-API-compatible layer — `winfsp-rs` exists. Or use **ProjFS** (Projected File System), Microsoft's native virtualization API, which is what Git VFS for Windows uses. ProjFS is actually nicer than FUSE for read-heavy workloads because files materialize lazily on access.

The honest take for OpenClaw: I'd build the versioning core as a trait/interface (`fn on_write(path, bytes) -> Result<()>`) and have two backends — a `notify`-based observer for "just watch a normal directory" mode (works everywhere, no install friction, can't intercept), and a `fuser`/WinFsp-based interceptor for "real versioned workspace" mode. Most users start with the observer; power users opt into the FUSE mount. That sidesteps the cross-platform FUSE install pain for the 80% case while keeping the door open for full interception when someone wants it.

---
**HUMAN** (2026-04-18T17:37):

For git, how does it work? Can I use it everytime a file changes

---
**ASSISTANT** (2026-04-18T17:37):

 Git doesn't watch files — it's purely on-demand. When you run `git status`, `git add`, or `git commit`, git walks the working tree, stats every tracked file, compares mtime/size against the index, and for anything that looks changed, hashes the content to confirm. Nothing is happening between commands. The "magic" is just that the index (`.git/index`) caches stat info so repeat scans are fast.

The storage model is what's interesting and why it composes well with what you're building: every file version is stored as a **blob** under `.git/objects/`, named by SHA-1 of its content (content-addressed, like we discussed). Identical content across files or commits = one blob. A **tree** object lists filenames + blob hashes for a directory. A **commit** points to one tree + parent commit(s). That's the whole data model — a Merkle DAG of immutable objects. Branches are just movable pointers to commits.

**Can you commit on every file change?** Yes, and people do. Two approaches:

**Approach 1: watcher + `git commit`.** Use `chokidar`/`notify` to watch the working tree, debounce events (200–500ms — editors save in bursts), then shell out to `git add -A && git commit -m "auto"`. Works everywhere, dead simple, ~50 lines. Downsides: every commit runs the full stat-walk (slow on large trees), commit history becomes noisy, and you get race conditions if a commit fires while another save is in flight. For a single-user agent workspace under maybe 10k files this is totally fine.

**Approach 2: write blobs directly.** Skip `git commit` and use `git hash-object -w <file>` to write a blob to `.git/objects/` on every change, then periodically (or on demand) assemble trees and commits. This is what tools like **`git fsmonitor`** + Watchman do under the hood — Watchman watches the FS, tells git "only these paths changed since last query," and git skips the full walk. Microsoft built this for the Windows repo (3.5M files) where naive `git status` took 25+ seconds. Modern git (2.37+) ships with a built-in fsmonitor daemon — `git config core.fsmonitor true` turns it on.

**For OpenClaw specifically**, I'd actually look hard at using libgit2 (Rust: `git2` crate, JS: `nodegit` / `isomorphic-git`) rather than shelling out. You get the same object store and Merkle DAG, but you can write blobs and trees programmatically without invoking the CLI. Combined with your FUSE layer, the natural design is: every write through FUSE → hash content → write blob via libgit2 → update an in-memory tree → commit on session boundaries (or every N writes, or on agent task completion). You get git-compatible history for free, and any human can `git log` the agent's work.

The really nice property: because git blobs are content-addressed, your FUSE layer's content-addressed storage *is* git's object store. They're the same thing. You're not building two systems.

---
**HUMAN** (2026-04-18T17:42):

Approach 2: write blobs directly is interest, is there an api my program can use?

---
**ASSISTANT** (2026-04-18T17:42):

 
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

 I've confirmed that both libgit2 and isomorphic-git provide the low-level primitives Ren needs—writeBlob, writeTree, writeCommit, and reference manipulation—so I can give him practical examples across Rust and JavaScript.Yes — both Rust and JS have clean programmatic APIs for exactly this. You never shell out to `git`.

## Rust: `git2` crate (libgit2 bindings)

The three primitives you need:

```rust
use git2::{Repository, ObjectType, Signature, Oid};

let repo = Repository::open(".")?;  // or Repository::init(".")?

// 1. Write a blob from raw bytes — returns the SHA (Oid)
let blob_oid: Oid = repo.blob(b"file contents here")?;
// or from a file path:
let blob_oid = repo.blob_path(Path::new("somefile.txt"))?;

// 2. Build a tree using a TreeBuilder
let mut tb = repo.treebuilder(None)?;  // None = empty tree, or pass parent tree
tb.insert("somefile.txt", blob_oid, 0o100644)?;  // 0o100644 = normal file
tb.insert("subdir", some_subtree_oid, 0o040000)?; // 040000 = dir
let tree_oid = tb.write()?;
let tree = repo.find_tree(tree_oid)?;

// 3. Write a commit
let sig = Signature::now("openclaw", "agent@openclaw")?;
let parent = repo.head().ok().and_then(|h| h.target()).and_then(|oid| repo.find_commit(oid).ok());
let parents: Vec<&_> = parent.iter().collect();

let commit_oid = repo.commit(
    Some("HEAD"),      // update HEAD ref
    &sig, &sig,
    "agent write: foo.txt",
    &tree,
    &parents,
)?;
```

That's the whole loop. On every FUSE write: `repo.blob(bytes)` → update your in-memory tree builder → periodically flush as a commit.

**Key APIs to know in `git2`:**
- `repo.blob()` / `repo.blob_path()` — write blobs
- `repo.treebuilder()` — assemble trees (you can pass an existing tree as the base and mutate)
- `repo.commit()` — write commits and optionally move a ref atomically
- `repo.odb()` — the raw object database if you want to bypass all of the above and write arbitrary objects
- `repo.reference()` / `repo.reference_matching()` — manipulate refs directly if you want to commit to something other than HEAD (e.g., a per-agent branch)

The `odb()` escape hatch is useful: `repo.odb()?.write(ObjectType::Blob, bytes)` is the lowest-level call and avoids any working-tree assumptions. For a bare object store (no checked-out files, just versioning) this is what you want.

## JavaScript: `isomorphic-git`

Same primitives, similar shape. The API exposes writeBlob, writeCommit, writeObject, writeRef, writeTag, and writeTree as individual functions:

```js
import * as git from 'isomorphic-git'
import fs from 'fs'

const dir = '/path/to/repo'

// 1. Write blob
const blobOid = await git.writeBlob({ 
  fs, dir, 
  blob: new Uint8Array(buffer)  // your file bytes
})

// 2. Write tree
const treeOid = await git.writeTree({
  fs, dir,
  tree: [
    { mode: '100644', path: 'foo.txt', oid: blobOid, type: 'blob' },
    { mode: '040000', path: 'sub',     oid: subTreeOid, type: 'tree' },
  ]
})

// 3. Write commit
const parentOid = await git.resolveRef({ fs, dir, ref: 'HEAD' }).catch(() => null)
const commitOid = await git.writeCommit({
  fs, dir,
  commit: {
    tree: treeOid,
    parent: parentOid ? [parentOid] : [],
    author:    { name: 'openclaw', email: 'agent@openclaw', timestamp: Math.floor(Date.now()/1000), timezoneOffset: 0 },
    committer: { name: 'openclaw', email: 'agent@openclaw', timestamp: Math.floor(Date.now()/1000), timezoneOffset: 0 },
    message: 'agent write: foo.txt\n',
  }
})

// 4. Move the branch ref
await git.writeRef({ fs, dir, ref: 'refs/heads/main', value: commitOid, force: true })
```

isomorphic-git is a pure JavaScript reimplementation that aims for 100% interoperability with canonical git — it modifies files in a .git directory just like normal git, so anything you write is readable by the regular `git` CLI. Nice property for debugging: you can `git log` the agent's activity from the shell.

One thing to watch on Node: LightningFS (the companion in-memory FS) may apply operations out of order and can corrupt the repo on crash — call fs.flush() after git operations to mitigate. If you're on native Node fs this doesn't apply.

## For the OpenClaw design

The pattern I'd suggest, given the FUSE-layer architecture we've been discussing:

**Hot path (inside FUSE write handler):**
1. Hash + `odb.write(Blob, bytes)` — this is cheap, ~one syscall + a zlib compress. Returns an OID.
2. Update an in-memory tree representation (a `BTreeMap<PathBuf, Oid>`).
3. Return from the write immediately — no commit yet.

**Cold path (debounced, every N ms or N writes or on agent task completion):**
4. Materialize the in-memory tree → `treebuilder.write()` → `commit()` → move the branch ref.

This keeps FUSE writes fast (you're only doing what you'd do anyway for content-addressed storage — the "git part" is free because the object format is the same), and it means the commit graph reflects semantic units of work (task boundaries) rather than every byte flush.

A refinement worth considering: **per-agent branches.** Each agent writes to `refs/heads/agent/<id>`, and the orchestrator merges to `main` on task completion. You get isolation, parallel exploration, and easy rollback for free from git's data model. This composes cleanly with the SST delegation model — a Sprite's workspace = a branch.

---
**HUMAN** (2026-04-18T17:44):

so fuse is better? how does it work in integration

---
**ASSISTANT** (2026-04-18T17:46):

  The user is asking me to clarify whether FUSE is actually better than the alternatives we discussed, and more importantly, how it would integrate into their OpenClaw system alongside the git blob approach we just covered. I need to figure out what comparison they're making—whether it's against file watchers, eBPF/fanotify, or something else—and then explain the practical integration path.

For their versioning use case, FUSE has real advantages: it intercepts writes atomically before they hit disk, so you can capture every agent modification without race conditions or missed events. The tradeoff is that it requires additional dependencies and adds syscall overhead, plus there's complexity around what happens if the FUSE daemon crashes. Compared to pure observation tools like eBPF, FUSE lets you actually transform or reject writes, not just watch them happen.

The integration would work by mounting a virtual filesystem at a specific path—the agent sees a normal directory but every read and write operation gets intercepted by your program, which can then version the changes through git before letting them through. The remaining filesystem operations—listing directory contents, returning file metadata—feed into a commit strategy where the in-memory tree periodically gets written as a git object and committed with the previous commit as parent. This mirrors what VFS for Git does but applied to agent versioning instead.

For OpenClaw specifically, I need to think through the lifecycle (mounting at session start, handling daemon crashes), whether each agent gets its own mount or they share one with namespacing, tuning FUSE timeouts since there's no external filesystem churn, serializing concurrent tree updates across parallel agent operations, bootstrapping from an existing branch by loading its tree into memory, and potentially letting certain paths passthrough to the real filesystem while others stay git-backed.

On whether FUSE is actually better—it's better *for atomic versioning and interception*, but watchers win on friction and compatibility since they don't need a daemon or special setup. I should clarify that distinction, walk through the actual daemon architecture and callback model, sketch out how it integrates with the git backing store, flag the real gotchas around lifecycle and platform support, and probably show what the concrete OpenClaw architecture looks like.

I'm thinking a Rust example with fuser since that's the stack, but keeping it architectural—just a minimal callback skeleton showing where the git write hooks in. I want prose with maybe one code block, nothing heavy, since the user is technical and building this so they need substance over structure.

The real distinction is that FUSE gives you atomic capture in the write path itself, which matters for OpenClaw's versioning use case where the layer needs to be authoritative. Watchers are fine for logging what happened, but they miss the atomicity guarantee and can drop events under load. There's a tradeoff though: FUSE requires macFUSE or WinFsp, adds metadata overhead, and if the daemon crashes the mount goes down. Watchers have zero install friction and integrate seamlessly with existing tools, but they're inherently reactive. For this specific job—where every agent write needs to be captured and versioned before commit—FUSE is the better choice.

Now I'm sketching out the actual architecture: a single process with three layers, built in Rust using the `fuser` crate. The core structure holds a git repository as the backing store, an in-memory tree mapping paths to git object IDs, a branch reference for the agent, and a bidirectional map between FUSE inodes and filesystem paths since FUSE and git speak different languages. Implementing the filesystem trait...

Implementing the write handler... I'm setting up the commit mechanism so the agent can decide when to snapshot the in-memory tree into git history—when a write completes, I materialize the tree into git objects, find the parent commit on the current branch, and prepare to create a new commit with a signature.

Now I'm thinking through the integration points for OpenClaw, particularly how each agent gets its own branch to track changes independently. ts its own FUSE instance backed by its own ref. Isolation is automatic. Merging = git merge.
- **Shared bare repo, multiple mounts.** All agents share one `.git/objects/` directory (content-addressed, so writes dedup across agents for free). Only the refs and the in-memory tree differ per mount.
- **Hybrid passthrough.** Some paths should hit the real disk: `/node_modules`, `/.venv`, `/tmp`. You implement these by proxying to real `fs::` calls in your FUSE callbacks when the path matches a passthrough prefix. Saves you from versioning build artifacts.
- **Read-through from parent branch.** On mount, you don't have to load the entire tree into memory — lazily resolve paths against the git tree object and only pull into your mutable map when written. This is what ProjFS does on Windows; it's what makes VFS-for-Git scale to 3.5M files. If the daemon crashes, the mount goes stale, but you recover by bootstrapping from the branch ref — committed state survives, in-memory changes don't, which is why frequent commits at tool-call boundaries matter.

The elegance here is that the FUSE filesystem, the content-addressed blob store, and the git history are all one unified system — no separate syncing needed. The core insight is that FUSE lets the daemon become the filesystem itself, with git as the persistent backing store underneath — and you get to decide when to commit, so write boundaries aren't tied to individual file operations but to meaningful semantic checkpoints instead. I should keep the focus tight, acknowledge the tradeoffs honestly, and maybe show a concrete integration example without overdoing it."Better" is conditional — FUSE is better for *atomic versioning*, where you need every agent write captured before it commits to disk and you want the ability to transform or reject. Watchers+git are better for the "just observe normal directory activity" case because there's zero install friction and the user's shell/editor/git CLI keep working unchanged. For OpenClaw's versioning core, FUSE wins because atomic capture is the whole point.

**How integration actually looks**

Your program *is* the filesystem. You're not interacting with FUSE as an external service — you implement a trait, call `mount()`, and the kernel starts routing syscalls to your methods. Sketch in Rust with `fuser`:

```rust
struct OpenClawFS {
    repo: git2::Repository,         // git object DB is the backing store
    tree: HashMap<PathBuf, Oid>,    // current working tree (in-memory)
    branch: String,                 // e.g. "refs/heads/agent/42"
    inode_map: BiMap<u64, PathBuf>, // FUSE speaks inodes, git speaks paths
}

impl Filesystem for OpenClawFS {
    fn write(&mut self, _req: &Request, ino: u64, ..., data: &[u8], reply: ReplyWrite) {
        let path = self.inode_map.get_path(ino);

        // The agent's write() syscall is paused here. We have the bytes.
        // This is the atomic-capture moment that watchers can't give you.
        let blob_oid = self.repo.blob(data).unwrap();
        self.tree.insert(path, blob_oid);

        reply.written(data.len() as u32);
    }

    fn read(&mut self, _req: &Request, ino: u64, ..., reply: ReplyData) {
        let path = self.inode_map.get_path(ino);
        let blob_oid = self.tree.get(&path).unwrap();
        let blob = self.repo.find_blob(*blob_oid).unwrap();
        reply.data(blob.content());
    }

    // + getattr, readdir, create, unlink, rename, lookup, etc.
}

fn main() {
    let fs = OpenClawFS::bootstrap("refs/heads/agent/42");
    fuser::mount2(fs, "/workspaces/agent-42", &[MountOption::FSName("openclaw")])?;
    // blocks until unmount
}
```

The agent sees `/workspaces/agent-42` as a normal directory. `echo hello > foo.txt` → kernel routes the syscall to your `write()` → blob hashed into `.git/objects/` → in-memory tree updated → `reply.written()` releases the syscall. From the agent's POV nothing weird happened. From yours, the write is now in the content-addressed store before it was "finished."

**Commit boundaries are your choice, not per-write.** The in-memory tree is the live working state. Periodically (task completion, tool-call boundary, every N writes, timer) you materialize it:

```rust
fn snapshot(&mut self, msg: &str) -> Oid {
    let tree_oid = self.build_tree();               // walk HashMap → TreeBuilder → write
    let parent   = self.repo.refname_to_id(&self.branch).ok();
    let sig      = Signature::now("agent", "agent@openclaw").unwrap();
    self.repo.commit(Some(&self.branch), &sig, &sig, msg, 
                     &self.repo.find_tree(tree_oid).unwrap(), &parent_commits).unwrap()
}
```

**Integration points that matter for OpenClaw:**

*Per-Sprite mounts, shared object store.* Each Sprite gets its own FUSE mount backed by its own branch, all sharing one `.git/objects/` directory. Content-addressed storage means identical writes across Sprites dedup automatically. Merging workspaces = git merge. Rollback = reset the ref.

*Lazy tree loading.* Don't load the full tree into the HashMap at mount time. On `lookup`/`read`, resolve the path against the git tree object on demand, cache the result. This is the trick that lets VFS-for-Git handle 3.5M files without choking. For small agent workspaces it doesn't matter, but it's the difference between "this works for a scratch dir" and "this works for a real codebase mounted from the main branch."

*Passthrough for non-versioned paths.* `node_modules/`, `.venv/`, `target/`, `.cache/` should hit the real disk — you don't want every `npm install` generating 50k blobs. Match these prefixes in your callbacks and proxy to `std::fs` directly.

*Crash recovery = commit frequency.* If your daemon dies, the mount becomes stale (reads return EIO) and anything in the in-memory tree that hadn't been committed is lost. What's committed is durable. This is the argument for snapshotting on every tool-call boundary, not every N minutes. Agents do discrete work; commit when a discrete unit finishes.

*Attr/entry timeouts.* Since the agent is the only writer, you can set `attr_timeout=3600` and `entry_timeout=3600` aggressively. The kernel will cache `stat` results and skip round-tripping to your daemon for the vast majority of metadata ops. This is where the "FUSE is slow" narrative mostly comes from — untuned mounts.

**The elegant thing:** your filesystem, your content-addressed blob store, and your git history are the same data structure. You're not building three things that need syncing — you're building one thing (a git object DB) and exposing it through FUSE for live writes and `git log` for human inspection. The SST model lines up naturally: a Space = a branch, a Sprite's workspace = the mount, Tokens granting write access = permission to advance the ref. The merge story, the audit story, the rollback story, and the "let me see what the agent did" story all reduce to operations git already supports.

---
**HUMAN** (2026-04-18T17:48):

let say for example another use case, can i use this to replace database, or do i need a database? what if i have 100k users and give them each a folder they have freedom to use

---
**ASSISTANT** (2026-04-18T17:48):

 Short answer: you still want a database, but the filesystem/git store isn't replaced by it — they do different jobs. Use the filesystem for what filesystems are good at (blob storage, hierarchical namespaces, sequential I/O) and the database for what databases are good at (indexed queries across users, transactions, aggregations, auth).

**What a filesystem alone can't answer cheaply at 100k users:**

- "Show me all users who signed up in the last 7 days" — requires scanning 100k directories.
- "How many total files across all users?" — same problem.
- "Give me users whose quota exceeds 1GB" — you'd have to `du` everything.
- "Authenticate this session token" — you need an indexed lookup by token, and you need it in single-digit milliseconds on every request.
- "List this user's files sorted by last modified, paginated 50 at a time" — doable but slow if they have 100k files; trivial if there's an index.
- "Atomically deduct credits and create a file" — no cross-system transaction.
- Full-text search, tag search, shared-with-me views, any relational query — FS gives you none of this.

The filesystem indexes by path. Any query that's not "give me the thing at this path" becomes a linear scan. Databases exist because that class of query is ~every query a real app needs.

**The split you actually want:**

*Filesystem (or git-backed object store) holds:* file contents, directory structure, per-user working trees. The bytes.

*Database holds:* users table, sessions, per-file metadata rows (owner, size, mime, created_at, hash, maybe tags), quotas, billing, audit log, sharing/ACLs, search indexes. Everything you'd ever want to query by something other than path.

The metadata row points at the blob (by hash, or by path, or by git OID). This is the pattern from your first question in this thread — it's the same answer, it just scales.

**At 100k users specifically, some concrete issues:**

*Inode/directory-entry pressure.* 100k top-level directories is fine on ext4/xfs, but if each user has 10k files, you're at 1B inodes. Do-able, but backup and `fsck` times get painful. Shard: `users/a3/a3f7.../...` (hash-prefixed) rather than `users/ren/...` flat.

*fs quotas don't scale per-user the way you want.* Linux supports per-UID quotas, but you're not going to give each of 100k users a real UID. You'll track quotas in the DB and enforce in app code.

*No atomic multi-user operations.* "Transfer this file from user A to user B and update both their quotas" — on FS alone, you get to reinvent two-phase commit. In a DB, it's a transaction.

*Concurrent writes to the same file* — FS gives you POSIX locking which nobody uses correctly. DB gives you row-level locking or MVCC.

*Backup/restore granularity.* Restoring one user from a full FS backup is a pain. Restoring one user from DB + object storage is a query + a prefix listing.

**The architecture at 100k users that actually works:**

- **Object storage for blobs** (S3/R2/MinIO, or your own disk with content-addressed paths). Files keyed by hash, not by user path. One copy of any identical file no matter how many users have it.
- **Postgres for metadata**, with tables roughly like: `users`, `files (id, owner_id, parent_folder_id, name, blob_hash, size, mime, created_at, updated_at)`, `folders`, `sessions`, `shares`. Index on `owner_id`, `blob_hash`, `(owner_id, parent_folder_id)`.
- **Per-user "filesystem" is a view constructed from the metadata table.** The user's "folder structure" is rows in `folders` + `files`. There isn't a literal directory on disk called `/users/ren/projects/` — there's a row for it.
- **Git/versioning layer optional, per-user.** If versioning matters per user, each user gets their own bare git repo (or their own branch in a shared object store, since git objects dedup globally by hash). libgit2 calls, same pattern as before.

This is basically how Dropbox, Google Drive, GitHub, and every file-hosting service is built. Nobody gives 100k users literal directories on a shared filesystem as the source of truth. The filesystem is an implementation detail under the metadata store.

**When a folder-per-user *does* work:**

- Small scale (<1000 users) where linear scans are fine.
- Single-tenant deployments (one user per instance — like how Nextcloud can run).
- When the "users" are actually trusted developers with shell access and the folder *is* the product (think: shared Unix server, 1990s web hosting, JupyterHub deployments).
- Read-heavy, rarely-queried workloads where the path IS the query (static site hosting, CDN origins).

**For your 100k-user case specifically,** I'd ask what the users are actually doing in their folder — because the answer changes the shape significantly:

- If it's "each user has a workspace with agents doing things" → one git repo per user, libgit2 for writes, Postgres for user/session/quota/billing. The FUSE layer is optional per-user (only power users who want a live mount).
- If it's "users upload and share files" → object storage + Postgres, no per-user FS at all. Folders are rows.
- If it's "users run code that reads/writes files" → container-per-user with an ephemeral FS, persistent state in object storage + DB.

Which of these is closer to what you're thinking about?

---
**HUMAN** (2026-04-18T17:50):

if This is basically how Dropbox, Google Drive, GitHub, and every file-hosting service is built, is there open source versions?

---
**ASSISTANT** (2026-04-18T17:51):

 Yes, plenty — and they cluster into a few categories depending on what "like Dropbox/Drive/GitHub" means to you.

**Dropbox/Drive-style (file sync + sharing, folder-per-user UX):**

- **Nextcloud** — the 800lb gorilla. PHP, MySQL/Postgres + filesystem (or S3) backend. Handles sync clients (desktop/mobile), sharing, ACLs, versioning, collaborative editing via plugins. Self-hostable, mature, used by governments and universities. Heavy if you just want storage, but it's the reference implementation of "open-source Drive."
- **Seafile** — C core, faster than Nextcloud for pure sync. Interesting architecturally: it stores files as content-addressed blocks (basically git's model applied to a sync product). If you're building something git-blob-based, Seafile's source is worth reading.
- **ownCloud** (now split into ownCloud Infinite Scale, Go-based) — Nextcloud's predecessor, rewritten for scale.
- **Pydio Cells** — Go, microservices architecture, more enterprise-shaped.
- **FileRun, Syncthing** (Syncthing is P2P, no central server — different model but same problem space).

**GitHub-style (git hosting + collaboration):**

- **Gitea** / **Forgejo** (Forgejo is a Gitea fork with stronger community governance). Go, SQLite or Postgres + filesystem for repos. Lightweight, single binary, runs on a Raspberry Pi. The pragmatic default.
- **GitLab** (Community Edition) — full DevOps platform, Ruby on Rails + Postgres. Heavyweight but complete.
- **Codeberg** — a public Forgejo instance, interesting as a model of how to run it.
- **Soft Serve** (Charm) — terminal-first, minimalist, Go.

**Storage backends (the "blobs" layer, not the user-facing product):**

- **MinIO** — S3-compatible object storage, Go, single binary. De facto standard for self-hosting.
- **SeaweedFS** — distributed, handles billions of small files well (Facebook Haystack–inspired). Good when you have lots of tiny blobs.
- **Garage** — Rust, designed for geo-distributed deployment on commodity hardware, lightweight.
- **Ceph / OpenStack Swift** — enterprise-scale, operationally heavy.
- **Juicefs** — interesting hybrid: presents as a POSIX filesystem (FUSE), stores blobs in object storage, metadata in Redis/Postgres/TiKV. Literally the architecture we've been discussing, implemented.

**The one to actually look at for your purposes: JuiceFS.** It's the cleanest open-source example of the exact pattern — FS interface on top of (object store + metadata DB) — and the code is readable Go. If you're designing Nomad OS storage or OpenClaw workspaces, it's worth reading how they handle the metadata schema, caching, and consistency model. Seafile for the content-addressed block store angle, JuiceFS for the metadata-DB-backed FS angle.

**What to steal vs. what to build:** if the goal is "give 100k users a workspace," Nextcloud or Gitea will get you 80% there day one, and you'll spend your time on the 20% that's actually OpenClaw-specific (agent integration, SST-aware permissions, Nomad OS billing). If the goal is to *learn* how these systems work, read Seafile and JuiceFS source. If the goal is to build the storage primitive for something more novel (agent workspaces with native versioning + delegation), you're probably better off composing MinIO + Postgres + libgit2 yourself, because the existing products assume a human-sync-client UX that doesn't fit agents.

---
**HUMAN** (2026-04-18T17:54):

let's say we use juicefs, how will us use hooks/events

---
**ASSISTANT** (2026-04-18T17:55):

  The user is asking about event hooks and notifications in JuiceFS—specifically how to get alerted when files change if you're using JuiceFS as your storage backend. I'm thinking through what JuiceFS actually is (a FUSE filesystem with metadata in databases like Redis or Postgres and object data in cloud storage) and considering the different angles for how file change events might work in that architecture.

I should verify what JuiceFS actually supports here, since this is a specific product question where my knowledge might be outdated—I'm wondering whether JuiceFS has native hooks, whether standard Linux tools like inotify would work on top of it, if you could tap into the underlying metadata database for change detection, or if there's a webhook or plugin system I'm not aware of.
```
This block is not supported on your current device yet.
```

 So JuiceFS doesn't natively support inotify or fanotify events according to their documentation—file monitoring only works through polling. The mount point that initiates changes can detect them via fswatch or Watchdog, but that's limited to its own writes and doesn't capture changes from other mounts.

JuiceFS does have an internal metadata change event subscription system that clients use for cache consistency, and the S3 Gateway supports MinIO-style bucket event notifications through Redis or message queues. For Ren's use case, the most practical options are tapping into the metadata database directly with Redis pub/sub or Postgres LISTEN/NOTIFY, using the S3 Gateway with bucket notifications, polling with Watchdog, or running a dedicated writer daemon that emits events. The metadata database approach is particularly elegant for OpenClaw's SST workflow since the metadata already lives in a queryable database.Good question to ask before committing — JuiceFS has a specific gotcha here. The obvious approach doesn't work, but there are several viable paths and one is actually very elegant for your architecture.

**The gotcha: inotify doesn't work on JuiceFS mounts.**

Straight from their docs: because FUSE doesn't yet support the inotify API, if you want to monitor file change events using libraries like Watchdog, you can only achieve this via polling (e.g. PollingObserver). And the mount point initiating changes has access to file change events (via fswatch or Watchdog), but the scope is limited to files changed within that mount point itself — files modified by mount A cannot be monitored by mount B.

Translation: if you were hoping to mount JuiceFS and slap `chokidar`/`notify` on top, you'd be stuck polling, and you'd miss all cross-node writes anyway. Not great for a 100k-user system where writes come from many nodes.

**The four real options:**

**1. Tap the metadata DB directly.** This is the elegant one. JuiceFS stores all metadata (file names, sizes, parent dirs, mtimes) in Redis/Postgres/TiKV. Every write goes through it. Hook there:

- *Redis metadata*: use `MONITOR` for debugging, or keyspace notifications (`CONFIG SET notify-keyspace-events KEA`) for production. You'll receive events on every key change. Noisy — you'll need to filter for JuiceFS's inode/dentry key patterns — but it's real-time, cross-node, and doesn't require cooperation from the clients.
- *Postgres metadata*: `LISTEN`/`NOTIFY` triggered from a trigger on the inodes/dentries tables. Even cleaner — you can filter in SQL and emit structured events.
- *TiKV*: harder, no native pub/sub, but you can use its CDC (change data capture) facility.

JuiceFS itself already uses this pattern internally — clients subscribe to metadata and listen for change events to invalidate their caches when files are modified. You're just piggybacking on the same channel from an external subscriber.

**2. Use the S3 Gateway with bucket event notifications.** If clients access JuiceFS through its S3 Gateway rather than POSIX mount, you get MinIO-style event notifications: the bucket event notification feature triggers notifications when specific events occur within a bucket — S3 Gateway writes the event to a configured publishing system (like a message queue) where other tools can retrieve records in real time. Supports Redis, Kafka, NATS, webhooks, etc. Downside: only triggers for writes that go through the S3 API, not POSIX mounts. Works if you design your app to write via S3 to JuiceFS (which is common for user-upload workflows anyway — SDKs handle it).

**3. Polling.** `watchdog`'s `PollingObserver`, or just your own periodic `readdir` + mtime comparison. Fine for 100 directories. Awful for 100k users × 10k files each. Skip.

**4. Application-layer events.** Your API server is the only thing writing to JuiceFS. When a user uploads, your server writes the file AND emits an event to your queue/pubsub in the same code path. You don't try to detect changes from the FS — you already know when they happen because you caused them. This is the pragmatic default for most SaaS products and arguably the right answer unless you have multiple write paths.

**Recommendation for your 100k-user case:**

Probably a hybrid. **Option 4 (app-layer events) as primary**, because you control the write path and it's the simplest and most reliable. Every file write in your API handler emits an event to a queue (NATS, Redis streams, Kafka — you already like Redis/Postgres-backed stacks). Downstream consumers handle indexing, quota tracking, webhooks to user integrations, agent triggers, etc.

**Option 1 (metadata DB tap) as a safety net** for things your app doesn't write directly — admin tools, migration scripts, direct mounts by power users. Hook Postgres `LISTEN`/`NOTIFY` on the JuiceFS metadata tables, emit to the same event bus. Deduplicate downstream if both fire.

**For your OpenClaw/SST layer on top of this**: the metadata DB tap actually becomes structurally interesting. Every Sprite write → metadata row change in Postgres → `NOTIFY` → your SST coordinator sees the write and can update Token accounting, trigger dependent agents, record to the audit log, etc. All without the SST layer having to wrap the filesystem — JuiceFS handles the FS concerns, the DB trigger is your event bus, SST is orchestration. Clean separation.

The one thing JuiceFS doesn't give you that a custom FUSE layer would: **pre-write interception**. You can observe writes; you cannot block or transform them. If that matters (e.g., Token-based permission enforcement at write time, content-addressed versioning captured atomically), you're back to building on top of `fuser` directly — or running JuiceFS as the storage backend and a thin custom FUSE layer in front as the policy/versioning layer. Two-layer architecture, but each layer is doing one thing well.

---
**HUMAN** (2026-04-18T18:03):

any other elegant solutions that allows me to scale to 100k and use file system

---
**ASSISTANT** (2026-04-18T18:03):

 Yes — a few worth knowing about, each with a different philosophy. I'll order them by how "elegant" (in the sense of "composes well, small surface area, scales without surprises") they are for your use case.

**1. CephFS + its native notification API**

Ceph is the old guard of distributed POSIX, but the thing people miss: CephFS has a native inode-level change notification system (`ceph fs subvolume`, snapshot diff, and the lower-level recursive stats via `rstat`). Every directory in CephFS maintains recursive statistics (file count, byte count, rctime = recursive mtime) that propagate up the tree in real time. You can cheaply ask "did anything change under this subtree since timestamp X?" without walking it. Combined with snapshots (which are cheap, copy-on-write), you get efficient "what changed between T1 and T2" diffs for any subtree. At 100k users this is genuinely nice — each user is a subvolume, you query their `rctime` to know if anything changed.

Operational cost is real though. Running Ceph well is a job. Don't pick this unless you already have Ceph expertise or the scale justifies it.

**2. SeaweedFS with its filer notification system**

SeaweedFS is the hidden gem for your exact shape of problem. It's designed around "lots of small files across lots of users," has a pluggable filer with metadata in your choice of DB (Postgres, Redis, Cassandra, etc.), and has a **native notification system**: every filer operation (create, update, delete) can be published to Kafka, RabbitMQ, NATS, AWS SQS, or Google Pub/Sub out of the box. No hooks to write, no metadata DB tapping — it's a config option.

It also has per-user mount support via its FUSE client, a built-in S3 gateway, WebDAV, and can use content-addressed chunks (dedup for free). Facebook's Haystack paper is the ancestor. It scales well to billions of files. Go, single binary, genuinely easy to run.

For 100k users with per-user workspaces + event-driven architecture, SeaweedFS is probably the most direct fit. You get the FS UX, the events are native, and the metadata lives in a DB you already query.

**3. Garage + S3 event notifications + a thin FUSE layer**

Garage (Rust, by Deuxfleurs) is what I'd reach for if you want S3 semantics with sane ops. It's lighter than MinIO, geo-distribution-first, runs on commodity hardware. S3-compatible, so events come via the standard S3 notification config. Pair with `s3fs-fuse` or `rclone mount` per user for POSIX UX when needed.

The elegance here: you're not running a "filesystem" at all. You're running object storage + metadata DB + optional FUSE-per-session. The FUSE mount is ephemeral — spin it up when the user connects, tear down on disconnect. No persistent mount tree to manage across 100k users.

**4. Content-addressed store + per-user "virtual filesystem" materialized on demand**

This is the architecturally interesting one, and it fits your instincts about git-style storage.

- **Blobs**: content-addressed in S3-compatible storage (Garage/MinIO/Seaweed). One copy globally; identical files across users dedup automatically.
- **Per-user tree**: a git-like tree object in Postgres (or git itself via libgit2, one bare repo per user, all sharing `.git/objects/` — git does this safely via `alternates`).
- **FS view**: either a FUSE mount (materialized on demand) or an HTTP/WebDAV/S3 API that projects the tree for the user.
- **Events**: Postgres `LISTEN`/`NOTIFY` on the tree table, emitted when an agent/user modifies the tree. The event bus is your DB.

The elegant property: **everything reduces to git operations.** User uploads a file = write blob + update tree. Share a folder = a tree object referenced by two users. Snapshot = a commit. Rollback = move the ref. Diff two states = git tree-diff. Audit log = commit history. At 100k users, you have 100k refs pointing into one shared object store of maybe 1B blobs with massive dedup. This is essentially how GitHub stores everything; it's how Seafile works under the hood.

Write path: Postgres transaction that updates the tree + inserts an event row + `NOTIFY`. One transaction, atomic, observable. Read path: resolve tree to blobs, stream from object store.

**5. Apache Ozone or MooseFS**

Both are distributed POSIX filesystems with event/audit hooks. MooseFS has per-operation logging you can tail. Ozone is Hadoop-world but has modern event streams. Mentioning for completeness; I wouldn't reach for either first.

**6. The "skip the filesystem, keep the UX" option**

Worth naming explicitly: at 100k users, most successful products *don't* actually expose a real filesystem. Dropbox, Drive, Notion — the "folder" UI is projected from a DB. The filesystem is implementation detail. You get:

- Every event is an app event (no FS hook needed).
- Sharing, permissions, search, quotas are all just SQL.
- Versioning is cheap (store blob hash history per file row).
- Scaling is DB scaling, which is a known problem.

The FUSE mount becomes an *optional* view — power users who want `vim` in their workspace get a mount; most users never touch it. The source of truth is the DB + object store. This is what I'd actually recommend for Nomad OS–shaped products. It's less architecturally exciting than a "real" distributed filesystem, but it ships.

---

**My ranking for your specific situation** (100k SEA users, agent-capable workspaces, event-driven, you on solo-dev capacity):

1. **SeaweedFS** if you want a real filesystem with native events. Least operational friction, best fit for "users with folders + events."
2. **Content-addressed store (Garage/MinIO) + Postgres metadata + libgit2 per user** if versioning and agent workspaces are central. Most elegant, most work upfront, composes best with OpenClaw.
3. **Skip the filesystem entirely, project folders from Postgres** if users are end-users rather than developers. Fastest to ship, easiest to scale, least exciting.

CephFS only if you end up at 10M+ users and have an ops team. JuiceFS is fine but the event story is weaker than SeaweedFS for your shape of problem.

The question that would sharpen this: *who are the 100k users and what do they do in their folder?* A folder for an end-user's uploaded files (option 3), a folder for a developer's code (option 2), and a folder for an AI agent's workspace (option 2 with FUSE) have genuinely different optimal architectures even though the user-facing description is identical.

---
**HUMAN** (2026-04-18T18:09):

i actually want my agent to be able to access it like filesystem, maybe also run commands over them

---
**ASSISTANT** (2026-04-18T18:10):

 Got it — that changes the shape meaningfully. If agents need POSIX filesystem access *and* the ability to run shell commands over files, you need a real mounted filesystem, not a projection. Agents doing `grep -r`, `find`, `sed`, `ls | wc -l`, `python script.py`, `npm install`, `git clone` — all of that needs actual files at actual paths on an actual kernel filesystem.

This narrows the architecture significantly. Here's how I'd think about it:

**The core constraint: one sandboxed environment per agent (or per session), not one mount for all 100k users.**

You do *not* want 100k simultaneous FUSE mounts on one host. That's a recipe for kernel resource exhaustion, noisy-neighbor problems, and a security nightmare (one agent escaping its chroot touches 99,999 others). The workable shape is:

- **Persistent state**: lives in the shared content-addressed store + metadata DB (the pattern we've been discussing).
- **Ephemeral compute**: when an agent starts work, a sandbox spins up with *that agent's workspace* mounted or materialized inside it. Agent does stuff, commands run, files change. On session end, changes are committed back to the persistent store and the sandbox is destroyed.

Three ways to implement this, in increasing order of isolation:

**1. Container-per-session, FUSE mount inside**

Each agent session = one container (Docker, Podman, Firecracker microVM, gVisor, or your own runc wrapper). Inside the container, mount the agent's workspace via FUSE (JuiceFS, SeaweedFS-fuse, or your custom git-backed FUSE). Agent runs shell commands inside the container normally — `bash`, `python`, `git`, whatever — and the FS they see is their workspace.

This is what Replit, Modal, E2B, Daytona, Codespaces all do. It's the proven pattern for "give an AI/user a sandboxed computer." At 100k users you're not running 100k containers — you're running N containers where N = concurrent active sessions, probably 1–5% of your user base. Idle users have no running compute, just state in the store.

**2. Container-per-session, materialized workspace (no FUSE)**

Same as above, but instead of a FUSE mount, you `git clone` (or `rsync`, or pull the tree from your object store) into a regular directory inside the container at session start. Agent works on local ext4/overlayfs, which is *fast*. On session end, commit/push changes back to the persistent store.

This is the Codespaces / Gitpod / devcontainer model. It's simpler than FUSE, faster for I/O-heavy work (no per-syscall overhead), and lets you use plain inotify for events inside the session. The cost: slow session startup if the workspace is big (clone time), and you need to handle sync-on-exit carefully.

For most agent workloads this is actually the better choice. Agents tend to read/write a lot during a task (tool use, running tests, compiling), and FUSE overhead compounds. Clone at start + commit at end gives you native FS performance throughout.

**3. microVM per session (Firecracker / Cloud Hypervisor)**

If agents run untrusted code, containers are not enough isolation — a bad `rm -rf /` or a kernel exploit breaks out. Firecracker gives you VM-level isolation with ~125ms boot times and ~5MB memory overhead. This is what Fly.io, AWS Lambda, and Modal use under the hood. Workspace gets mounted via virtio-fs (the VM equivalent of FUSE, much faster) or materialized at boot.

For AI agents specifically, microVMs are increasingly the default because agents *will* run arbitrary code that you didn't write and can't fully predict.

---

**The architecture I'd actually build for OpenClaw at 100k-user scale:**

```
Persistent layer (always on):
├── Object store (Garage/MinIO/SeaweedFS) — content-addressed blobs
├── Postgres — metadata, refs, users, sessions, quota, audit log
└── Event bus (NATS/Redis streams) — write events for coordination

Ephemeral compute layer (on-demand):
├── Orchestrator (scheduler — you, or K8s, or Nomad-the-hashicorp-thing)
├── microVMs (Firecracker) — one per active agent session
│   ├── /workspace — materialized from git tree at VM boot
│   ├── bash, python, node, git, your CLI — normal userland
│   └── session agent — watches /workspace with inotify, emits events
└── Commit-on-exit — diff /workspace vs. origin tree, write blobs, update ref
```

A few properties worth highlighting:

*The agent's view is a normal Linux box.* It runs `ls`, `grep`, `npm install`, `python app.py`, spawns subprocesses, writes logs to `/tmp`. You don't need to teach the agent about your storage layer — it doesn't know there is one.

*inotify works inside the VM.* Because the workspace is a real ext4 filesystem inside the microVM (materialized from git at boot), standard watchers work. No FUSE limitations. Your session-local event collector runs inside the VM and streams interesting events out.

*Versioning is per-session.* Boot = checkout a branch. Exit = commit to the branch. Merge to main = explicit action. Rollback = move the ref. Parallel agent exploration = parallel branches. This maps directly onto the SST model: a Space is a branch, a Sprite's session is a checkout of that branch.

*Quota/resource enforcement is kernel-enforced.* Each microVM has its own memory, CPU, disk quota. An agent that writes a 100GB file just fills its VM's disk, not the shared filesystem. Clean.

*Sessions are cheap to start and kill.* Firecracker boots in ~125ms. If an agent stalls, kill the VM, lose the session, ref is still at last commit. Recovery = boot a new VM from the same ref.

**Tooling that already does most of this:**

- **E2B** (open-source-ish) — "sandbox for AI agents," Firecracker-based, has an SDK. Worth studying their architecture even if you don't use it.
- **Daytona** — open-source dev environment orchestrator, containers-based, FS-focused.
- **Modal** — not FS-focused but their sandbox primitive is the pattern.
- **Firecracker-containerd** — if you want to roll your own on Firecracker with a containerd-shaped API.
- **Kata Containers** — containers with VM-level isolation, OCI-compatible, drop-in for Docker.
- **devpod** — runs devcontainers anywhere, could be adapted.

**For shell command execution specifically:**

Inside each VM you want a small agent-side daemon that exposes an RPC interface (`exec(cmd, cwd, env) -> (stdout, stderr, exit_code)`), so your orchestrator can send shell commands without SSH-per-call overhead. Claude Code's shell tool is exactly this shape. Stream stdout back so the agent sees long-running output. Handle timeouts, signals, and stdin.

**The hard parts you'll hit:**

- **Cold-start vs. warm-pool.** First-session latency matters. Keep a pool of pre-booted VMs ready. Snapshot/restore (Firecracker supports this) to get sub-100ms session starts with a pre-populated workspace.
- **Persistent side effects.** Agents install packages, write to `~/.cache`, modify `$HOME`. Decide what's workspace (commits back) vs. ephemeral (thrown away). Usually: `/workspace` persists, everything else doesn't.
- **Resource limits for runaway agents.** Memory bombs, fork bombs, `dd if=/dev/zero`. VM-level limits catch these cleanly; container-level limits can be escaped.
- **Network policy.** Agents shouldn't see each other's sessions, shouldn't hit internal services, should have controlled egress. Per-VM network namespace.

---

**My concrete recommendation for OpenClaw specifically:**

Phase 1 (now, prove it works): containers with materialized workspaces. `git clone` at start, `git commit + push` at end, bind-mount the workspace dir, run agent commands via `docker exec`. Postgres for state, object store for blobs, use whatever you have for events. 1000 users easy.

Phase 2 (scaling, 10k+ users): swap Docker for Firecracker + virtio-fs, add snapshot/restore for fast session resume, warm pool for cold-start. Architecture doesn't change; the sandbox primitive does.

Phase 3 (100k+ users, distinct workloads): multi-region, regional object stores with cross-region replication for the metadata DB. Agents run near the user. This is where Nomad OS's SEA-regional focus becomes a real advantage — you're not pretending to serve Vietnam from us-east-1.

The insight worth internalizing: **you're not scaling a filesystem to 100k users. You're scaling a workspace orchestrator that gives each active session its own little Linux box.** The filesystem problem is small (per-session, ephemeral); the orchestration problem is the actual one, and it's well-understood because every cloud dev-env company has solved it.

---
**HUMAN** (2026-04-18T18:12):

This is what Replit, Modal, E2B, Daytona, Codespaces all do. It's the proven pattern for "give an AI/user a sandboxed computer."
find the open source version

---
**ASSISTANT** (2026-04-18T18:12):

  I need to look into what open source alternatives exist in this space, since the landscape changes pretty quickly and I want to give the user current information about sandboxed execution environments similar to what those platforms offer.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

 Let me take a closer look at microsandbox since it seems worth investigating further.Based on the current landscape (early 2026), here are the serious open-source options for the "sandboxed computer for agents" pattern, ordered by how they'd fit your situation:

**1. Daytona** — the current heavyweight

[github.com/daytonaio/daytona](https://github.com/daytonaio/daytona), AGPL-3.0, over 65,200 GitHub stars as of March 2026. Secure, scalable runtime for AI-generated code execution and agent workflows, providing sandboxes as full composable computers with complete isolation, a dedicated kernel, filesystem, and network. Under 100 milliseconds sandbox creation time, supports 10–30-minute sessions, with snapshotting, recovery, and forking so teams can save and restore progress or duplicate environments. SDKs in Python, TypeScript, Ruby, Go.

The snapshot/fork primitive is genuinely interesting for your SST model — fork = create a new Sprite workspace from a parent state. The architecture maps cleanly: Space = sandbox, Sprite = session within it, Token = API auth controlling what operations are allowed.

Trade-off: self-hosting Daytona is non-trivial — you'll need Kubernetes and DevOps expertise, as the system is composed of many microservices and requires significant infrastructure setup. Also AGPL-3.0 has network-use copyleft implications — fine if OpenClaw is open source, something to think about if it isn't. Solo-dev operability is real concern.

**2. E2B (self-hosted)** — the reference implementation

[github.com/e2b-dev/infra](https://github.com/e2b-dev/E2B). MIT licensed, deployed using Terraform, supports AWS and GCP, Azure listed but not green. Each sandbox is a Firecracker microVM. The org also publishes Surf (computer use), Desktop (graphical sandbox), and Fragments (Claude Artifacts clone).

E2B's self-host path is real and documented, but clearly designed to nudge you toward their cloud. The codebase is what you want to study if you're building your own — it's the cleanest example of the Firecracker + orchestrator + SDK pattern.

**3. Microsandbox** — the lightweight, self-host-first option

[github.com/microsandbox/microsandbox](https://github.com/microsandbox/microsandbox), ~3.3k stars. A younger, community-driven project positioned as a self-hosted, open-source alternative to commercial cloud sandboxing solutions, focused on running untrusted code securely using virtual machines with fast startup times.

The architectural choice is interesting: Microsandbox uses micro-virtualization with the libkrun library — every sandbox gets its own virtual machine with a dedicated kernel, using KVM on Linux or HVF on macOS. Lighter than Firecracker to deploy. Persistence: when using its "project sandbox" feature, any changes made to the filesystem inside the guest VM are automatically saved to a ./menv directory on the host machine using virtio-fs to map the host directory into the guest.

For a solo dev on Hetzner/Netcup-style infra this is the most pragmatic choice. Trade-off: development appears driven by a smaller core team, and some GitHub issues report I/O errors with virtio-fs mounting single files and problems with Unix sockets — the filesystem layer is still maturing. For agent workspaces this matters.

**4. Beam** — serverless-shaped, container-based

[github.com/beam-cloud/beta9](https://github.com/beam-cloud/beta9), AGPL-3.0. Containers start in under 1 second, scale to thousands for parallel workloads, with support for GPUs, file I/O, networking, long-running processes, and no timeouts. Container-based not VM-based, so weaker isolation but faster and simpler to operate.

Good if the agent workloads are "trusted-ish" (your own code doing LLM stuff) rather than fully untrusted user code. GPU support is a real plus if any of the OpenClaw agents need local inference.

**5. Firecracker + your own orchestrator** — the DIY path

[github.com/firecracker-microvm/firecracker](https://github.com/firecracker-microvm/firecracker), Apache 2.0, from AWS. The engine underneath E2B, Fly.io, Koyeb, etc. Plus [firecracker-containerd](https://github.com/firecracker-microvm/firecracker-containerd) for the containerd integration, or [Kata Containers](https://github.com/kata-containers/kata-containers) for an OCI-compatible VM runtime.

This is "roll your own E2B." Realistic only if the orchestration model is genuinely custom to SST — in which case existing platforms fight you, and you'd rather own the primitive. For OpenClaw's "each Sprite = workspace + exec rights + token-controlled capabilities" model, this probably *is* worth it eventually. Not in month 1.

**6. Codespaces-adjacent: Coder, Gitpod (Flex), devpod**

[Coder](https://github.com/coder/coder) (AGPL) and [devpod](https://github.com/loft-sh/devpod) (MPL-2.0) give you devcontainer-spec-based cloud dev environments you can self-host. Not designed for AI agents specifically — designed for humans with VSCode — but the underlying primitive (per-user persistent container with a workspace) is the same. Gitpod's old self-hostable version is effectively deprecated in favor of Gitpod Flex.

For OpenClaw these would feel like wearing a suit to go hiking — lots of IDE UX you don't need. Skip unless you also want human dev UX on the same platform.

**Honorable mention: Kata Containers + containerd**

If you want VM-level isolation with the Docker/K8s API surface, Kata is the grown-up answer. Doesn't give you the "agent sandbox" product — gives you the runtime primitive. Pair with a thin orchestrator you write.

---

**My actual recommendation for you, given solo-dev capacity and OpenClaw's shape:**

Look at **Microsandbox first**. It's the only option on this list that a solo dev can reasonably operate without a Kubernetes cluster, and the primitives map cleanly to what you need: a VM per session, virtio-fs backed workspace, auto-persist to host directory, libkrun-fast. Its rough edges on Unix sockets and single-file mounts are worth verifying against your specific needs, but for "agent has a Linux box with a workspace" it's closest to right.

If Microsandbox's rough edges hit you, fall back to **E2B self-hosted** (if you're OK running the Terraform on AWS/GCP) or build directly on **Firecracker + libgit2 + Postgres** for a workspace-versioning-first architecture that matches your FUSE-versioning instincts.

Skip Daytona unless you genuinely want to run a Kubernetes cluster. Its feature set is excellent but the operational surface is wrong for your situation.

One strategic observation: this space is consolidating rapidly. Daytona rebuilt and relaunched for AI agents in late April 2025 and crossed $1 million in ARR within two months, with Series A in February 2026. The "sandbox for agents" category is being commoditized by well-funded players. If OpenClaw's value is in the *orchestration* layer (SST, Sprite coordination, Token delegation) rather than the *sandbox primitive*, it's worth being honest that you probably don't want to own the primitive long-term. Use Microsandbox or E2B self-hosted, keep OpenClaw portable across sandbox backends, and let this layer commoditize under you.

---
**HUMAN** (2026-04-18T18:21):

so i use Microsandbox and mount it to my filesystem database right?

---
**ASSISTANT** (2026-04-18T18:22):

 Close, but the mental model needs one adjustment — you don't mount *to* the filesystem, you mount the user's workspace *into* each Microsandbox VM as it spins up. The direction of the relationship matters.

Here's the picture:

```
Persistent layer (always on, shared across all sessions):
├── Postgres ────────── users, sessions, metadata, refs, quotas, audit log
├── Object store ────── content-addressed blobs (Garage/MinIO/SeaweedFS)
└── Git object DB ───── optional, for versioning (libgit2 over the object store)
                         
                         ↕ (workspace materialization + commit-back)

Ephemeral layer (on-demand, per active session):
└── Microsandbox VM ─── one per active agent session
    ├── /workspace ──── materialized from Postgres + object store at boot
    ├── bash, python, git, your tools — normal Linux
    └── agent daemon ── runs commands, emits events, commits changes on exit
```

**The lifecycle of an agent session:**

1. Agent needs to start work → orchestrator asks Microsandbox to spin up a VM.
2. At VM boot, you materialize the workspace into `/workspace` — either via `git clone` from your libgit2-backed bare repo, or by listing the user's files from Postgres and pulling blobs from the object store into the VM's filesystem.
3. Agent runs commands inside the VM normally. Reads/writes hit the VM's real ext4 filesystem, fast, no FUSE overhead.
4. Microsandbox's virtio-fs *already* persists the VM's filesystem changes to a host directory (the `./menv` pattern). You're not fighting that — you're using it as the pickup point.
5. On session end, a commit-back step reads the final state from that host directory, writes new blobs to your object store, updates the metadata in Postgres, bumps the user's ref.
6. VM is destroyed. Persistent state lives on.

**Why not "mount your DB-backed filesystem into the VM directly":**

You *could* do this — mount JuiceFS or a custom FUSE layer on the host, then have Microsandbox's virtio-fs expose that mounted directory into the VM. Two reasons it's worse than materialize-then-commit:

*Performance.* Every file operation inside the VM goes: VM → virtio-fs → host FUSE → metadata DB / object store. Two layers of userspace translation per syscall. Agent workloads that do lots of small I/O (grep, git status, npm install) will be painfully slow.

*Failure modes.* If the DB or object store hiccups, the VM sees filesystem errors mid-operation. `npm install` fails halfway, leaving a corrupt `node_modules/`. With materialize-then-commit, transient failures happen at session boundaries where you can retry cleanly.

The materialize-then-commit model treats the VM's filesystem as a *working copy* — disposable, fast, local — and your DB+object store as the *source of truth*. Git's working-directory / object-store split, applied to sandboxes. This is how Codespaces works, how Gitpod works, and it's the right shape for agents too.

**Concrete architecture for OpenClaw:**

```
┌─────────────────────────────────────────────────────────────┐
│  Orchestrator (your code)                                   │
│  - Receives agent task                                      │
│  - Looks up user + ref in Postgres                          │
│  - Asks Microsandbox to create a VM                         │
│  - Runs materialize_workspace(vm, user_ref)                 │
│  - Sends commands to agent_daemon inside VM                 │
│  - On completion: commit_workspace(vm, user_ref)            │
│  - Destroys VM                                              │
└─────────────────────────────────────────────────────────────┘
         │                                           │
         │ create/destroy VMs                        │ read/write state
         ▼                                           ▼
┌────────────────────┐                    ┌─────────────────────┐
│   Microsandbox     │                    │ Postgres + ObjStore │
│  ┌──────────────┐  │                    │                     │
│  │ VM (session) │  │                    │  users              │
│  │ /workspace   │◄─┼── materialize ─────┤  refs               │
│  │   foo.py     │  │                    │  trees              │
│  │   data/      │  │                    │  blobs (by hash)    │
│  └──────┬───────┘  │                    │  audit_log          │
│         │          │                    │                     │
│         └────────── commit back ────────►                     │
└────────────────────┘                    └─────────────────────┘
```

**The materialize and commit functions are where your versioning logic lives:**

```python
def materialize_workspace(vm, user_id, ref):
    tree = db.get_tree(user_id, ref)              # Postgres lookup
    for path, blob_hash in tree.items():
        blob = object_store.get(blob_hash)        # S3/MinIO fetch
        vm.write_file(f"/workspace/{path}", blob)
    vm.run("cd /workspace && git init && git add -A && git commit -m 'base'")

def commit_workspace(vm, user_id, ref, message):
    changes = vm.run("cd /workspace && git diff --name-status HEAD").parse()
    new_tree = {}
    for path, status in changes:
        if status != 'D':
            content = vm.read_file(f"/workspace/{path}")
            blob_hash = hash_content(content)
            object_store.put(blob_hash, content)   # idempotent, dedup-friendly
            new_tree[path] = blob_hash
    db.write_tree_and_advance_ref(user_id, ref, new_tree, message)
    db.append_audit_log(user_id, ref, changes)
```

That's the whole pattern. The git-inside-VM trick is optional but convenient — it gives you free diffing at commit time rather than reimplementing file-change detection.

**For 100k users specifically:**

- Postgres handles 100k users + their refs + metadata easily. Shard later if needed.
- Object store handles the blobs, dedup is automatic (content-addressed).
- Microsandbox VMs are ephemeral — you only run them for *active* sessions, which is probably 1–5% of users at any time. 1000–5000 concurrent VMs is doable on a few beefy hosts.
- The expensive part operationally is the VM host fleet, not the storage. Storage scales linearly and cheaply; compute scales with active users.

**The part to think about next:** idle sessions. Agents often have "thinking time" between tool calls. Keeping a VM alive for a 30-minute task where it's actually executing 30 seconds is wasteful. Options: pause/snapshot VMs between tool calls (Microsandbox + libkrun supports this), or keep a warm pool of pre-booted generic VMs and only materialize the workspace on first use. This is where Daytona and E2B put a lot of engineering; it's worth knowing you'll hit this problem eventually, but not worth solving until you have real usage data.

So yes — Microsandbox sits *between* your agent orchestrator and your persistent DB+object-store, and the workspace is materialized into each VM on demand rather than permanently mounted. The DB is the source of truth, the VM is the scratch pad.

---
**HUMAN** (2026-04-18T18:26):

basically, i want a tree database that can be quickly accessed, and can also be used by microsandbox

---
**ASSISTANT** (2026-04-18T18:27):

 Got it — you want the *data model*, not just a storage backend. A tree structure that's first-class queryable from your app (list a user's folder, search by path, check permissions) AND cheap to materialize as a real filesystem inside a Microsandbox VM.

This is a well-understood design problem with a few good patterns. The right answer depends on two choices:

**Choice 1: What shape is the tree?**

*Option A — Path-as-key.* Each file is a row keyed by its full path. Simple, flat table, fast exact lookups.

```sql
CREATE TABLE files (
    user_id    UUID,
    path       TEXT,         -- '/projects/openclaw/README.md'
    blob_hash  TEXT,         -- points into object store
    size       BIGINT,
    mode       INT,          -- 0o100644 etc
    mtime      TIMESTAMPTZ,
    PRIMARY KEY (user_id, path)
);
CREATE INDEX ON files (user_id, path text_pattern_ops);  -- prefix scans
```

Listing a folder = `WHERE user_id = ? AND path LIKE '/projects/%' AND path NOT LIKE '/projects/%/%'`. Works, but "rename a directory" means updating every row under it, and deep trees get awkward.

*Option B — Adjacency list.* Each file/folder is a row with a `parent_id`. Classic.

```sql
CREATE TABLE nodes (
    id         UUID PRIMARY KEY,
    user_id    UUID,
    parent_id  UUID REFERENCES nodes(id),
    name       TEXT,          -- 'README.md', just the basename
    kind       TEXT,          -- 'file' or 'dir'
    blob_hash  TEXT,          -- null for dirs
    mode       INT,
    mtime      TIMESTAMPTZ,
    UNIQUE (parent_id, name)
);
```

Listing a folder is one indexed query by `parent_id`. Rename a directory = update one row. Full-path lookups are slower (need recursive CTE), but Postgres handles that fine.

*Option C — Git-style tree objects.* Each directory is a blob-like object listing its entries; each file is a blob. User's workspace is a single ref pointing at a root tree.

```sql
CREATE TABLE tree_objects (
    hash      TEXT PRIMARY KEY,       -- content hash of the tree
    entries   JSONB                   -- [{name, kind, hash, mode}, ...]
);
CREATE TABLE blobs (
    hash      TEXT PRIMARY KEY,       -- content hash of the file bytes
    size      BIGINT,
    storage_url TEXT                  -- s3://...
);
CREATE TABLE refs (
    user_id   UUID,
    name      TEXT,                   -- 'main', 'agent/sprite-42', etc.
    tree_hash TEXT REFERENCES tree_objects(hash),
    updated_at TIMESTAMPTZ,
    PRIMARY KEY (user_id, name)
);
```

This is literally git's data model. Every write creates new tree objects up the spine to the root, new ref. Old trees remain addressable by hash — free history, free snapshots, free branching. Listing a folder = fetch the ref's tree, then one tree_object lookup per subdirectory walked.

**Choice 2: How eagerly do you enforce the tree?**

*Eager*: every file write synchronously updates parent tree objects all the way up. Reads are cheap (one ref lookup + a few tree fetches), writes are O(depth). Git does this.

*Lazy*: writes only update the leaf record; parent trees are computed/cached on demand. Writes are O(1), reads do more work but you can cache aggressively.

---

**My recommendation for your situation, ranked:**

**Best fit: Option C (git-style trees) with lazy commits.**

Why it fits:
- Maps directly onto libgit2 / Microsandbox materialization. `materialize_workspace` becomes "walk the tree object, pull blobs into the VM." `commit_workspace` becomes "walk the VM's filesystem, write blobs, write tree objects, update ref."
- Free versioning, snapshots, branching — Spores/Sprites each get their own branch trivially.
- Content-addressed blobs dedup globally: one copy of `package.json` across 100k users.
- You can literally use a bare git repo per user (or one shared repo with per-user refs) and libgit2 for all tree operations. Postgres just stores refs + metadata you want to query (quotas, sharing, tags).
- Fast enough at scale: GitHub's entire product sits on this model.

Concrete schema (hybrid: git for trees/blobs, Postgres for the queryable metadata layer):

```sql
-- Git-shaped object store (can be actual .git/objects/ on disk,
-- or in Postgres, or in S3 — doesn't matter for the model)
CREATE TABLE git_objects (
    hash       TEXT PRIMARY KEY,        -- sha-256 (or sha-1 if you want real git compat)
    kind       TEXT,                    -- 'blob' | 'tree' | 'commit'
    size       BIGINT,
    storage    TEXT                     -- 's3://bucket/key' or inline for small objects
);

-- Per-user workspace pointer(s)
CREATE TABLE refs (
    user_id    UUID,
    name       TEXT,                    -- 'main', 'agent/sprite-42'
    commit_hash TEXT,
    updated_at TIMESTAMPTZ DEFAULT now(),
    PRIMARY KEY (user_id, name)
);

-- Queryable metadata layer — materialized views of current ref state
-- Rebuilt from the tree on commit; fast to query without walking git objects
CREATE TABLE current_files (
    user_id    UUID,
    path       TEXT,
    blob_hash  TEXT,
    size       BIGINT,
    mode       INT,
    mtime      TIMESTAMPTZ,
    PRIMARY KEY (user_id, path)
);
CREATE INDEX ON current_files (user_id, path text_pattern_ops);
CREATE INDEX ON current_files (blob_hash);          -- "who has this file?"

-- Quotas, sharing, tags, audit — normal relational stuff
CREATE TABLE users (id UUID PRIMARY KEY, quota_bytes BIGINT, ...);
CREATE TABLE shares (from_user UUID, to_user UUID, path TEXT, perm TEXT);
CREATE TABLE audit_log (user_id UUID, op TEXT, path TEXT, at TIMESTAMPTZ);
```

The `current_files` table is the "queryable projection" — kept in sync with the ref by a trigger or application code on every commit. You query this for the UI, search, listing, quotas. You use git objects for materialization into VMs and for history.

**Materialize into Microsandbox:**

```python
def materialize(vm, user_id, ref_name='main'):
    commit_hash = db.get_ref(user_id, ref_name)
    tree_hash = git.read_commit(commit_hash).tree
    walk_tree_into_vm(vm, tree_hash, target='/workspace')

def walk_tree_into_vm(vm, tree_hash, target):
    tree = git.read_tree(tree_hash)  # JSONB entries
    for entry in tree.entries:
        if entry.kind == 'blob':
            vm.write_file(f"{target}/{entry.name}", 
                          git.read_blob(entry.hash), mode=entry.mode)
        elif entry.kind == 'tree':
            vm.mkdir(f"{target}/{entry.name}")
            walk_tree_into_vm(vm, entry.hash, f"{target}/{entry.name}")
```

For large workspaces, stream blobs lazily (only materialize on first access) — this is where a thin FUSE layer inside the VM becomes worth it, but it's an optimization for later.

**Commit back:**

```python
def commit(vm, user_id, ref_name='main', msg='agent work'):
    tree_hash = build_tree_from_vm(vm, '/workspace')  # recursive
    parent = db.get_ref(user_id, ref_name)
    commit_hash = git.write_commit(tree=tree_hash, parent=parent, message=msg)
    db.update_ref(user_id, ref_name, commit_hash)
    rebuild_current_files_table(user_id, tree_hash)    # refresh query layer
    db.append_audit_log(user_id, 'commit', tree_hash)
```

**Why this beats a pure relational tree:**

At 100k users with 10k files each = 1B file rows. Doable in Postgres but painful. With git-shaped storage, you have maybe 1B blobs (heavily dedup'd to perhaps 100M unique) + 100k refs + tree objects proportional to directory count. Most reads hit a handful of tree objects, not scan a billion-row table. Snapshots/history cost nothing extra. Branch = one ref row.

**Why this beats using git CLI or raw libgit2 alone:**

Pure git is great for the tree/blob storage but bad at relational queries ("show me all files larger than 10MB across all of user X's branches," "who has files matching this hash," "paginated search by tag"). Postgres `current_files` gives you those queries in single-digit ms.

---

**Pragmatic starting point:**

1. **Object store (MinIO/Garage/S3):** raw blobs, keyed by hash.
2. **Postgres:** `refs`, `tree_objects` (as JSONB), `current_files` (projection), plus users/quotas/sharing.
3. **libgit2** (Rust `git2` or JS `isomorphic-git`): for walking/building trees programmatically.
4. **Microsandbox:** materialize via `walk_tree_into_vm` at session start, commit via `build_tree_from_vm` at end.

You can skip the actual git format if you want — the model is the valuable part, not git's wire format. Store tree objects as Postgres JSONB rows keyed by their content hash; you get the same semantics without needing libgit2. The payoff from git compat is that users can `git clone` their workspace from the command line, which is a nice property but not essential.

**The core insight:** a "tree database" for your use case is really three things composed: (1) content-addressed blobs (object store, key = hash), (2) immutable tree objects that reference blobs and other trees by hash (Postgres JSONB works fine), (3) mutable refs that name a current tree for each user/branch. That's it. Everything else — fast listing, versioning, sharing, materialization into VMs — falls out of those three primitives.
