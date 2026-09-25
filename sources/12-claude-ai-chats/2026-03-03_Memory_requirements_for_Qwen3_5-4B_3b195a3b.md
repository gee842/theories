# Memory requirements for Qwen3.5-4B

created: 2026-03-03T07:28:43.820918Z  uuid: 3b195a3b-a92f-45d7-ac42-a8ca8d22775b  export: old
messages: 3  total_chars: 1801  human_chars: 100

summary: **Conversation Overview**

The user asked a brief technical question about the memory requirements to run Qwen3.5-4B, a large language model from the Qwen3.5 small series. Claude used a web search to find current information and provided a breakdown of VRAM requirements by quantization level: approximately 9GB for FP16, ~4GB for Q8, and ~2GB for Q4. Claude also noted that the full Qwen3.5 small series (0.8B through 9B) can run in near full precision on 12GB of RAM/VRAM, with that ceiling sized for the 9B model. Claude characterized the 4B model as suitable for edge devices, noting compatibility with modern GPUs with 4GB+ VRAM or Apple Silicon Macs with 8GB unified memory. The conversation was a single exchange with no follow-up or corrections.


---
**HUMAN** (2026-03-03T07:28):

What’s the memory required to run Qwen3.5-4B

---
**ASSISTANT** (2026-03-03T07:29):

The user is asking about memory requirements for Qwen3.5-4B. Let me search for this since it's a specific model that may have been released after my knowledge cutoff.
```
This block is not supported on your current device yet.
```

The user asked about Qwen3.5-4B specifically. From the search results, I can see that the Qwen3.5 small series includes 0.8B, 2B, 4B, and 9B models. The Unsloth guide says for the small series (including 4B), "you'll just need 12GB of RAM / VRAM / unified memory device" to run them "in near full precision" - but that seems to be for the 9B variant specifically.

For Qwen3-4B (previous gen), the data shows ~3.9GB FP16, ~2GB Q4. The Qwen3.5-4B should be similar in size since it's also 4B parameters.


Based on what I've found, I can give the user a solid answer about the memory requirements for running Qwen3.5-4B.Based on the search results, here's what you need for Qwen3.5-4B:

The Qwen3.5 small series (0.8B, 2B, 4B, and 9B) can all run in near full precision with just 12GB of RAM/VRAM/unified memory — though that 12GB figure is sized for the largest model in the small series (9B). The 4B model will need less.

For more specific estimates, looking at the comparable Qwen3-4B (same parameter count):

- FP16 requires about 9GB, Q8 quantization needs roughly 4GB, and Q4 quantization only needs about 2GB of VRAM

So in practice, the Qwen3.5-4B should be very accessible — you can run it quantized on basically any modern GPU with 4GB+ VRAM, or even on a base Apple Silicon Mac with 8GB unified memory. At full precision you'd want at least 8–10GB available. Given your interest in AI hardware products, this is firmly in the "runs on edge devices" category.

---
**HUMAN** (2026-03-03T07:30):

If I run it on raspberry pi, what’s the token per second
