# Runtime — 服务器的浏览器操作系统 · 总体规划 v4（完整版）

> **Status（P7 之后）**：P0–P2、P4–P7 已完成并在 Mac 上全绿；P3b（真实服务器）待域名 +
> SSH。本文件是**计划**，不随实现改写；已建成的系统见 [README.md](README.md) 与
> `docs/`（architecture · invariants · add-an-app · deploy · recovery），验收现状见
> [docs/acceptance.md](docs/acceptance.md)。

> 定位：独立部署在你 server 上的 web dashboard（shell），单次 passkey 登录，进入一个**不断增长**的 app 列表 —— Terminal、Editor、Desktop 起步，之后是 agent UI、files、host-admin，以及任何你想写的页面。**这是你与 server 交互的主 UI。**
>
> 北极星：**加一个新 app 必须便宜。** 工程哲学：**骨架自写、器官现成；质量靠类型 + 少量锋利的 e2e，不靠流程。**
>
> 阅读地图：Part I 看懂整个系统（架构在 §2）；Part II 分层设计；Part III 工程与执行。附录 A 是决策记录。

---

# Part I — 愿景与整体架构

## 1. 意图：这是什么、为谁、往哪长

- **是什么**：你的 server 的 runtime + 它的浏览器入口。login 一次，terminal / desktop / code editor…都在里面。
- **核心诉求**（按你的原话）：这个 list 会不断增加——你想要的功能、页面、agent UI 会越来越丰富，**你自己想要的界面你都可以 code 一个挂上去**。因此架构第一优先级是可扩展性。
- **主 UI**：这是你以后与 server 交互的主要方式，可靠性与恢复路径是一等要求。
- **关闭页面 ≠ 中断任何东西**：进程不死（terminal 里挂着的 ssh 不断），回来时页面处于关闭前的状态。
- **未来 multi-user**：逐渐开放给朋友。v0 单用户，但 identity/schema/授权从第一天按 multi-user 建模，邀请制，永无公开注册。

## 2. 整体架构

### 2.1 全景

```
                        Browser（你；未来：朋友）
                                │  仅 HTTPS / WSS
 ───────────────────────────────┼─────────────────────────────── 公网边界
                                ▼
              ┌──────── Caddy :443（唯一公网入口）────────┐
              │     TLS · registry 生成的路由 · 每请求     │
              │     forward_auth → authd（唯一决策点）     │
              └───┬──────┬──────┬──────┬──────┬───────────┘
                  │      │      │      │      │     （下行全部经 unix socket）
                  ▼      ▼      ▼      ▼      ▼
   origins:    os.<d>  terminal  editor  desktop  host.<d>
               shell    .<d>     .<d>    .<d>     host terminal
               +authd  终端 UI  code-   Xpra     （owner+step-up）
               +/__api          server  HTML5         │
                  │      │        │      │            │
                  ▼      ▼        ▼      ▼            ▼
   services:  ┌─ authd ─┐  ┌── workspace-main 容器 ──────────────┐   host-terminald
              │ passkey │  │  rootless Podman · systemd PID1     │   (User=ren, P5)
              │ session │  │  dev 用户（容器内 sudo）              │        │
              │ SQLite  │  │  terminald → tmux → zsh·vim·ssh·agent│     tmux(host)
              └─────────┘  │  code-server ─┐                     │        │
              (authd 用户)  │  Xpra → XFCE ─┴─ 同一个 /home/dev    │    host shell
                           │                    与 /workspace     │
                           └─────────────────────────────────────┘
                            (compute 用户；数据卷持久化在 host 上)
 ─────────────────────────────────────────────────────────────── host 边界
  Host = Ubuntu 24.04
  用户：ren（人类 admin，sudo，SSH）· compute（无 sudo，跑 workspace）· authd（无 sudo，跑 authd）
  host 级常驻服务只有 Caddy（apt）；SSH = break-glass，永远独立于以上一切
```

### 2.2 认证平面（与 2.1 正交的一条线）

```
一次登录      os.<d>/login（顶层页面）→ Touch ID / passkey → __Host-rt_central（os 域）
    │
无感换票      iframe 打开 terminal.<d> ─无票→ 设一次性 state cookie
（每 surface）   → 302 os.<d>/__runtime/authorize → 验 central → code（绑 state）
      　        → 302 terminal.<d>/__runtime/callback → 验 code+state
      　        → Set __Host-rt_terminal → 放行            全程 <100ms，无 UI
    │
每个请求      Caddy forward_auth → authd：验 surface 票 → central 存活 → access
      　      → step-up 新鲜度 →（WS 时）Origin 白名单 → 200/302/401
    │
长连接        terminald 每 5min introspect 复验 · WS 12h 硬上限 · host app idle 10min
```

### 2.3 信任边界（由外到内）

1. **公网 ↔ Caddy**：只有 80/443 暴露；一切内部服务在 unix socket 后。
2. **origin ↔ origin**：shell 与每个 high-trust app 各自独立 origin + 独立 `__Host-` cookie；shell 被 XSS 拿不到任何 surface 凭据，也过不了 WS Origin 校验。
3. **gateway ↔ service**：Caddy 经权限受控的 unix socket 连 upstream；本机低权用户绕不过 Caddy（回环 TCP 是提权面，已弃用）。
4. **service ↔ service**：三个 unix 用户互相隔离；authd 摸不到 workspace 数据，compute 无 sudo。
5. **容器 ↔ host**：workspace 是 rootless 容器，无 host socket/filesystem/network；容器内 root ≠ host root。
6. **web 栈 ↔ SSH**：SSH 与网络配置永不被本系统管理；web 全挂时 SSH 必在。

### 2.4 核心抽象（六个词）

```
Shell     dashboard 本身：登录、导航、app 宿主、连接状态
App       registry 的一条声明：UI + 权限 + 指向某个 service
Service   跑在某个 target 上的后端（自写 daemon 或现成软件），经 unix socket 被 Caddy 反代
Gateway   Caddy：TLS、生成的路由、每请求 forward_auth
Auth      authd：passkey、central session、per-surface 换票、唯一 authz 决策点
Runtime   target：workspace-main 容器（默认）、host、未来多 workspace / 多机
```

新能力落点的判断法（架构是否还健康的测试）：**新 app = registry 一条 + 叶子目录；换桌面协议 = image 改动；加 target = 注册表一行；朋友入驻 = 数据行。核心代码永远不被触碰 —— apps are data, platform is code。**

## 3. 与最初方案（另一个 assistant）的取舍

**保留**（方向正确的部分）：
- terminal 链：xterm.js → WebSocket → node-pty → tmux；现成件 code-server、Xpra+XFCE
- rootless Podman + Quadlet + systemd 管 workspace；Caddy 唯一边缘 + forward_auth
- WebAuthn/passkey（SimpleWebAuthn）、SQLite、per-surface 独立 origin + cookie
- 「workspace runtime 可弃、user state 持久」；部署顺序安全（SSH 最后动）
- 观测极简主义（journald + doctor，不上 Prometheus/Grafana）；backup 少而真（数据卷 + SQLite + 配置）

**修改**（与你的意图冲突或过度/欠缺设计的部分）：
1. 它定位「嵌入现有网站的 computer」→ **dashboard 即产品，独立站点**。
2. 它把扩展性列为 non-goal（"v0 是 Computer 不是 Platform"）→ **registry + 加 app 流程是 v0 核心交付物**，三件套只是前三个 app。
3. 双层解锁（网站登录 + compute unlock）→ **单次 passkey 登录 + 静默换票**（隔离不降级，仪式减一步；纵深由 step-up 补）。
4. 只允许 workspace 容器 → **runtime target 注册表**（workspace 默认；host、host-admin、多 workspace 都是后续 target）。
5. 完全没有 multi-user 设计 → schema/授权第一天按 multi-user 建。
6. （后续 review 又砍掉了它与我 v1 都有的 auth 独立子域 → authd 并入 os 域保留前缀，见 §6。）

## 4. 拓扑与域名

### 生产（占位 `BASE_DOMAIN=example.com`，域名到位只改一处 config）

```
os.example.com          shell + authd（保留前缀）+ builtin 数据（/__api）
terminal.example.com    terminal app（workspace target）
editor.example.com      code-server
desktop.example.com     Xpra HTML5
host.example.com        host terminal（step-up）
```

**保留前缀**（生成器用互斥 handle 块保证优先于 forward_auth 与静态资源，surface 自身永不使用）：

```
所有域名   /__runtime/*   → authd（换票机关；os 域上还有登录/session/authorize 全套）
os 域      /__api/<id>/*  → 对应 builtin 后端 service（central session 门禁）
```

- **硬约束**：全部子域同一 registrable domain（same-site → iframe cookie 不被第三方 cookie 政策拦截；RP ID = apex 覆盖全部子域）。域名必须是自有注册域、**不在 Public Suffix List**。
- DNS：一条 wildcard A 记录；Caddy 自动 per-host TLS。
- 公网仅 80/443 + SSH（break-glass，P7 前不动、之后再议收紧且永远保留通道）。

### 本地开发（全保真，Mac 上跑，P0 即建立）

```
DEV_DOMAIN=runtime.test（.test 不在 PSL，可作 RP ID）
/etc/hosts 一行（gen 打印）；Caddy brew + tls internal + caddy trust（一次管理员密码）
```

- 同一生成器输出 `Caddyfile.dev`（upstream 指 vite/tsx 回环端口）与 `Caddyfile.prod`（unix socket）。
- WebAuthn 真实可用（真 Touch ID）；Firefox 需另装 CA，主力 Safari/Chrome。
- dev 的回环端口仍强制 Origin/Host 校验（DNS rebinding 防线，不可关闭）。
- vite 模板统一 `server.allowedHosts: ['.runtime.test']`（Vite ≥6.0.9 的 Host 白名单会拦代理请求）。
- terminald 本地直接 spawn brew 的 tmux——容器只在服务器上出现，不进开发内环。
- `pnpm dev` 一条命令起全栈。

---

# Part II — 分层设计

## 5. 认证与会话

**单次 passkey 登录解锁全部。** authd = Fastify + SimpleWebAuthn（**锁 v13 文档口径**，网上大量 v9/v10 旧 API 不可照抄）+ better-sqlite3，全 TS。

### 5.1 会话模型

- **central session**：`__Host-rt_central`，HttpOnly，挂 os 域（authd 与 shell 同源，零 CORS）。DB 有行（存 cookie 值的**哈希**——备份泄露 ≠ 活会话泄露），30 天滚动，记录 `last_passkey_at`。
- **surface token**：每 surface 独立 `__Host-rt_<app>`，无状态 HMAC token `{uid, aud, sid, exp}`（24h）。校验时顺带查 `sid` 的 central 存活 → 登出/撤销立即生效（长连见 5.4）。省一张表，不省可撤销性。
- **`__Host-` 前缀强制**（Secure、无 Domain、Path=/）：浏览器层面杜绝兄弟子域 cookie tossing。全部 cookie 带 Max-Age 持久化：TTL 内重开浏览器零摩擦，过期也只是一次 Touch ID。
- **auth code**：一次性、30 秒、audience 绑定、**绑定发起浏览器**（state）。≥128-bit CSPRNG，哈希入库。
- **step-up**：`stepUp: true` 的 app 要求 `last_passkey_at` ≤ 10 分钟，否则重做一次 assertion（不重建 session，只刷新时间戳）。
- **WebAuthn ceremony（登录/注册/step-up）一律在顶层页面完成**——iframe 内需要跨源委托且 Safari 支持残缺（三方 review 共识）：shell 挂载 stepUp app 前先查 `/session` 新鲜度，顶层完成 assertion 再挂 iframe；直开子域时 authorize 渲染顶层 passkey 页。

### 5.2 静默换票（本设计的机关）

surface 域上的 `/__runtime/*` 由 Caddy 路由给 authd。cookie 是 host-only 的，必须由"该域名下的响应"设置——这个保留前缀就是 authd 在每个 surface 域上的落点，**surface 因此不需要任何自己的认证后端**：

```
iframe 打开 terminal.example.com
  forward_auth：无有效 rt_terminal
    → authd 先在 terminal 域设一次性 __Host-state cookie
    → 302 os.example.com/__runtime/authorize?aud=terminal&redirect=…
  central 有效 → 发 code（绑 state 哈希）→ 302 terminal.example.com/__runtime/callback?code=…
  callback 验 code + state 双向匹配 → Set-Cookie __Host-rt_terminal → 302 回原路径 → 放行
central 无效 → 302 os.example.com/login?next=…（顶层登录后原路返回）
```

防线（全部进 e2e 安全矩阵）：
- **state 绑定**：code 只能被发起换票的那个浏览器消费——封死"注入他人 code 的会话固定"。
- **redirect 白名单**：仅该 aud 对应 origin 的路径；拒 `//`、`/\` 开头；其余回落 `/`。
- **Sec-Fetch-Site 门**：`/__runtime/*` 与 authorize 拒 cross-site 发起（顺带封 XS-Leak 探测与跨站铸码）。
- `/__runtime/*` 响应带 `Referrer-Policy: no-referrer`（callback URL 携 code）；换票链带循环熔断。

### 5.3 forward_auth（唯一 authz 点）

由 `X-Forwarded-Host` 映射 app（gen 产出的 JSON 配置）→ 验 `rt_<app>` 签名/aud/exp → 查 central 存活 → 查 `access`（owner|member）→ 查 step-up 新鲜度 → **对 `websocket: true` 的 app 集中校验 Upgrade 的 Origin**（白名单由 registry 生成，通常仅 self + shell；不依赖 code-server/Xpra 自己验）→ `200 + X-Runtime-User / X-Runtime-Session` 或 302/401。terminald 的 Origin 自校验降级为纵深。

### 5.4 长连接的撤销（review P0 修复）

forward_auth 只覆盖 upgrade 时刻，故：terminald 持 sid **每 5 分钟调 `/__runtime/introspect` 复验**（经公网 URL；sid 为 128-bit 能力凭据，限速），失效即关 WS——tmux 保证无损；WS 12h 硬上限强制重连（app-kit 无感）；host app 另加 10 分钟 idle 断开。语义："登出立即生效" = 新请求立即拒 + 存量 WS ≤5 分钟收割。

### 5.5 端点与 schema

```
os 域 /__runtime/：login|register 的 options/verify、session、authorize、introspect、logout、healthz
      /__runtime/register：已登录 + step-up 门槛，为自己增登 passkey（防丢机锁死；onboarding 提示 ≥2 把）
各 surface 域 /__runtime/：callback、ping
```

```sql
users(id, handle UNIQUE, display_name, role CHECK(role IN('owner','member')), status, created_at)
credentials(id, user_id, public_key, counter, transports, created_at, last_used_at)
sessions(id_hash, user_id, created_at, last_seen_at, last_passkey_at, expires_at)
auth_codes(code_hash, user_id, aud, state_hash, created_at, expires_at, used_at)
invites(code_hash, role, created_by, created_at, used_by, used_at)   -- v0 有表无 UI
-- challenge 存内存（authd 单进程）+ TTL；重启中断 ceremony 可重试
```

- 首用户 bootstrap：CLI 产出**一次性高熵 token URL**（给自己的 invite）——公网上不存在"无 token 可注册"的时间窗（CT log 扫描以分钟计）。
- WebAuthn 细则：`expectedOrigin` 钉死 os 顶层 origin；counter 宽松策略（同步 passkey 恒 0，只拒回退）。
- 限速：`/webauthn/*`、authorize、introspect per-IP 限速（Caddy 层）。
- 签名密钥：文件挂入 authd 容器（0400）；轮换 = 全部 surface token 失效 = 一次全局静默换票，代价可忽略。

### 5.6 builtin 数据通路

builtin 页面跑在 os 域，数据走 `os.<d>/__api/<service>/*` → Caddy（central 门禁 + access）→ 对应 service socket。同源、credentialed、零 CORS。未来 agent UI / status 页即用此通路。

## 6. Runtime 层

### 6.1 target 注册表（server 端定义，browser 永远只能引用 id）

| target | 是什么 | 何时 |
|---|---|---|
| workspace `main` | rootless Podman 容器，完整 Ubuntu，容器内 sudo | v0 默认 |
| `host` | server 本体 shell（`ren`），独立 app + step-up | v0 核心（P5，先于 desktop） |
| host-admin app | metrics / systemd / journald GUI | v0 后 |
| 更多 workspace | project-x / 朋友的 | multi-user 阶段 |

**授权红线**：workspace-main 系 app 永远 owner-only——把现有 app 放开给 member 等于共享同一条 tmux/桌面（含你的命令历史与挂着的 ssh）。member 化必须走"每人独立 workspace"（§10）；terminald 协议按 uid 预留 session 推导位。

### 6.2 workspace-main（systemd 容器）

**image**（`images/workspace/Dockerfile`）——`ubuntu:24.04` 基座 + 全清单：

```
init/系统   systemd systemd-sysv dbus（PID 1；Podman --systemd；noble=podman 4.9，勿用 5.x Quadlet 特性）
用户        dev（容器内 NOPASSWD sudo）
shell/工具  bash zsh tmux git curl wget ca-certificates openssh-client
            build-essential ripgrep fd jq tree htop
语言        python3 + uv · node22 + pnpm
app 后端    code-server · Xpra（锁 xpra.org 官方 repo v6 LTS + xpra-html5，noble 自带是古董）
            · XFCE · terminald（经挂载交付，不烘 image）
输入法      fcitx5（desktop 中文输入，fast-follow）
```

- 服务 = 容器内 systemd unit（`User=dev`，显式 `RuntimeDirectory`/`XDG_RUNTIME_DIR`——无 logind 会话）：`terminald.service`、`code-server.service`、`xpra.service`。journald `Storage=persistent`。**未来 agents 就是这里的又一个 unit**——放弃 supervisord 换来的最大红利。
- **持久化**：host `/home/compute/data/main/{home,workspace}` → 容器 `/home/dev`、`/workspace`。容器 recreate ≈ 重启电脑：文件全在、进程重来。
- **生命周期**：Quadlet（gen 产出）→ systemd user unit（`compute` + linger）→ 开机自愈，`Restart=always`。
- **禁止**：`--privileged`、host socket / filesystem / network / PID namespace。

### 6.3 host 布局

```
ren       人类 admin，sudo，SSH
compute   无 sudo，rootless podman，拥有 workspace 数据（linger + subuid）
authd     无 sudo，跑 authd 容器（linger + subuid 同样要配）
```

Host 级服务仅 Caddy（apt）。**Caddy admin API 关闭或改 unix socket**（默认 127.0.0.1:2019 无认证，本机任意用户可改路由——bootstrap 必做）。

### 6.4 内部上游 = unix socket（review P0 修复）

回环 TCP 挡公网不挡本机用户：被攻陷的 `authd` 用户 curl 127.0.0.1 打 terminald 即拿 workspace 执行、打 host-terminald 即拿 `ren` shell——本机横向提权。因此：

- **所有内部上游经 unix socket + 文件系统权限**（仅 caddy 可连）：authd、terminald（容器内 socket 挂载到 host 目录）、code-server（`--socket`）、Xpra（`--bind-ws=socket`）、host-terminald。
- 个别上游实测不支持 socket → Caddy 注入 gateway-secret 头 + 服务端校验；再不行加 ~20 行 TS pass-through。
- 附带红利：**新 service = 挂载目录里多一个 socket 文件**，无端口发布、无容器 recreate。
- dev（Mac 单用户）保留回环 TCP，Origin/Host 校验强制。
- **host target 依赖此项先落地（P3 完成）。**

### 6.5 服务交付：不重建容器（review P0 修复）

服务烘进 image 意味着每加/改一个 daemon 都 rebuild + recreate = 杀光 tmux 里的进程。改为：

- **自写 TS 服务产物 + gen 的 unit 文件走 bind-mount 卷**（host `/home/compute/deploy/…` → 容器内），deploy = rsync 产物 → 容器内 `systemctl daemon-reload && restart <unit>`。**加/改 daemon 不碰 image、不 recreate、不杀进程**（terminald 自身重启也只掉 WS，tmux server 无感）。
- image rebuild 只留给 OS 级依赖（apt 包，如 Xpra），并作为**显式的"计划内重启电脑"事件**（自己挑时机）。
- registry 的 service 条目声明 unit 名，gen 产出 unit 文件——闭环。

## 7. 会话与状态持续性（关闭页面 ≠ 中断任何东西）

### 7.1 第一层：进程不死（服务端事实）

terminal 的一切跑在 tmux 里（shell、vim、**挂着的 ssh**、agent 进程）；Xpra session、code-server 常驻。页面关闭 / Mac 合盖 / 断网 / 换浏览器换设备，对服务端进程**完全等价且无影响**。终止进程的只有 workspace 容器重启（≈ 重启电脑）——且经 §6.5 后，日常 deploy 不再属于此类事件。

### 7.2 第二层：重连即 reattach

app-kit 指数退避重连；开 WS 前先 fetch 同源 `/__runtime/ping` 走换票链（WS 无法跟随 302）；tmux/Xpra 语义保证回到原会话；**永不回放击键**。cookie 持久化见 §5.1。

### 7.3 多客户端语义

两个 tab / 两台设备同开：**tmux grouped session**（`new-session -t main`）——共享窗口集、各自独立视口与焦点，不镜像打架；断开即销毁 grouped 实例，base session 常驻。进 e2e。

### 7.4 第三层：页面状态恢复（回来"像没关过"）

- **shell 布局**：localStorage 持久化 `{打开的 tabs、活跃 app、每 app 偏好}`，加载即恢复。（Safari 有 7 天不访问清空的上限——主 UI 天天用可接受；跨设备的服务端 user-state 在 §22 且优先级提前。）
- **切 app 不卸载 iframe**：切走只是 CSS 隐藏，切回零重载零重连。
- **terminal scrollback 回放**：重连时 terminald 先发 `capture-pane -epJ` 取**可见屏以上的历史区**（当前屏交给 attach 重绘，避免重复一屏；attach 前先按客户端尺寸 resize；alternate screen `#{alternate_on}` 跳过；v0 限单 pane），协议 `{t:'hist'}`，client 写入但不触发自动滚动。
- **editor / desktop**：code-server 恢复打开的文件与布局、Xpra 恢复窗口——天然满足。

## 8. 首发三 app 详设

### 8.1 Terminal（参照实现，最值得自己写的部分）

```
xterm.js ──wss──▶ terminald（node-pty）──▶ tmux new-session -A(-t) ──▶ zsh
```

- **协议**（`packages/protocol`，zod 双端共用，版本化）：`c→s {in|resize|ack|ping}`，`s→c {hist|out|exit|pong}`。JSON 起步，性能需要再上二进制帧。
- **流控**：ack 方案（xterm.js 官方指南）：client 每收 64KB 发 `ack`；server 未确认 >512KB `pty.pause()`、<128KB `resume()`（node-pty ≥1.1 实测可用）。
- **安全**：不存在任何 command/cwd/exec 参数；session 名服务端白名单（`^[a-z0-9-]{1,32}$`，命名 session 为 fast-follow）；bundle 零第三方脚本；CSP `default-src 'none'` 白名单化。
- **必须通过的体验验收**（e2e + 手测）：vim / htop / tmux 嵌套 / Claude·Codex 交互式 CLI、**中文显示与 IME 输入**（composition 定位、宽字符渲染——主 UI 日常体验，P2 就调手感，不留到最后）、resize、Ctrl-C/D/Z、Tab、方向键、Alt、paste、选择复制、断线重连回原 session、刷新不丢进程、`yes` 级高速输出不失控。
- xterm.js addons：fit / webgl / unicode11 / clipboard。

### 8.2 Editor

- code-server 跑在 workspace 容器内，`auth: none` + **仅 unix socket**，公网认证完全在 gateway 层。
- 它和 terminal 看到**同一个** `/home/dev` 与 `/workspace`；它的集成终端就是同一个容器环境（同一套 dotfiles、同一个 tmux 可 attach）。
- 恶意扩展的能力上限 = workspace 执行（editor 本来的能力），无 host、无他 origin 凭据。
- 未来"端口预览"需要 `--proxy-domain`/`VSCODE_PROXY_URI`，v0 不做（§22）。

### 8.3 Desktop

- **Xpra + XFCE**（决策已锁；KasmVNC/Selkies 已评估未选，桌面协议保持可替换件——swap 只是 image 改动，registry/gateway 不感知）。
- 为什么 XFCE 不是 GNOME：Ubuntu 的"外观"= GNOME Shell 只是默认桌面环境；无显卡容器里 GNOME 依赖 systemd session/合成器，出名地折腾。XFCE 是容器桌面的标准做法，装在 Ubuntu 上就是完整 Ubuntu（apt、Firefox、文件管理器都在）。在意观感可上 Yaru 主题。
- v0 范围：desktop 模式 + keyboard + mouse + clipboard + resize。**默认关闭**：audio、打印、USB、摄像头、麦克风、文件传输（有真实需求再开）。
- 已知坑（可实现性 review）：xpra.org v6 repo + xpra-html5 包；`User=dev` unit 无 logind 会话 → 显式 RuntimeDirectory/dbus/Xvfb；2–3GB 镜像慢迭代 → 这是全计划最大时间黑洞，放最后（P6）且预算单列。
- 断线重连回到同一桌面 session（窗口原样）。

## 9. Shell（dashboard 本身）

- React + Vite SPA。路由：`/login`（passkey ceremony 顶层）、`/`（registry 驱动的 app 导航）、`/a/:id`（iframe 宿主）。不引状态库。
- **iframe 常驻**（§7.4）；iframe 属性：`allow="clipboard-read; clipboard-write; fullscreen"`。
- postMessage presentation 协议（双向验 origin，白名单来自 registry）：`parent→surface {theme|visible}`，`surface→parent {ready|state|title|nav}`——**`nav` 是白名单导航 chord（枚举值如 cmd-1..9 / cmd-k，无 payload）**，解决"焦点在 iframe 时 shell 快捷键全灭"。**永不出现**：按键流、文本、命令、文件、凭据。
- 状态 UI 一览（每种情况有明确的样子，不出现白屏/裸错误）：

| 状态 | UI |
|---|---|
| 未登录 / central 过期 | 顶层 passkey 弹层（登录后各 iframe 自动恢复） |
| step-up 需要 | 顶层 assertion 提示（挂载前预检） |
| 换票/连接中 | Connecting… |
| 已连接 | 状态点 ● + app 内容 |
| 断线重连 | Reconnecting…（指数退避，永不回放击键） |
| workspace 容器启动中 | Workspace starting… |
| 服务不可用 | Unavailable + [Retry]（并提示 SSH 兜底） |

- shell 静态资源公开无敏感信息；一切数据来自同源 `/__runtime/session` 与 `/__api/*`。

## 10. Multi-user readiness（现在建模，以后开闸）

- schema 第一天就是 multi-user 的（§5.5：users/credentials/sessions/invites 全部挂 user_id + role）。
- registry 每个 app 声明 `access: owner|member`，authd 执行；v0 验收含"member 被 owner-only app 拒绝"预演。
- 注册**永远邀请制**：首用户 = bootstrap token URL；此后 owner `authd invite` 生成邀请；不存在公开注册。
- 朋友入驻的图景（不实现，只保证不堵路）：每人自己的 passkeys + **自己的 workspace 容器**（Quadlet 模板参数化 ×N；service→target 间接层已铺好，按用户换 upstream 不动 app 层）；共享 app 按 access 放开；workspace-main 系 app 永远 owner-only（§6.1 红线）。

## 11. 配置与 secrets

```
BASE_DOMAIN=example.com      # 全部 origin 按约定推导（os. / terminal. / …）
DEV_DOMAIN=runtime.test
WORKSPACE_NAME=main
SESSION_SIGNING_KEY / AUTH_CODE_SIGNING_KEY   # scripts 生成；文件挂入 authd 容器（0400）
```

- 密钥轮换 = 全部 surface token 失效 = 一次全局静默换票（代价可忽略），写进 runbook。
- **永不进 gateway/authd 环境**：GitHub token、Anthropic/OpenAI key、SSH 私钥——它们属于 workspace 内你自己的 dotfiles/secret 管理。agent secrets 未来随 agentd 单独设计。

---

# Part III — 工程与执行

## 12. Repo 结构（pnpm monorepo，TypeScript）

```
runtime/
├── apps/
│   ├── shell/              # dashboard SPA（React + Vite）
│   └── terminal/           # xterm.js UI（独立小 bundle）
├── services/
│   ├── authd/              # Fastify + SimpleWebAuthn + better-sqlite3
│   └── terminald/          # node-pty ↔ tmux bridge（workspace 与 host 两个部署形态）
├── packages/
│   ├── registry/           # ★ 唯一真理源：targets + services + apps + origins
│   ├── protocol/           # terminal WS 消息 + postMessage 消息（zod，版本化）
│   └── app-kit/            # 浏览器通用件：ping-then-WS、重连、postMessage、nav chord、主题
├── images/
│   └── workspace/          # Dockerfile、容器内 systemd units、构建脚本
├── infra/
│   ├── caddy/              # 模板 + 生成的 Caddyfile.{dev,prod}（提交进 repo）
│   └── quadlet/            # 模板 + 生成的 workspace-main.container、authd.container（提交）
├── scripts/
│   ├── dev.ts              # 一条命令起本地全栈
│   ├── gen.ts              # registry → Caddyfile/Quadlet/units/JSON 配置/hosts 行；--check 防漂移
│   ├── new-app.ts          # 骨架 + registry 条目
│   ├── bootstrap-host.sh   # 三用户 + linger×2 + subuid×2 + podman/caddy + admin off（幂等）
│   ├── deploy.sh           # gen --check → rsync → 各用户 build/restart → restart caddy
│   ├── doctor.sh           # DNS/TLS/healthz/容器/socket 权限/AppArmor userns/磁盘
│   └── backup.sh restore.sh
└── docs/                   # P7 从本文件拆出：architecture / invariants / add-an-app / recovery
```

## 13. 省力工程学

1. **一种语言**：全 TypeScript；bash 仅 bootstrap / doctor / backup（服务器无 Node 的场合）。
2. **一个部署原语**：容器 + Quadlet（authd 也容器化）；自写服务走挂载交付（§6.5）。
3. **一个真理源**：registry 生成一切；**生成物提交进 repo**（server 零 Node 依赖，直到 P5 host target）；**authd 运行时读 gen 产出的 JSON**（不 import TS registry——加 app 后 rsync + 重启 authd 即生效）。
4. **一条本地开发环**：§4 dev 拓扑，认证/换票/terminal/e2e 全在 Mac 秒级反馈；容器/DNS/TLS 只在服务器阶段。
5. **自写代码预算**（review 校准；超预算 = 回头改设计）：

| 组件 | 预算 |
|---|---|
| authd | ~1000 行（端点 ×10、state/introspect、CLI、迁移） |
| terminald | ~400 行（grouped session、hist 回放、复验） |
| 生成器 | ~250 行哑模板 |
| shell + terminal UI + app-kit | ~1500 行（工作量大头，明示不隐藏） |

6. 买来的 boring 件：tmux、code-server、Xpra、Caddy、SimpleWebAuthn、node-pty、better-sqlite3——每个都被 gateway + registry 隔离成可替换件。
7. 工具链：pnpm workspaces（不上 turbo/nx）、Vite、tsx、Biome、vitest、Playwright（**1.61+ `browserContext.credentials` passkey API，回退 CDP virtual authenticator；Chromium-only；CI 装 Caddy 根证书**）。Node 22 LTS、TS strict、node-pty ≥1.1。

## 14. 关键实现规格（补充 §5–§9 未尽事项）

- **registry**：app 不直接持端口/socket——`app → service → target` 间接；socket 名由 gen 推导 dev 端口 / prod socket 路径。
- **terminald 连接时序**：Origin 纵深校验 → 按客户端尺寸 resize → 非 alternate screen 发 `hist` → attach（grouped session）→ 每 5min introspect 复验。
- **authd 分层**：`webauthn.ts` / `sessions.ts` / `exchange.ts` / `forward-auth.ts` / `introspect.ts` / `db.ts`（手写迁移 `migrations/*.sql`，不引 ORM）。CLI：`bootstrap-user`、`invite`。
- **Caddy 生成物**：互斥 handle（保留前缀 → authd；forward_auth；reverse_proxy socket）+ 统一注入头：surface `frame-ancestors 'self' https://os.<d>`（Caddy 层注入，覆盖 code-server/Xpra 这类改不动的上游）、shell/登录页 `frame-ancestors 'none'`、保留前缀 `Referrer-Policy: no-referrer`。
- **镜像归属 per-user**：rootless 镜像存储各用户独立——authd 镜像由 `authd` 用户自建（同一 rsync 构建上下文；或 `podman image scp` 中转）；deploy.sh 用 `sudo systemctl --user -M <user>@` 编排。
- **backup**：数据卷 tar + SQLite 经 `podman exec` 容器内 `.backup`（host 保持零 Node）+ caddy/infra 配置；systemd timer 每夜；restore.sh + P7 真实演练。

## 15. 质量保障

1. **类型层**：TS strict + zod 边界（registry、协议、authd 输入）；`gen --check` 防生成物漂移。
2. **单元**（vitest，只测有逻辑处）：token/code/state/step-up 判定、流控计数、协议编解码。
3. **e2e**（Playwright 对本地全栈，**主力**）：
   - 认证：注册/登录/登出/过期重登/增登第二把 passkey/step-up 顶层流
   - terminal：echo、中文/IME、resize、Ctrl-C、断线重连、高速输出
   - 持续性：关 tab 重开（进程存活 + scrollback）、切 app 零重连、浏览器重启免认证恢复布局、双客户端 grouped 不打架
   - 安全矩阵：异 Origin WS 拒（含兄弟子域发起）、无 cookie → 302、editor cookie ≠ terminal、`__Host-` tossing 写不进、redirect 注入拒、state 不匹配拒、cross-site 触发 `/__runtime` 拒、登出后存量 WS ≤5min 收割
4. **生产**：doctor + healthz + 每夜备份 + P7 restore 演练。手动清单只剩：浏览器兼容、IME 手感、Desktop 体验。

## 16. 实施 Phases（local-first；每阶段 DoD，不过不进下一个）

| # | 内容 | DoD（摘要） |
|---|---|---|
| **P0** 骨架+本地环（Mac） | monorepo、registry+gen、本地 Caddy、shell 占位、`pnpm dev` | `https://os.runtime.test` 绿锁；`gen --check`+`pnpm check` 绿 |
| **P1** 认证纵切（Mac） | authd 全端点（state/introspect/增登）+CLI；shell 登录页；Playwright passkey 流 | 真 Touch ID 登录；认证组+安全子集 e2e 绿 |
| **P2** Terminal 纵切（Mac） | protocol+app-kit+terminald（本机 tmux，grouped）+UI+换票+流控+hist 回放+IME 手感 | 无感全功能；terminal/持续性/安全矩阵全绿 |
| **P3** 上服务器（需域名+SSH） | bootstrap（三用户/linger/subuid/admin off）；image+Quadlet+数据卷+**socket 链路**+**挂载交付**；authd 容器化；deploy.sh；DNS+TLS。唯一无法本地预演的阶段，预算 2× | 真域名 terminal 进 workspace；reboot 自愈；recreate 文件在；除 SSH 外仅 80/443；低权用户绕不过 Caddy；doctor 绿 |
| **P4** Editor（检验"现成软件接入"） | image 加 code-server（计划内重启）；registry 条目 | 同文件系统；直连不可达；流程不顺滑先修流程 |
| **P5** Host target（主 UI 第二活路，提前） | host 装 Node；host-terminald（socket）；host app（stepUp） | fresh passkey 生效；workspace cookie 无效；workspace 停机时 host 可用；idle 10min |
| **P6** Desktop（最大时间黑洞，放最后） | Xpra（xpra.org v6+html5）+XFCE+RuntimeDirectory/dbus；键鼠/clipboard/resize | 断线重连回同一桌面（窗口原样） |
| **P7** Ops 硬化+平台验证 | doctor/backup+**restore 演练**/recovery.md（含 passkey 全丢剧本）；member authz 预演；**new-app hello（含 daemon，走挂载交付）计时 ≤30min**；docs 拆分；安全清单全跑；之后才议 SSH 收紧 | 全部 DoD 清零 |

## 17. v0 验收（Definition of Done 总表；[auto]=Playwright/doctor 覆盖）

**体验与持续性**
- [ ] 一次 passkey 登录 → 全部 surface 可用，无二次认证 [auto]
- [ ] 关 tab / 刷新 / 合盖 / 断网后回来：terminal 屏幕+滚动历史恢复，tmux 里的 ssh/长进程未断 [auto]
- [ ] 浏览器整个退出重开（TTL 内）：免认证，shell 恢复关闭前 tabs/活跃 app [auto]
- [ ] shell 内切换 app 不重载不重连 [auto]
- [ ] 双客户端同开 terminal：独立视口不镜像打架 [auto]
- [ ] Terminal / Editor / Desktop 看到同一个 `/workspace` [manual]
- [ ] 每种故障状态有明确 UI（§9 表）[manual]
- [ ] workspace 停机时 host app 可用 [manual]

**平台**
- [ ] `new-app hello`（含 daemon）≤30 分钟，只触碰 apps/hello + services/hello + registry [manual 计时]
- [ ] 加/改自写 daemon 的 deploy 不杀 tmux 进程 [manual 一次]
- [ ] `gen --check` 保证 registry 与生成物一致 [auto]
- [ ] member 被 owner-only app 拒绝 [auto]

**安全**
- [ ] 异 Origin WS 全拒（含兄弟子域）；surface cookie 互不可见互不可用 [auto]
- [ ] `__Host-` tossing 写不进；state 不匹配/cross-site 触发换票 → 拒；redirect 注入 → 拒 [auto]
- [ ] 登出后：新请求立即拒，存量 WS ≤5 分钟收割 [auto]
- [ ] step-up 全部顶层完成（shell 内与直开两条路）；host app 要求 fresh passkey [auto]
- [ ] terminald / code-server / Xpra 公网直连失败；除 SSH 外仅 80/443 [doctor]
- [ ] 本机低权用户绕 Caddy 直连任一 socket → 权限拒 [doctor]
- [ ] terminal bundle 零第三方请求；CSP/frame-ancestors 白名单 [auto]
- [ ] workspace 非 host root、无 host socket/fs；compute 无 sudo [doctor]
- [ ] owner 增登第二把 passkey 流程可用 [auto]

**持久与恢复**
- [ ] 容器 recreate 文件在；host reboot 全自动恢复 [doctor+manual]
- [ ] backup → restore 实测通过 [manual 演练]

## 18. 安全 invariants（docs/invariants.md 初稿，改动不可违反）

1. Shell 只是 presentation；authz 决策全在 authd/gateway。
2. 每个 high-trust app 独立 origin + 独立 `__Host-` session cookie。
3. 单次登录靠换票（state 绑定），不靠共享 cookie。
4. postMessage 只传 presentation 与白名单导航 chord（枚举、无 payload）；永不传按键流/文本/命令/文件/凭据。
5. 浏览器输入永不进 spawn()/exec；browser 只能引用服务端注册的 id/verb（target、session 名、未来 action verbs → 固定命令）。
6. workspace runtime 可弃，user state 持久。
7. 内部服务只在 unix socket / 容器内网可达，本机其他用户也不可达；公网只有 Caddy。
8. workspace 无 host socket / filesystem / network。
9. 加 app 只触碰 `apps/<id>`（+`services/<id>`）+ registry；自写 daemon 的交付不重建容器。
10. host 管理默认带外（SSH）；web 通路必须 owner + step-up + socket 链路落地后。
11. 恢复路径独立于本系统：SSH 与网络配置永不被本系统管理。
12. shell 非单点：每个 surface 可独立直开。
13. 生成器保持哑模板；`/__runtime/*`、`/__api/*` 是保留前缀。
14. 断连/关页永不终止 runtime 侧进程；重连 = reattach，永不回放输入。
15. WebAuthn ceremony 只在顶层页面发生。
16. 日常 deploy 永不终止用户进程；image rebuild 是显式的计划内重启。

## 19. Threat model

**保护对象**：host root、SSH keys、源码与数据、API keys、终端击键、passkeys。

| 攻击路径 | 结果 |
|---|---|
| shell XSS | 拿不到任何 surface cookie；WS Origin（含兄弟子域）拒；postMessage 无 input 通道 → 不能变成 shell RCE |
| 恶意 VS Code 扩展 / workspace 恶意进程 | 上限 = workspace 执行；无 host、无他 origin 凭据、无 authd DB、无 Caddy secrets |
| 本机低权用户（compute/authd 被攻陷） | 上游全在权限受控的 socket 后：打不到 terminald / host-terminald / Caddy admin——横向提权路被封 |
| 持有账号者注入 code（会话固定） | state 绑定拒 |
| terminald 漏洞 | 就在 workspace 里，上限 = workspace 执行 |
| host app web 路径被攻破 | = `ren` 级 host；"web 里管 host"的固有代价 → owner + step-up + idle 断开 + socket 链路，SSH 保底 |

## 20. v0 非目标（明确不做，架构不堵路）

开放注册 / 多 workspace / 多 server / GPU / agent 编排 / files API / 端口预览 / 浏览器上传下载 / 移动端专门 UI / 深链 / Kubernetes / Guacamole·RDP·VNC / 自研桌面协议 / Docker-in-Docker / 共享会话 / 动态 app 注册 / billing（永不）

## 21. 未来演进（大致顺序）

1. **Agent UI**：workspace 里 agentd（列出/attach tmux 与 Claude Code session、流式输出、审批）→ shell 的 Agents app；tmux control mode（`-CC`）是现成的程序化接口；动作走 server-defined verbs（invariant #5）。app 模型已覆盖——UI + daemon + registry 条目，到时只是写。
2. 命名 tmux session 管理（多独立 terminal tab）
3. **服务端 user-state**（shell 布局跨设备；Safari localStorage 上限的根治）——优先级提前
4. Files app（workspace 文件浏览/上传下载）
5. host-admin app（metrics / systemd / journald，step-up）
6. 端口预览（workspace dev server 一键子域，补 code-server `--proxy-domain`）
7. 多 workspace（Quadlet 模板 ×N；service→target 间接层已铺好）
8. 朋友入驻（invite + 各自 workspace + access 策略）
9. 动态 app 注册（DB registry + 管理页，不重部署挂新 app）
10. 深链（`/a/:id/...` 转发给 surface）与移动端形态
11. 远景：多 dedicated server / GPU 节点 / 临时环境——"runtime → node"抽象（原方案的 personal compute fabric 远景，保留）

## 22. 待提供

1. **域名**（P3 前；自有注册域、不在 PSL）。
2. **服务器 SSH**（P3 前；确认 Ubuntu 24.04）。
3. shell 子域名字（默认 `os.`）。

---

## 附录 A：决策记录

| 日期 | 决定 |
|---|---|
| 2026-08-15 | 独立站点，dashboard 即产品（不嵌入现有网站）；单次 passkey 登录（否决双层解锁）；子域名方案 |
| 2026-08-15 | Terminal target"全都要"→ target 注册表：workspace 容器默认 + host + host-admin + 未来多 workspace |
| 2026-08-15 | 自写 backend 全 TypeScript；桌面锁定 Xpra+XFCE（KasmVNC 已评估被否）；容器内 systemd PID1 替代 supervisord |
| 2026-08-15 | 本 runtime = 与 server 交互的主 UI → host target 升 v0 核心、可靠性分层进验收 |
| 2026-08-15 | local-first 实施：P0–P2 全在 Mac（runtime.test + tls internal），P3 才上服务器 |
| 2026-08-15 | 关闭页面 ≠ 中断任何东西：进程不死 + 页面状态恢复为 v0 硬性要求 |
| 2026-08-15 | 三 agent review（安全/架构/可实现性）修订：unix socket 替代回环 TCP；WS 周期复验；换票 state 绑定；cookie 全 `__Host-`；WebAuthn 一律顶层；daemon 挂载交付不重建容器；tmux grouped session；P5/P6 对调（host 先于 desktop）；预算校准 ~3k 行 |
| 2026-08-15 | auth 子域取消：authd 并入 os 域 `/__runtime/*`（零 CORS；builtin 数据走 `/__api/*`；少一个 origin） |
| 2026-08-15 | v4：恢复被逐版压缩掉的基座内容（整体架构图、repo 树、image 清单、三 app 详设、multi-user、配置、非目标、完整 DoD），此后 PLAN.md 保持自包含 |
