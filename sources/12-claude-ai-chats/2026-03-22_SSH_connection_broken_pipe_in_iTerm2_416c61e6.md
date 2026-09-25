# SSH connection broken pipe in iTerm2

created: 2026-03-22T09:10:05.738988Z  uuid: 416c61e6-0d5f-40eb-892f-bef90879482a  export: old
messages: 4  total_chars: 2889  human_chars: 635

summary: **Conversation Overview**

The person sought help troubleshooting a recurring iTerm2 terminal issue where SSH connection drops (broken pipe errors) cause buffered terminal escape sequences to be dumped into the shell, rendering the terminal unusable with garbled commands. Claude explained the root cause and offered a two-part solution: preventing disconnects via `~/.ssh/config` keepalive settings (`ServerAliveInterval 60`, `ServerAliveCountMax 3`, `TCPKeepAlive yes`), and recovering a broken terminal using the `reset` command or iTerm2's built-in reset options.

The person followed up clarifying that the terminal was already in a broken state and typing `reset` was not possible. Claude then provided immediate recovery options specific to iTerm2: using `Cmd + K` to clear and partially reset, accessing Edit → "Reset Terminal" from the menu, or simply closing the broken tab with `Cmd + W` and opening a fresh one. Claude also recommended switching to `mosh` as a longer-term solution given its resilience to connection drops and network roaming, with specific install and usage commands provided for both the remote Ubuntu server and local Mac.


---
**HUMAN** (2026-03-22T09:10):

using iterm2, everytime ssh break, i got this, and it breaks terminal
client_loop: send disconnect: Broken pipe
~ on ☁️  renyongxu@gmail.com took 2d1h51m37s
❯ ssh -i ~/.ssh/bonfire1.pem ubuntu@3.26.243.133:3:3Du;1:3uu;1:3u9;5u9;5:3u9;5u9;5:3u9;5u9;5:3u0;5u0;5:3u0;5u0;5:3u0;5u0;5:3uu;1:3uu;1:3uA

---
**ASSISTANT** (2026-03-22T09:10):

The user is experiencing a common issue where after an SSH connection breaks (broken pipe), garbage characters get dumped into the terminal, which then gets interpreted as a new command. The garbled text after the SSH command is actually terminal escape sequences that were buffered and got dumped when the connection died.

This is a well-known iTerm2/terminal issue. Let me give practical solutions.This is a classic issue — when SSH dies, buffered terminal escape sequences get dumped into your shell and interpreted as garbage input (those `:3Du;1:3uu;` strings are corrupted escape codes). Two things to fix:

**1. Keep SSH alive (prevent the break)**

Add this to `~/.ssh/config`:

```
Host *
    ServerAliveInterval 60
    ServerAliveCountMax 3
    TCPKeepAlive yes
```

This sends a keepalive ping every 60 seconds so idle connections don't get killed by NATs/firewalls.

**2. Fix your terminal after it breaks**

When it happens, just type `reset` and hit Enter (even if you can't see what you're typing — the terminal is in a broken state but still accepting input). This resets the terminal emulator state.

You can also hit `Ctrl+C` first to cancel whatever garbage command got pasted, then type `reset`.

**3. Use `mosh` instead of `ssh`**

Since you're nomadic and on variable connections, `mosh` is a much better fit — it handles disconnects, roaming, and high-latency gracefully:

```bash
# on your EC2 instance
sudo apt install mosh

# from your Mac
brew install mosh
mosh --ssh="ssh -i ~/.ssh/bonfire1.pem" ubuntu@3.26.243.133
```

`mosh` uses UDP and reconnects automatically — no more broken pipes, no more garbled terminals. It's especially good when switching between WiFi networks or working from cafés in Da Nang/Chiang Mai.

---
**HUMAN** (2026-03-22T09:11):

but the current session is broken, and i can't type reset
~ on ☁️  renyongxu@gmail.com
❯ r4;1:3ue1;1:3us5;1:3ue3;1:3u1;1:3ut6;1:3u
zsh: command not found: r4
zsh: command not found: 1:3ue1
zsh: command not found: 1:3us5
zsh: command not found: 1:3ue3
zsh: command not found: 1:3u1
zsh: command not found: 1:3ut6
zsh: command not found: 1:3u

---
**ASSISTANT** (2026-03-22T09:11):

The user's terminal is currently broken and they can't type properly. Let me give them immediate fixes.Try these in order:

1. **`Cmd + K`** — clears the iTerm2 screen and resets some state

2. **Open iTerm2 menu → Edit → "Reset Terminal"** (or `Cmd + Shift + R` if that binding exists)

3. If you can't type at all, just **close that tab** (`Cmd + W`) and open a new one (`Cmd + T`)

That's it — don't fight a broken terminal session, just kill the tab and open fresh. Your shell state isn't worth saving.
