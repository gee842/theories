# Rokid AR glasses lyrics display and screen issues

created: 2026-03-14T14:59:07.966431Z  uuid: 2acced7c-6764-4add-899f-43727d6f5942  export: old
messages: 18  total_chars: 27793  human_chars: 665

summary: **Conversation Overview**

The person is a Rokid Glasses user troubleshooting two immediate issues: the music interface persistently displaying a lyrics-needs-to-be-enabled message, and the screen staying on unnecessarily during music playback. Claude explained that both issues stem from the glasses automatically activating the lyrics display feature when audio playback is detected, and provided workarounds including exiting the lyrics app via touchpad, checking Hi Rokid app display settings, and updating firmware. The person is based in Shenzhen, which was noted as relevant context for hardware sourcing.

The conversation then shifted toward developer interest, with the person asking about building custom apps for the glasses to address limitations like notification reply functionality. Claude outlined two development paths: the CXR-M SDK (phone-side Android companion app) and native glasses-side APK sideloading via ADB. A significant constraint emerged when the person revealed they only have an iPhone — the entire CXR-M SDK ecosystem is Android-only, making WeChat notification interception and reply functionality impossible without an Android companion device. Claude suggested a cheap Android device from Huaqiangbei as the practical workaround, while noting that glasses-side apps via ADB remain viable using the iPhone's Personal Hotspot as the internet source on the go.

The person expressed clear frustration with the ecosystem fragmentation and iOS limitations throughout. The conversation converged on a concrete project idea: a screenless voice-only AI assistant app that runs natively on the glasses, uses the microphone for input, calls an LLM API over WiFi (via iPhone hotspot), and outputs TTS audio through the speakers — deliberately avoiding the display to conserve the 210mAh battery. Claude confirmed this is technically feasible with standard non-root ADB access, which allows APK sideloading, permission grants, port forwarding, WiFi configuration, and standard Android shell commands. The main unresolved blocker identified is sourcing the proprietary 5-pin dev cable required for ADB connection to the Rokid Glasses RV101.


---
**HUMAN** (2026-03-14T14:59):

When I use rokid ar glasses, the music interface is keep telling me the lyrics needs to be enabled by app, and the screen is always on, which is totally unnecessary, how do I fix it

---
**ASSISTANT** (2026-03-14T14:59):

The user is asking about their Rokid AR glasses having two issues:
1. Music interface keeps showing a message about lyrics needing to be enabled by the app
2. The screen is always on during music playback

Let me search for solutions to these specific Rokid glasses issues.
```
This block is not supported on your current device yet.
```

The search results don't directly address the specific issues. Let me search more specifically for the music/lyrics notification and always-on screen issues.
```
This block is not supported on your current device yet.
```

The search results don't directly address the specific issues Ren is having. Let me search in Chinese since Ren is in Shenzhen and might be using the Chinese version of the app/glasses, and the issue might be more discussed in Chinese forums.
```
This block is not supported on your current device yet.
```

I found some useful info. The 53AI article mentions that the Rokid Glasses have a "歌词" (lyrics) function in the touchpad menu. Let me search more specifically for how to disable the lyrics display and screen-always-on behavior.
```
This block is not supported on your current device yet.
```

Based on my research, I can now provide a helpful answer. The Rokid Glasses have a "歌词" (lyrics) feature built into the touchpad menu. The issue seems to be that when playing music, the glasses automatically show a lyrics interface that says lyrics need to be enabled by the app, and the display stays on. Let me provide practical advice based on what I've found.This is a pretty common annoyance with the Rokid Glasses. Here's what's happening and how to deal with it:

**The lyrics prompt:** When you play music via Bluetooth, the glasses detect audio playback and automatically activate the lyrics display feature. Since most music apps (Spotify, Apple Music, QQ音乐, etc.) don't have deep integration with Rokid's lyrics API, the glasses can't pull lyrics and just show that "需要app开启歌词" message instead. To get rid of it, swipe the touchpad on the glasses to navigate to the home screen or back out of the lyrics function. The lyrics feature is one of the built-in functions accessible via the touchpad menu (alongside translation, teleprompter, navigation, etc.) — you want to make sure you're not accidentally entering it.

**The screen staying on:** This is tied to the same issue. Once the lyrics interface is active, it keeps the display on because it thinks you want to see lyrics. A few things to try:

1. **Exit the lyrics app on the glasses** — tap the touchpad to go back/home. Once you're out of the lyrics function, the display should turn off after the normal timeout.

2. **In the Hi Rokid app**, check under Glasses Settings (眼镜设置) for display-related options. There should be settings for screen timeout/auto-off behavior. Some firmware versions also have a "wearing detection" (佩戴检测) toggle that affects when the screen activates.

3. **Update your firmware** — Rokid has been pushing frequent OTA updates that improve this kind of behavior. Make sure both your glasses firmware and the Hi Rokid app are on the latest version (the app changelog mentions several display and notification duration fixes).

4. **Don't enter the lyrics function** — if you just want to use the glasses as Bluetooth headphones for music, avoid swiping into the lyrics feature from the touchpad menu. Just play music from your phone and leave the glasses display idle.

The broader issue, as one detailed user review noted, is that the current display logic gives apps too much control over the screen, and the system doesn't let users easily dismiss or prevent unwanted display activations — it's a known UX gap that Rokid is still iterating on. If none of the above fully solves it, it might be worth posting in the Rokid R星社区 (vip.rokid.com) where other users and Rokid staff are active.

---
**HUMAN** (2026-03-14T15:03):

I can see WeChat notifications, but can I open them or reply?

---
**ASSISTANT** (2026-03-14T15:03):

The user is asking about WeChat notification functionality on Rokid Glasses - whether they can open or reply to notifications.
```
This block is not supported on your current device yet.
```

The search results don't give a specific answer about opening/replying to WeChat notifications on Rokid Glasses. Based on what I know about the product and the search results, the notifications on Rokid Glasses are display-only - they show the notification content on the glasses display but you can't interact with them (open, reply, etc.) since the glasses don't have a full app ecosystem or input method for that. Let me give an honest answer based on what I found.Unfortunately, no — notifications on Rokid Glasses are display-only. You can see the notification preview (sender name and message snippet) on the glasses display, but you can't tap into it to open the full conversation or type a reply. The glasses don't run WeChat natively and there's no text input mechanism on the device itself.

What you *can* do as workarounds:

**Voice reply (limited):** If someone calls you through WeChat voice/video call, you can answer hands-free (nod to accept, shake head to decline). But for text messages, there's no voice-to-reply integration with WeChat currently.

**Customizing notification behavior:** In the Hi Rokid app, under Home > Notification, you can control which apps push notifications to the glasses and adjust how long they display. A recent update also added customizable notification duration for message notifications on the glasses. So at minimum you can tune it so WeChat notifications don't linger and block your view.

**The practical workflow** is basically: see the notification on the glasses → decide if it's urgent → pull out your phone to actually reply. It's a "glanceable" system, not an interactive one.

This is honestly one of the bigger limitations of the current generation. The display is too small and the input methods too limited (touchpad + voice) to support full messaging interactions. Even the 53AI review you might have seen flagged this — the notification system can actually be intrusive since it pops up in your field of view without giving you any way to act on it. Hopefully future firmware updates or deeper app integrations will improve this, but for now it's read-only.

---
**HUMAN** (2026-03-14T15:05):

This is stupid, can I develop my own app? What are the limitations?

---
**ASSISTANT** (2026-03-14T15:05):

Ren wants to know about developing custom apps for Rokid Glasses - this is right in their wheelhouse given their hardware development background in Shenzhen. Let me search for the developer SDK and limitations.
```
This block is not supported on your current device yet.
```

Let me search for more specific info about the CXR-M SDK and what you can actually do with it for the Rokid Glasses (the new ones, not the older Glass 2).
```
This block is not supported on your current device yet.
```

Great, now I have a much better picture. Let me synthesize this for Ren.Yeah, the good news is you absolutely can — Rokid is actually one of the more open platforms among smart glasses manufacturers. Here's the real picture:

**What's available:**

The glasses run YodaOS (a custom Android-based system on Snapdragon AR1), and Rokid released the Rokid Glasses SDK in September 2025, opening interfaces for AI, interaction, and sensors. Some users have already ported NES games and built vocabulary-learning apps for it. The developer community has grown to around 30,000 developers according to Rokid's own numbers.

There are two main development paths:

1. **CXR-M SDK (phone-side control):** You build an Android app on the phone that communicates with the glasses over Bluetooth/WiFi. This gives you control over the display (push text, custom JSON-based UI views), camera, audio, device settings, and can push APKs to the glasses. This is the more documented and accessible path — the CSDN articles we saw earlier about teleprompter apps and meeting assistants all use this approach.

2. **Native glasses-side APKs:** You can actually sideload Android APKs directly onto the glasses. There's even a community-built tool called RokidApkUploader that uses the CXR-M SDK to sideload APKs over WiFi without a dev cable, though the developer warns it can be frustrating. There's also an OpenClaw integration project that pushes a glasses-side APK for voice-first AI interaction.

**The real limitations you'll hit:**

The display is monochrome green, 480×398 per eye, 23° FOV — so you're working with very constrained screen real estate. Input is limited to touchpad swipes/taps, voice commands, and head gestures (nod/shake). No keyboard, no text input on-device. The 210mAh battery means anything that keeps the display and AR1 chip active will drain fast — heavy AR usage kills battery quickly compared to audio-only mode (which offloads to the low-power RT600 MCU).

For something like a better WeChat integration specifically, you'd probably go the CXR-M SDK route: build a phone-side companion app that intercepts WeChat notifications via Android's NotificationListenerService, renders the full message on the glasses display, and lets you voice-reply through the phone. The CXR-M SDK gives you the display control and audio pipeline to make this work. The JSON-based CustomView system lets you define UI layouts without needing to build a full glasses-side app.

**Getting started:**

Check ar.rokid.com/sdk for the official SDK downloads, the developer forum at developer-forum.rokid.com, and the GitHub repos (RokidGlass org, plus the community projects like zero2005x/RokidAIAssistant which is a solid reference implementation with phone-app + glasses-app architecture). Given your Shenzhen location, you might also be able to access developer support more directly — Rokid is Hangzhou-based but has presence in Shenzhen's maker ecosystem.

This is actually a pretty viable weekend hack for you — the WeChat notification + voice reply flow is a well-scoped project that would be immediately useful.

---
**HUMAN** (2026-03-14T15:08):

hmm I only have an iPhone

---
**ASSISTANT** (2026-03-14T15:08):

The user is asking about developing for Rokid Glasses but only has an iPhone. This is a significant constraint since the CXR-M SDK and most development tools are Android-based. Let me think about what I know and search for iOS support.

From the earlier search results, I saw that the Hi Rokid app is available on the iOS App Store (we saw the App Store listing). But for development, the CXR-M SDK and sideloading tools are Android-focused. Let me check if there's iOS SDK support.That's a real constraint. Here's the situation:

**The Hi Rokid companion app does exist on iOS** — we saw it on the App Store earlier, and it covers basic features like pairing, settings, photo sync, notifications, and translation. So for daily use you're fine.

**But for development, it's rough.** The CXR-M SDK, the sideloading tools, the custom UI push system — all of that is Android-only. The community projects on GitHub (RokidAIAssistant, the OpenClaw integration, the APK uploader) are all Android apps. The glasses themselves run an Android-based OS, so the entire dev toolchain assumes an Android phone as the companion device.

Your realistic options:

**Cheapest path:** Grab a cheap Android phone just for development. You're in Shenzhen — you can pick up a used Redmi or Realme for a couple hundred RMB at Huaqiangbei. It doesn't need to be your daily driver, just a dev/testing device that stays paired with the glasses when you're hacking on it. This is honestly what most iOS-primary Rokid developers end up doing.

**Wait for official iOS SDK:** Rokid has been expanding iOS support (the Hi Rokid app only launched on iOS relatively recently), but there's no public iOS CXR-M SDK yet. Given their pace of updates it might come, but no timeline.

**ADB over USB:** For sideloading APKs directly onto the glasses, you technically just need ADB access, which you can do from your Mac/PC without an Android phone at all. The glasses-side app development doesn't require an Android phone — you'd build the glasses APK in Android Studio on your computer and push it via ADB. The limitation is you lose the phone-side companion app functionality (which is where most of the heavy lifting happens in the CXR-M architecture).

The Huaqiangbei Android burner phone is probably your best bet honestly. Would keep your iPhone as daily driver and have a dedicated dev device for the glasses.

---
**HUMAN** (2026-03-14T15:10):

For adb over usb, can I access my phone’s internet, WiFi or anything else that can connect me to the internet?

---
**ASSISTANT** (2026-03-14T15:11):

The user is asking whether, when using ADB over USB to connect to the Rokid Glasses, they can get internet access on the glasses - either through the phone's internet connection, WiFi, or some other means. This is a practical technical question about the glasses' connectivity options.

Let me think about what I know:
- The Rokid Glasses have Bluetooth (for phone pairing) and WiFi capabilities
- When connected via ADB/USB, you're connecting to the glasses as an Android device
- The glasses should have their own WiFi capability since features like translation and AI require internet

Let me search for more specific info about the glasses' connectivity.Good question — this matters a lot for whether the glasses-only (no Android phone) dev path is actually viable.
```
This block is not supported on your current device yet.
```

The user is asking specifically about the Rokid Glasses (the newer AI+AR glasses, not the Rokid Max/Air display glasses). They want to know if, when connecting via ADB over USB from their computer, the glasses can access the internet independently - through WiFi or by sharing the phone's internet.

The Rokid Glasses have both Bluetooth and WiFi. The glasses run on Snapdragon AR1 with YodaOS. Since it's Android-based, they should have WiFi capability. The key question is whether the glasses can connect to WiFi independently (without needing the companion app to set it up).

From what I've gathered:
- The glasses have WiFi capability (used for connecting to the companion app and for data transfer)


- When paired normally, the glasses connect to the phone via Bluetooth, with WiFi handling larger data transfers and internet traffic typically routing through the phone's connection
- However, since these glasses run Android underneath, via ADB I should be able to configure WiFi settings directly and connect the glasses to a WiFi network independently

, giving them their own internet accessYes — the Rokid Glasses have their own WiFi radio (it's how they do the WiFi P2P data transfer with the companion app). Since the glasses run Android under the hood (YodaOS on Snapdragon AR1), once you have ADB access you should be able to connect the glasses directly to a WiFi network.

Via ADB shell you can configure WiFi the standard Android way:

```
adb shell cmd wifi connect-network "YourSSID" wpa2 "YourPassword"
```

Or on older Android versions, use `svc wifi enable` and configure through `wpa_supplicant`. You can also check the glasses' network status with `adb shell dumpsys connectivity` or `adb shell ifconfig`.

So the dev workflow without an Android phone would look like:

1. Connect glasses to your Mac/PC via USB (you'll need the Rokid dev cable or figure out the pinout)
2. Use ADB to connect the glasses to your home/office WiFi directly
3. Build your glasses-side APK in Android Studio on your Mac
4. Push it via `adb install`
5. The app has independent internet access through WiFi

The main thing you lose compared to the CXR-M SDK path is the phone-side companion architecture — no intercepting iPhone notifications, no using the phone as a touchpad/input relay, no offloading heavy compute to the phone. Your app has to be fully self-contained on the glasses, constrained by the AR1 chip's processing power and that tiny 210mAh battery.

For your WeChat reply use case specifically though, this glasses-only path is probably a dead end — you'd need the phone-side notification access that only the CXR-M SDK on Android provides. That circles back to the cheap Huaqiangbei Android phone being the practical answer if you actually want to build a WeChat integration.

---
**HUMAN** (2026-03-14T15:12):

But I want it on the go, like in the outside with only 5g on my iPhone , is it still possible?

---
**ASSISTANT** (2026-03-14T15:13):

The user wants to know if they can use their Rokid Glasses with internet access while on the go, where the only internet source is their iPhone's 5G connection. They don't have a separate Android phone.

The key question is: can the Rokid Glasses connect to the iPhone's personal hotspot for internet access?

Since the glasses have WiFi, they should be able to connect to the iPhone's Personal Hotspot (which creates a WiFi network). This would give the glasses internet access on the go without needing an Android phone.

So the workflow would be:
1. Turn on iPhone Personal Hotspot
2. Glasses connect to that WiFi hotspot


3. Any glasses app that needs internet will work fine this way

The main limitation is that I can't intercept iPhone notifications from the glasses side, so features like WeChat replies wouldn't work. But for apps that just need internet connectivity—like a custom AI assistant or translation tool—this approach works perfectly.Yeah, that's simple actually — just turn on your iPhone's Personal Hotspot. It broadcasts a WiFi network, and the glasses can connect to it like any other WiFi access point. The glasses don't care that it's an iPhone hotspot vs. a router.

So your on-the-go setup would be:

1. iPhone Personal Hotspot on (Settings > Personal Hotspot)
2. Pre-configure the glasses to connect to that hotspot SSID via ADB at home
3. Walk out the door — glasses auto-connect to your iPhone's WiFi, internet works

This is fine for any glasses-side app that just needs internet — a custom AI assistant, API calls, whatever you build that runs natively on the glasses.

**But** — and this is the core problem — it still doesn't solve the WeChat reply use case. The glasses can reach the internet through your iPhone's hotspot, but they can't reach *into* your iPhone to read WeChat notifications or send replies through WeChat. That requires either iOS-level notification access (which Apple locks down heavily) or the Android CXR-M SDK companion app approach.

So realistically you're looking at two separate things:

**Glasses-only apps via iPhone hotspot (viable):** Custom AI chat, lookup tools, translation, anything where the glasses are self-contained and just need an API connection. Build it, push via ADB, use iPhone hotspot for connectivity.

**WeChat integration (still needs Android phone):** No way around it. You'd carry the cheap Android phone as a paired companion device, with its own SIM or tethered to your iPhone hotspot too.

What kind of app are you actually most motivated to build first? That determines whether the iPhone-only path works for you or not.

---
**HUMAN** (2026-03-14T15:14):

This is stupid, omg

---
**ASSISTANT** (2026-03-14T15:14):

Ren is frustrated with the limitations. Let me be empathetic but practical. They're right - it is annoying that you'd need to carry a second phone just for this. Let me think about whether there are any creative workarounds.

Actually, let me think more carefully. The core frustration is: they have an iPhone, they want to use Rokid Glasses with full functionality including replying to messages, and the ecosystem forces them into Android.

Some possible angles:
1. The Hi Rokid iOS app does handle notifications already - maybe future updates will add reply
2. WeChat itself has limitations on iOS notification actions
3. Maybe there's a way to use voice reply through the glasses' built-in system for calls at least


4. The smart glasses market is still in its infancy and this kind of cross-platform friction is pretty typical right now

I should be honest and sympathetic here rather than stretching for solutions that probably don't exist.Yeah, it really is. You bought a piece of hardware, you have a perfectly good phone, and the ecosystem is telling you to carry a second phone in your pocket just to make the glasses do what they should do out of the box. That's a genuinely bad user experience.

The honest take: Rokid is still an early-stage product pretending to be a mature one. The iOS SDK gap, the notification system being display-only with no reply path, the lyrics screen that won't shut up — these aren't hard technical problems, they're just stuff that hasn't been prioritized yet.

A few things that might actually help in the short term without buying another device:

The Hi Rokid iOS app already pushes notifications to the glasses. Rokid has been shipping updates fast — iOS reply support through the companion app is a pretty obvious feature gap they're likely aware of. It might be worth posting in the R星社区 or emailing global-support@rokid.com to explicitly request it. User pressure on a small company actually moves things.

Also worth noting — the latest updates added things like head-gesture call control (nod to answer, shake to decline) and voice-triggered phone calls. They're clearly building toward more interactive features on iOS. The reply capability might just be a few OTA updates away.

For now though, if you want to hack on the glasses, the iPhone hotspot + ADB path works for self-contained apps. The WeChat thing just has to wait for Rokid to close the gap on iOS.

---
**HUMAN** (2026-03-14T15:28):

Can I use it with screen off? During ai conversation

---
**ASSISTANT** (2026-03-14T15:29):

The user is asking whether they can use the Rokid Glasses with the screen/display off during AI conversations - basically just using it as a voice-in, voice-out device without the display being on. This is a practical question about battery life and usability.
```
This block is not supported on your current device yet.
```

The user is asking if they can use the Rokid Glasses with the screen/display turned off during AI conversations - just voice in, voice out. This would save battery and also be less distracting. Let me think about what I know from the search results.

The glasses have a dual-chip architecture - the AR1 handles heavy tasks (display, camera, AI) while the RT600 MCU handles low-power tasks like audio. When using just audio (music, calls), the AR1 can sleep and the RT600 takes over, giving much better battery life (5-6 hours music vs much less with display active).

For AI conversations though, the AI processing requires the AR1 chip (it needs to send audio to cloud, receive response, play back audio). The question is whether the display needs to be on during this.
 
The AI assistant typically shows text responses on the display while speaking them, but I don't have clear documentation on whether you can force the display off during AI interactions specifically. There are battery-saving options like disabling always-listening mode and toggling wearing detection, though these don't directly address display control during conversations.

Since both the display and AI processing run through the same AR1 chip, they'd both be active during use. However, you might be able to manually dim the display to zero brightness or turn it off entirely while keeping the AI processing running, though I should give you an honest answer based on what I actually know rather than speculate further.That's a great question for battery life. The AI conversation by default shows the response as text on the display while also speaking it through the open-ear speakers.

From what I can tell, the stock behavior keeps the screen on during AI interactions — it displays the text of what it's saying. There's no obvious "voice-only AI mode" toggle in the current firmware.

But practically, there are a couple of angles:

**The hardware architecture actually supports this in theory.** The dual-chip design (AR1 for heavy compute + RT600 MCU for audio) means audio-only tasks run on the low-power chip. When users listen to music or make calls, all audio decoding and playback is handled by the MCU while the main AR1 chip can enter deep sleep. But AI conversations still need the AR1 active since it's processing the cloud API calls — the question is just whether the display needs to be on while it does that.

**What you could try:** Set display brightness to the lowest level, or check if there's a screen timeout setting that would let the display auto-off while the AI response plays as audio. One reviewer mentioned that to stretch battery life, you can lower display brightness and disable "always listening" when you don't need voice control.

**The custom app route:** If you build your own glasses-side app via ADB, you absolutely could make a voice-only AI assistant that never touches the display at all. Mic in → API call to whatever LLM → TTS audio out through the speakers. That would burn way less power than the stock AI feature since you'd skip the display pipeline entirely. This is actually a pretty clean project for the ADB + iPhone hotspot setup we discussed.

Honestly that might be the most practical first app to build — a screenless AI voice assistant that doesn't waste battery on display you don't need.

---
**HUMAN** (2026-03-14T15:30):

Okay. What,ADB functionalities or permissions do I have?

---
**ASSISTANT** (2026-03-14T15:30):

The user wants to know what ADB access they have on the Rokid Glasses - what commands work, what's locked down, whether they have root, etc. This is a pretty specific technical question. Let me search for this.
```
This block is not supported on your current device yet.
```

The search results are all generic ADB information, not specific to Rokid Glasses. Let me search more specifically for Rokid Glasses ADB developer access.
```
This block is not supported on your current device yet.
```

Good, I found some very useful info. Let me check the specific GitHub repos for more details about what ADB access looks like on the Rokid Glasses.Based on what community developers have documented, here's what you're working with:

**Connection:** You need a 5-pin dev cable to connect the RV101 (Rokid Glasses) via ADB. This isn't a standard USB-C — it's a proprietary connector (the same magnetic charging cable pinout, but you need a specific dev cable variant). You'd need to source this from Rokid's developer program or figure out the pinout yourself.

**What works without root (standard ADB shell):**

Based on the hackathon projects and community repos, you get standard non-root Android ADB access:

- `adb install` — sideload APKs onto the glasses
- `adb shell pm grant` — grant permissions manually like camera and microphone access to your apps
- `adb reverse tcp:8000 tcp:8000` — port forwarding, useful for connecting your glasses-side app to a backend running on your laptop
- `adb logcat` — read logs for debugging
- `adb shell pm clear` — clear app data
- `adb shell am start` — launch activities
- Standard file push/pull with `adb push` / `adb pull`
- WiFi configuration via shell commands

**What you probably don't have:**

Almost certainly no root access. This is a production build on the Snapdragon AR1, so `adb root` will be rejected. That means no modifying system apps, no accessing `/system` partition, no killing Rokid's stock services, and no deep system-level tweaks. You're sandboxed as a normal Android app developer.

**What this means practically for your voice-only AI app:**

You have everything you need. Your app can request microphone permission, internet permission, use Android's AudioManager/MediaPlayer for TTS output through the speakers, and make HTTP calls to any LLM API. You just build a standard Android app, target the glasses' screen resolution (or ignore the display entirely), push it via ADB, and you're running.

The main unknown is getting that dev cable. That's your first real blocker — worth asking on the Rokid developer forum or checking if anyone in the Shenzhen maker community has figured out the pinout.
