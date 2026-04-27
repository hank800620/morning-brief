# Claude Code Routine 為什麼不能直接寄 email 到 Gmail

> 寫於 2026-04-25。我花了 2 小時才搞清楚這件事，整理出來避免別人走同樣的冤枉路。

## TL;DR

**Claude Code Routine (claude.ai/code/routines) 跑在 Anthropic 雲端 sandbox 中，該 sandbox 的出口防火牆封鎖所有寄信協定與所有第三方 email 服務的 API**。任何「在 routine 裡寄 email」的方案 (SMTP、Resend、Brevo、SendGrid、Mailgun…) 都會失敗。**這是 Anthropic 為了防止 spam 濫用的設計，不會被開放**。

要從 routine 把資訊送到使用者信箱，**必須繞過 routine sandbox**：用 GitHub Issue (`api.github.com` 在白名單) 或在本機跑排程。

---

## 我想做的事

每天早上 8:00，自動產生科技新聞早報 + 寄到 `hank800620@gmail.com`。

希望用 Claude Max 訂閱完成 (不另付 API 費用)。

---

## 試過的方案 (時間軸)

### 方案 1：Routine + Gmail SMTP + App Password ❌

直觀做法：routine 內 Claude 寫 brief，呼叫 Python `smtplib` 透過 Gmail 的 App Password 寄信。

**Routine session 內部的測試結果**：

```
Port 465 is blocked.
Port 587 is blocked.
SMTP is blocked on all ports.
```

→ Anthropic sandbox **在 port 層級**擋掉所有 SMTP 出向。

### 方案 2：Routine + Resend HTTPS API ❌

SMTP 不行，那用 HTTPS API？Resend 是 HTTPS 服務，免費 100 封/天，看起來合理。

**Routine 內呼叫 `https://api.resend.com/emails` 結果**：

```
HTTP/2 403
x-deny-reason: host_not_allowed
Host not in allowlist
```

一開始以為是 Resend 的 IP allowlist。從本機 Windows 戳同樣 API → **200 OK**，信也寄到。所以本機 IP 通、sandbox IP 不通。原以為 Resend 把 Anthropic 雲端 IP 列黑名單。

### 方案 3：Routine + Brevo HTTPS API ❌

Brevo 對雲端 IP 比較友善，policy 上沒有預設 IP 黑名單。換 Brevo 試。

**Routine 內呼叫 `https://api.brevo.com/v3/account` 跟 `/v3/smtp/email` 兩個端點**：

```
HTTP/2 403
x-deny-reason: host_not_allowed
content-length: 21
content-type: text/plain
Host not in allowlist
```

---

## 真相：是 Anthropic sandbox 自己擋的

**Resend 跟 Brevo 回傳的 403 內容、headers、bytes 完全一樣** (連 `content-length: 21` 都一樣 — 那是 "Host not in allowlist" 21 個字元)。

兩家獨立公司不可能回傳一字不差的錯誤訊息。**這是 Anthropic 出口防火牆自己捏的 403，request 根本沒離開 Anthropic**。

換句話說：
- Brevo 沒收到我們的 request
- Resend 沒收到我們的 request
- 換 SendGrid / Mailgun / Postmark / MailerSend / AWS SES 都會被擋
- key 對不對、帳號驗證了沒、IP 在不在他們 allowlist — 通通**沒差**

**Anthropic routine sandbox 有一份「出口白名單」，所有 email 服務都不在白名單上**。

### 已知白名單上的 host (有效)

- `api.github.com` ✅ (clone repo + 開 issue + GitHub API 寫操作 — 後者要 PAT)
- `api.anthropic.com` ✅
- `pypi.org` ✅ (pip install)
- 一般 web 透過 Claude Code 內建 `WebSearch` / `WebFetch` 工具 (走 Anthropic proxy)

### 已知白名單之外 (擋)

- 所有 SMTP port (25/465/587)
- `api.resend.com`、`api.brevo.com`
- 推測同樣擋：所有第三方 email 服務 (SendGrid、Mailgun、Postmark、AWS SES、MailerSend...)
- Slack / Discord webhook 推測也被擋 (未實測)

---

## 為什麼 Anthropic 要這樣擋

**為了防止 Claude 被當大型 spam / phishing 引擎**。

想像如果 routine 能自由寄信：

- Claude 寫釣魚信寫得比人還好
- 有人建一個 routine 每分鐘寄 1000 封假銀行通知信
- 一夜之間 Anthropic 整片 IP 變成 spam 來源
- Gmail / Outlook 把 Anthropic 整片 IP 列黑名單
- 全平台所有用戶被連坐

所以 Anthropic 的政策是：**AI 自動化平台不能直接寄信，要寄信請使用者用自己的基礎設施 (本機、自己的 server、自己已驗證的 GitHub 帳號)**。

這是業界標準，不是 Anthropic 為難用戶：

| 平台 | 預設擋寄信 |
|---|---|
| AWS Lambda | ✅ 擋 port 25 (要開 ticket 申請才開) |
| Cloudflare Workers | ✅ 沒有 raw SMTP 能力 |
| Vercel Functions | ✅ 擋 SMTP |
| Netlify Functions | ✅ 擋 SMTP |
| Google Cloud Run | ✅ 預設擋 port 25 |
| **Claude Code Routine** | ✅ **擋 SMTP + 擋 email 服務 API** |

Claude 是寫信能力最強的 AI，所以 Anthropic 擋得**比一般雲端平台更徹底** — 連 HTTPS-based email API 都擋。

---

## 真正可行的路

### A. GitHub Issue 當早報通知

- routine 用 `api.github.com` (白名單) 在 repo 開新 issue
- issue title = email subject
- issue body = 完整 markdown brief (GitHub 渲染表格、emoji、連結都漂亮)
- 手機裝 GitHub App → 自動推播當通知
- 體感跟收 email 通知相似，但 markdown 渲染**比 email 更好**

需要：產一組 GitHub PAT (Personal Access Token)，貼到 routine prompt。2 分鐘。

### B. 本機 Windows 排程跑一切

- 完全不用 routine
- Windows Task Scheduler 每天 8:00 觸發
- 本機跑 `claude` CLI (用你 Max 訂閱，免費) 寫 brief
- 本機 Python `smtplib` + Gmail App Password 寄信 (本機沒防火牆問題)

需要：你的電腦每天 8:00 要開機/喚醒。

### C. Hybrid

- routine 寫 brief 到 GitHub repo (commit / issue / file)
- 本機排程定期拉 + 寄信

複雜，不推薦。

---

## 我浪費的時間 (避免別人重蹈覆轍)

| 時間 | 試的事 | 結果 |
|---|---|---|
| ~30 min | Routine + Gmail SMTP | "lost connect" → 後來才知道 SMTP 全部擋 |
| ~30 min | Routine + Resend，以為是 IP allowlist | 換新 key、改帳號 email、本機驗證能寄 → 仍 routine 擋 |
| ~20 min | 註冊 Brevo (新平台) | 跟 Resend 一字不差的 403 |
| ~10 min | 才看出兩家 403 完全相同 = Anthropic 自己擋 | 真相大白 |

**省事方法**：上面這份文件直接看完，跳過所有 email API 嘗試。

---

## 速查表

| 你想做 | 從 routine 行嗎 |
|---|---|
| 寄到 Gmail (App Password) | ❌ |
| 寄到任何信箱 (Resend/Brevo/SendGrid/Mailgun/Postmark) | ❌ |
| 寄 Slack 通知 (webhook) | ❌ 推測 (未實測) |
| 寄 Discord 通知 (webhook) | ❌ 推測 (未實測) |
| 開 GitHub Issue | ✅ |
| 推送 GitHub commit (用 PAT) | ✅ 應該可以 (用 git via HTTPS to api.github.com) |
| 建 GitHub Release | ✅ |
| 寄 Telegram bot | ⚠️ 未實測，可能擋 |
| 從 routine 呼叫 Anthropic API | ✅ (但會收費，違背使用 Max 額度的初衷) |

**結論**：要從 routine 把產出送到使用者，最可靠的通道是 GitHub。其他都假定不通。

---

## 給 Anthropic 的建議

把這個 policy 寫進 `/schedule` skill 的官方文件第一段，會省下大量用戶的時間 + 客服成本。
