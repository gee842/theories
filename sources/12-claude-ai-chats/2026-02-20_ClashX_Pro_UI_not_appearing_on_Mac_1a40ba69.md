# ClashX Pro UI not appearing on Mac

created: 2026-02-20T15:02:14.153585Z  uuid: 1a40ba69-7f26-4932-8ea9-22bf60e54f05  export: old
messages: 12  total_chars: 8156  human_chars: 605

summary: **Conversation Overview**

The user encountered a technical issue with ClashX Pro on Mac where the process was running but the UI wasn't accessible - no menu bar icon appeared and the dashboard wouldn't load. Through systematic troubleshooting, Claude helped diagnose that the app's core functionality was working properly but the native macOS UI components were failing, likely due to compatibility issues with newer macOS versions since ClashX Pro is no longer maintained. The key breakthrough came when running the app from Terminal revealed the API was listening on port 54455 instead of the default 9090, allowing access to the web dashboard at http://127.0.0.1:54455/ui.

Since the menu bar interface remained broken, Claude recommended migrating to Clash Verge Rev, an actively maintained alternative that uses the same configuration format. The user successfully installed Clash Verge Rev via Homebrew and needed guidance on importing their existing YAML configuration file. Claude provided specific instructions for loading the config through the Profiles section, including both drag-and-drop methods and manual file placement options. The troubleshooting process demonstrated the user's comfort with Terminal commands and technical problem-solving, working through multiple diagnostic steps including process management, port checking, and configuration file manipulation.


---
**HUMAN** (2026-02-20T15:02):

I installed clash x pro on my Mac but can’t open the ui, nothing shows up but I can see the process running

---
**ASSISTANT** (2026-02-20T15:02):

The user is having trouble with ClashX Pro on Mac - the UI won't show but the process is running. This is a technical support question I can answer from knowledge.This is a common issue with ClashX Pro on Mac. Here are a few things to try:

**Check the menu bar.** ClashX Pro runs as a menu bar app, not a regular window app. Look for a small icon (usually a cat or diamond shape) in your Mac's top menu bar, possibly hidden behind the notch on newer MacBooks. Click the arrow (‣) on the right side of the menu bar to reveal hidden icons.

**Try these fixes in order:**

1. **Right-click the menu bar icon** → Select "Dashboard" or "Open UI" to launch the web-based control panel.

2. **Access the dashboard directly** in your browser at `http://127.0.0.1:9090/ui` (the default address). If that doesn't work, try `http://localhost:9090/ui`.

3. **Check if the port is correct** — open Terminal and run:
   ```
   cat ~/.config/clash/config.yaml | grep external-controller
   ```
   This will show you the actual port the API is listening on.

4. **Reset the app** — quit ClashX Pro completely (right-click menu bar icon → Quit), then delete the config folder and restart:
   ```
   rm -rf ~/.config/clash
   ```
   Then reopen ClashX Pro and it will regenerate default configs.

5. **macOS permissions** — Go to System Settings → Privacy & Security → check that ClashX Pro has the necessary permissions (Network Extensions, etc.). On newer macOS versions, you may need to explicitly allow it.

6. **Reinstall** — if nothing works, uninstall fully (including the `~/.config/clash` folder), redownload from the official source, and reinstall.

Which of these have you already tried? That'll help me narrow down the issue.

---
**HUMAN** (2026-02-20T15:05):

No icon, tried 2,3,4 not working

---
**ASSISTANT** (2026-02-20T15:05):

The user has ClashX Pro running as a process but no menu bar icon and the dashboard isn't accessible. Let me think about what could cause this.

Key possibilities:
- The app might be blocked by macOS security (Gatekeeper)
- The process might be a zombie/stuck process
- Could be an Apple Silicon vs Intel compatibility issue
- The config might have an error preventing proper startup
- macOS version compatibility issue

Let me give practical troubleshooting steps.Since the process is running but there's no menu bar icon and no dashboard, the app is likely crashing silently or being blocked by macOS. Try these:

**1. Kill the existing process first:**
```bash
killall ClashX\ Pro
# or if that doesn't work:
ps aux | grep -i clash
# then kill the PID:
kill -9 <PID>
```

**2. Check if macOS is blocking it.** Open the app again and immediately check System Settings → Privacy & Security. There may be a message at the bottom saying "ClashX Pro was blocked from opening." Click **"Open Anyway."**

**3. Try launching from Terminal** to see error output:
```bash
/Applications/ClashX\ Pro.app/Contents/MacOS/ClashX\ Pro
```
This should print any crash or error messages — share what you see and I can help diagnose further.

**4. Check your macOS version and chip.** If you're on Apple Silicon (M1/M2/M3/M4), make sure you downloaded the ARM version. If you're on an older Intel Mac, you need the x86 version. Running the wrong architecture can cause silent failures.

**5. Try the open-source alternative.** ClashX Pro has been discontinued by its developer. If you can't get it working, consider switching to one of these actively maintained alternatives:
- **Clash Verge Rev** — modern UI, actively maintained
- **Stash** (paid, on the App Store) — polished Mac client
- **mihomo Party** — free, based on the mihomo (formerly Clash.Meta) core

The Terminal output from step 3 will be the most useful — what does it show?

---
**HUMAN** (2026-02-20T15:07):

❯ /Applications/ClashX\ Pro.app/Contents/MacOS/ClashX\ Pro

23:06:47 INF check port success port=7890
23:06:47 INF inbound create success inbound=mixed addr=127.0.0.1:7890 network=tcp
23:06:47 INF inbound create success inbound=mixed addr=127.0.0.1:7890 network=udp
23:06:47 INF [API] listening addr=127.0.0.1:54455

---
**ASSISTANT** (2026-02-20T15:07):

The API is listening on port 54455, not the default 9090. That's why the dashboard wasn't loading.There it is — the API is on port **54455**, not the default 9090. That's why the dashboard wasn't loading.

Try opening this in your browser:

```
http://127.0.0.1:54455/ui
```

If that shows a blank page or 404, try the external dashboard:

```
http://clash.razord.top/#/proxies?host=127.0.0.1&port=54455
```

or

```
http://yacd.haishan.me/#/proxies?hostname=127.0.0.1&port=54455
```

As for the missing menu bar icon — since the core is running fine but the macOS UI isn't rendering, this is likely a compatibility issue with your macOS version. Since ClashX Pro is discontinued, I'd recommend switching to **Clash Verge Rev** or **mihomo Party** — they use the same config format and subscription links, so migration is painless.

---
**HUMAN** (2026-02-20T15:08):

http://127.0.0.1:54455/ui
Does work, but no icon or anything else

---
**ASSISTANT** (2026-02-20T15:08):

The core works fine but the macOS menu bar UI doesn't render. This is a known issue with discontinued ClashX Pro on newer macOS versions. The app's UI framework is likely incompatible.

Since the core is functional, the user has two options: live with the web UI only, or switch to a maintained client.Good — so the core is healthy, it's just the native macOS menu bar UI that's broken. This is a known issue with ClashX Pro on newer macOS versions (especially Ventura/Sonoma/Sequoia) since the app is no longer maintained.

You have two options:

**Option A: Live with it.** Bookmark `http://127.0.0.1:54455/ui` and manage everything from the web dashboard. The proxy itself works fine — just set your system proxy to `127.0.0.1:7890` (SOCKS5 and HTTP) manually in System Settings → Network → Wi-Fi → Proxies, since there's no menu bar toggle to do it for you.

**Option B: Switch to a maintained app (recommended).** Your existing subscription links and configs will work directly. The easiest migrations:

- **Clash Verge Rev** — free, open source, very similar to ClashX Pro. Install via `brew install --cask clash-verge-rev`
- **mihomo Party** — free, clean UI, also brew-installable
- **Stash** — paid but polished, available on the Mac App Store

I'd go with Option B since you'll keep running into issues with a dead project. Clash Verge Rev is probably the closest experience to what you're used to.

---
**HUMAN** (2026-02-20T15:10):

Can you help me find Clash Verge Rev

---
**ASSISTANT** (2026-02-20T15:10):

The user wants to find Clash Verge Rev. Let me search for it.
```
This block is not supported on your current device yet.
```

Got the info needed.Here you go — two easy ways to get it:

**Easiest: Homebrew**
```bash
brew install --cask clash-verge-rev
```

**Manual download:**
Go to the GitHub releases page: [github.com/clash-verge-rev/clash-verge-rev/releases](https://github.com/clash-verge-rev/clash-verge-rev/releases)

The latest version is **v2.4.5**. Download the `.dmg` file matching your chip:
- **Apple Silicon** (M1/M2/M3/M4): the `aarch64.dmg` file
- **Intel Mac**: the `x64.dmg` file

Once installed, your existing subscription URLs from ClashX Pro will import directly — just paste them into Profiles. Then you can kill the old ClashX Pro process and you're good to go.

---
**HUMAN** (2026-02-20T15:15):

Ok installed, I have a yaml file, how do I load it

---
**ASSISTANT** (2026-02-20T15:15):

The user has installed Clash Verge Rev and wants to load a YAML config file.In Clash Verge Rev:

1. Open the app → go to **Profiles** (in the left sidebar)
2. There should be a "New" or import button at the top — look for a **file icon** or drag-and-drop area
3. You can either:
   - **Drag your .yaml file** directly into the Profiles area
   - Click the **import** button and select your file
   - Or use "Local File" option to browse to it

Once imported, **click on the profile card** to activate it (it should highlight), then the proxy groups and rules from your YAML will load automatically.

If you can't find the import option, you can also manually copy your YAML file to the config directory:

```bash
# Check where Clash Verge Rev stores configs:
ls ~/Library/Application\ Support/io.github.clash-verge-rev.clash-verge-rev/
```

Let me know if you get stuck on any step.
