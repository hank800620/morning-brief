# Morning Brief Bot

每天 08:00 (台北時間) 由 **Claude Code Routine** 自動執行：搜尋過去 24 小時新聞 → 整理成 CEO 級早報 → 寄到 `hank800620@gmail.com`。

涵蓋：AI / 科技 (3 則)、科技產業 (3 則)、國際新聞 (2 則)，外加一段 Today's Insight (CEO 視角內化思考)。

---

## 架構

```
[Claude Routine — 每天 00:00 UTC = 08:00 Asia/Taipei]
        │
        ▼
[Anthropic 雲端 spawn 一個 Claude session]
        │
        ├── git clone 此 repo
        ├── Claude 用 web search 搜尋過去 24 小時新聞
        ├── Claude 依 prompt 規範寫好 brief (subject + body markdown)
        ├── pip install -r requirements.txt
        └── python morning_brief.py --subject "..." --body-file body.md
                │
                └── Gmail SMTP → hank800620@gmail.com
```

**重點：新聞搜尋與整理由 routine 內的 Claude 直接做，使用 Max 訂閱額度，不另外算 API 費用。** `morning_brief.py` 只負責收下成品再寄信，不呼叫 Anthropic API。

---

## Setup

### 1. 推到 GitHub (private repo)

```bash
cd "C:/Users/hank8/Documents/Visual Studio/morning-brief"
gh repo create morning-brief --private --source=. --remote=origin --push
```

或在網頁建 private repo 後：
```bash
git remote add origin https://github.com/<your-user>/morning-brief.git
git push -u origin main
```

### 2. 產生 Gmail App Password

1. <https://myaccount.google.com/security> → 確認 2-Step Verification 已開啟
2. <https://myaccount.google.com/apppasswords> → 建立 (App name 隨意)
3. 複製 16 碼密碼 (例如 `abcd efgh ijkl mnop`) — **只會顯示一次**

這組密碼專屬此用途，可隨時撤銷，不會洩漏你 Google 帳號真密碼。

### 3. 建立 Routine

由 Claude Code 的 `/schedule` 指令建立 (我會幫你做這步)。Routine prompt 內會嵌入：
- Gmail App Password (routine 設定僅你看得到)
- repo URL
- 完整 brief 格式規範

---

## 本地測試 (選用)

`morning_brief.py` 不再呼叫 Claude API，只負責寄信。可以餵任意 markdown 測試：

```bash
pip install -r requirements.txt
export GMAIL_USER="hank800620@gmail.com"
export GMAIL_APP_PASSWORD="abcdefghijklmnop"
export TO_EMAIL="hank800620@gmail.com"

# Dry-run
python morning_brief.py --subject "[test] hello" --dry-run <<< "# Hello\n\nThis is a test."

# 真的寄
python morning_brief.py --subject "[test] hello" <<< "# Hello\n\nThis is a test."
```

---

## 調整內容

- **新聞風格、分類、字數**：在 routine prompt 裡 (用 `/schedule update` 修改)
- **執行時間**：routine 的 cron expression (UTC)
- **寄送對象**：routine prompt 裡的 `TO_EMAIL`
- **email 樣式**：`morning_brief.py` 的 `EMAIL_CSS`

## 💰 Bounty Contribution

- **Task:** [morning-brief][daily] 2026-04-27 Google TPU 8i推論晶片交聯發科設計，MTK雙雲AI格局確立
- **Reward:** $8520
- **Source:** GitHub-Paid
- **Date:** 2026-04-27

