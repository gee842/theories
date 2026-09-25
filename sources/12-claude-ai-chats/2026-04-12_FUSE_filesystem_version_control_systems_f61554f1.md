# FUSE filesystem version control systems

created: 2026-04-12T17:34:00.762396Z  uuid: f61554f1-635d-4555-853c-5e028b5e6811  export: new
messages: 8  total_chars: 10826  human_chars: 251

summary: **Conversation Overview**

The person engaged in a technical exploration of versioned and snapshotting filesystems, starting with an interest in FUSE-based "Time Machine"-like implementations that track file changes similarly to git or a blockchain. Claude provided a landscape overview of relevant technologies including gitfs, ZFS/Btrfs snapshots, NILFS2, Perkeep, IPFS, and Hypercore, explaining how each relates to the concept of immutable, hash-verified file history.

The conversation progressed through several focused sub-questions. The person asked about extensibility options for gitfs, and Claude explained that while gitfs has no formal plugin system, changes can be intercepted via git hooks on the underlying repo, inotify/fswatch on the mount point, remote git polling, or by forking the Python source. Claude noted gitfs uses a commit queue and sync worker architecture and is small enough to modify easily. The person then asked about using git itself as a Time Machine replacement, and Claude provided a practical overhead comparison covering storage efficiency, snapshot speed, CPU cost, and binary file handling — concluding that git works well for text/code but degrades significantly for large binaries or whole-home-directory tracking, recommending restic or BorgBackup for broader use cases.

Finally, the person asked specifically about FUSE-mountable Time Machine tools. Claude recommended restic as the top practical choice due to its single Go binary, cross-platform support, FUSE mount capability for browsing snapshots as a live directory, content-addressed deduplication, and support for remote backends like S3 and SFTP. BorgBackup was presented as a close alternative with similar FUSE browsing. ESFS was noted as a purpose-built FUSE versioning filesystem for real-time copy-on-write snapshotting. Claude drew a distinction between backup tools with FUSE read access (restic, Borg) versus live FUSE filesystems that version every write in real-time (ESFS or a custom layer), and closed by asking whether real-time versioning or periodic snapshots was the actual requirement.


---
**HUMAN** (2026-04-12T17:34):

Is there a fuse time machine like implementations? Like git, track every file changes like a block chain

---
**ASSISTANT** (2026-04-12T17:34):

The user is asking about FUSE-based time machine implementations that track file changes like git or blockchain - essentially versioned filesystems.Yes, there are several projects in this space! Here's what exists:

**FUSE-based versioned filesystems:**

- **gitfs** — Mounts a git repo as a FUSE filesystem. Every write automatically commits, so you get full git history of all file changes. Closest to what you're describing.

- **ZFS / Btrfs snapshots** — Not FUSE, but kernel-level filesystems with copy-on-write semantics. You can take snapshots at any point and roll back. ZFS in particular has `zfs diff` to see exactly what changed between snapshots.

- **NILFS2** — A Linux filesystem that's continuously snapshotting (log-structured). Every state of every file is preserved until you run garbage collection. Built into the kernel, not FUSE.

**More experimental / blockchain-adjacent:**

- **CAS (Content-Addressable Storage) filesystems** — Like how git stores objects by SHA hash. Projects like **Perkeep** (formerly Camlistore) store all file versions as content-addressed blobs, giving you immutable, deduplicated history.

- **IPFS + FUSE** — IPFS is content-addressed (every version of a file has a unique CID). It has a FUSE mount. Combined with MFS (Mutable File System), you get something like what you're describing — though you'd need tooling on top to auto-snapshot.

- **Datproject / Hypercore** — Append-only log structure (like a blockchain) for file changes. Merkle-tree verified history.

**The "holy grail" combo you're describing** — FUSE mount + automatic change tracking + Merkle/hash-chain integrity — doesn't exist as one polished product. The closest practical setup would be:

1. **gitfs** for the git-style auto-versioning
2. **Perkeep** for the content-addressed immutable storage
3. **ZFS** if you want battle-tested snapshots at the OS level

Would you like to dig deeper into any of these, or are you thinking about building something in this space?

---
**HUMAN** (2026-04-12T17:36):

Can I add plugins to gitfs? Or listen to changes

---
**ASSISTANT** (2026-04-12T17:36):

The user is asking about gitfs extensibility - whether it supports plugins or change listening hooks. Let me search for current info on this.
```
This block is not supported on your current device yet.
```

gitfs (presslabs) doesn't have a plugin system. But I can explain the architecture and how you could hook into changes. Let me think about practical approaches.

The presslabs gitfs uses a commit queue and sync worker architecture. It doesn't have a formal plugin API. But there are several ways to listen to changes:

1. Git hooks (post-commit, post-receive) on the underlying repo
2. inotify/fswatch on the mounted filesystem
3. Fork gitfs and modify the Python code (it's Apache 2.0)
4. Use git hooks on the remote

Given Ren's context - building agent infrastructure, OpenClaw - this question might be about building a versioned filesystem layer for agent state or coordination. 

For your use case, I'd recommend starting with git hooks since they're the least invasive and work directly with gitfs's commit queue. You could trigger custom logic whenever changes are committed, which would let you integrate with your agent coordination layer without modifying gitfs itself.Short answer: **gitfs (presslabs) has no plugin system**. But there are practical ways to hook into changes:

**Git hooks on the underlying repo**
Since gitfs commits to a real git repo (cached locally at `repo_path`), you can drop standard git hooks into that repo's `.git/hooks/` directory — `post-commit`, `pre-commit`, etc. Every auto-commit gitfs makes will trigger them.

**inotify / fswatch on the mount point**
Watch the mounted directory with `inotifywait` or `fswatch`. You get real-time file-level change events before gitfs even commits them. This is the lightest-weight approach.

```bash
inotifywait -m -r /mount/point -e modify,create,delete
```

**Git polling on the remote**
If multiple nodes are involved, watch the remote repo with a cron or webhook — GitHub/Gitea webhooks fire on every push gitfs makes.

**Fork the Python source**
The architecture uses a commit queue consumed by a sync worker that batches changes based on a configurable timeout. It's Python + fusepy + pygit2, Apache 2.0 licensed. You could inject your own callback at the commit queue level pretty easily — the codebase is small.

**The more interesting question though** — if you're thinking about this for agent state or coordination (OpenClaw-adjacent), you might want to skip gitfs entirely and go lower:

- **Write your own thin FUSE layer** in Python (fusepy) or Rust (fuser) that intercepts writes and emits events to whatever bus you want — Redis streams, a Hypercore append-only log, or your own SST token emission
- **Watchman** (Facebook's file watcher) is more robust than inotify for high-throughput change detection and has a subscription API

What's the use case you're circling? Agent workspace versioning, or something more like an auditable state log?

---
**HUMAN** (2026-04-12T17:59):

Can I use git as my Time Machine? How much overhead

---
**ASSISTANT** (2026-04-12T17:59):

The user is asking about using git as a full Time Machine replacement - tracking all file changes on their system. Let me think about the practical overhead and feasibility.Great question. You *can*, but the overhead profile is very different from Time Machine. Here's the real breakdown:

**Where git works well as backup/versioning:**
- Text files, config files, code, notes, documents — great. Delta compression is extremely efficient, often 90%+ space savings.
- Small binary files — acceptable.

**Where it falls apart:**

- **Large binary files** (images, videos, databases, .psd, .zip) — git stores a full copy of every version. A 1GB video edited 5 times = 5GB in `.git/`. Time Machine uses block-level dedup and hard links, so it only stores the changed blocks.
- **The `.git` directory grows forever** — and `git gc` helps but can't fix the fundamental problem with binaries. A few months of tracking a home directory could balloon to hundreds of GB.
- **Commit overhead** — each auto-commit needs to SHA-hash every changed file. For a working directory with tens of thousands of files, `git status` alone can take seconds. Time Machine operates at the filesystem/block level, which is far cheaper.

**Rough overhead comparison:**

| | Time Machine (APFS snapshots) | git |
|---|---|---|
| Snapshot speed | ~instant (CoW) | Seconds to minutes |
| Storage for text | ~same | ~same (excellent) |
| Storage for binaries | Block-level dedup | Full copy per version |
| 100GB working dir | Works fine | `git status` chokes |
| CPU per snapshot | Near zero | Hashes everything |

**If you still want git-based Time Machine, the practical setup is:**

1. **git + git-lfs** for large files (offloads binaries to separate storage)
2. **Limit scope** — track `~/Documents`, `~/code`, `~/.config`, not your entire home dir
3. **Exclude** `.cache`, `node_modules`, build artifacts, media libraries
4. **Auto-commit on a timer** (every 5-15 min) rather than per-write

**Better alternatives for the full "Time Machine but git-like" experience:**

- **Btrfs/ZFS snapshots** — copy-on-write, instant, block-level, near zero overhead. Closest to what you actually want.
- **restic** or **borg** — deduplicating backup tools that feel like git (content-addressed, append-only) but are designed for arbitrary files, not just code.

The honest answer: git is a *source code* tool being asked to be a *filesystem* tool. For your code and text? Perfect. For everything? Use ZFS snapshots or restic. What's the actual scope you're thinking about?

---
**HUMAN** (2026-04-12T18:01):

Are there good time machine I can use with fuse?

---
**ASSISTANT** (2026-04-12T18:01):

The user wants a FUSE-based time machine - a filesystem they can mount that gives them versioning/snapshot capabilities. Let me search for this.
```
This block is not supported on your current device yet.
```

Good results. Let me also search for some more modern options like restic FUSE mount, borg mount, etc.
```
This block is not supported on your current device yet.
```

Good, now I have a clear picture. Let me summarize the best FUSE-mountable time machine options.Here are the best options, ranked by practicality:

**Tier 1: Battle-tested, FUSE-mountable**

**BorgBackup** — probably the closest thing to what you want. Borg's FUSE mounting lets you browse backups like a filesystem. Run `borg mount /repo /mnt` and you get a browsable filesystem of every backup. Need one config file from last Tuesday? Navigate to it and copy it out. It does content-defined chunking (dedup), zstd compression, AES-256 encryption, and handles binaries well.

**restic** — similar to Borg but written in Go (single binary, no dependencies). You can mount a repository via FUSE and browse the contents of snapshots directly without having to restore them first. Snapshots show up as directories organized by date, host, and tags. Supports S3, SFTP, and many cloud backends natively — useful if you're bouncing between Shenzhen and Southeast Asia.

**Tier 2: Purpose-built FUSE versioning filesystems**

**ESFS** — a FUSE-based snapshotting filesystem that uses copy-on-write to save blocks of old data before they are overwritten, only saving a block once when modified for the first time after a snapshot. You create snapshots with `mkdir /mount/snapshots/Monday` and browse old versions at that path. Lightweight, but less mature.

**CopyFS** — a versioning filesystem for FUSE where you can check revision history of a file and revert to older versions. Old project (2004), simple but hasn't been maintained.

**Tier 3: DIY**

**vaves** (via fsfipi) — a filter framework supporting a cascade of filters which modify filesystem behavior, including a configurable versioning filesystem. Academic-flavored but interesting architecture.

**My recommendation for your setup:**

**restic** is probably your best bet because:
- Single Go binary — works on your Android edge nodes, Linux VPS, macOS, everywhere
- Backs up to S3/SFTP/local — you can point it at your Singapore VPS
- FUSE mount to browse any snapshot as a normal directory
- Content-addressed dedup handles mixed text+binary well
- Cron it every 15 min and you have a Time Machine

```bash
# backup
restic -r sftp:user@sg-vps:/backups backup ~/projects

# browse any snapshot as a filesystem
restic -r sftp:user@sg-vps:/backups mount /mnt/timemachine
# then: ls /mnt/timemachine/snapshots/2026-04-13T10:30:00/
```

The key difference from what you were originally asking though: Borg/restic are **backup tools with FUSE read access**, not **live FUSE filesystems that version every write in real-time**. For the latter, ESFS or writing your own thin FUSE layer is the path. Is real-time versioning the requirement, or is periodic snapshots sufficient?
