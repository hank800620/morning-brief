# Morning Brief Bot

每天 08:00 (台北時間) 由 **Claude Routine** 自動執行：搜尋過去 24 小時新聞 → 整理成 CEO 級早報 → 開成 GitHub Issue。

涵蓋：AI / 科技 (3 則)、科技產業 (3 則)、國際新聞 (2 則)，外加一段 Today's Insight (CEO 視角內化思考)。

GitHub 會在 issue 建立時自動寄通知信到你 watcher 信箱，所以體感跟收 email 一樣，但 markdown 渲染更好，且 routine 不需要任何寄信權限。

---

## 架構

```
[Claude Routine — 每天 00:00 UTC = 08:00 Asia/Taipei]
        │
        ▼
[Anthropic 雲端 spawn 一個 Claude session]
        │
        ├── git clone 此 repo (用 PAT)
        ├── 用 web search 搜尋過去 24 小時新聞
        ├── 依 prompt 規範寫好 brief (subject + body markdown)
        ├── (可選) python morning_brief.py --fetch-recent --label daily   # 拉前幾期作為跨期記憶
        └── python morning_brief.py --subject "..." --body-file body.md --label daily
                │
                └── POST api.github.com/repos/<repo>/issues
                        │
                        └── GitHub 自動 email 通知 → hank800620@gmail.com
```

**重點：新聞搜尋與整理由 routine 內的 Claude 直接做，使用 Max 訂閱額度，不另外算 API 費用。** `morning_brief.py` 只負責收下成品再開 issue，不呼叫 Anthropic API。

**為什麼不用 email**：Anthropic routine sandbox 的出口防火牆封鎖所有 SMTP port 與所有第三方 email API。`api.github.com` 在白名單，所以走 GitHub Issue。

---

## `morning_brief.py` 用法

```bash
# 開新 issue (一般情況)
python morning_brief.py --subject "[morning-brief][daily] 2026-05-09 ..." \
                       --body-file body.md \
                       --label daily

# 預覽不送出
python morning_brief.py --subject "..." --body-file body.md --label daily --dry-run

# 拉最近 N 期 issues 作為跨期記憶 (供 routine 內 Claude 讀)
python morning_brief.py --fetch-recent --label daily --limit 7
```

**Flags**：
- `--subject`：issue 標題（必填，除非 `--fetch-recent`）
- `--body-file`：markdown 檔案路徑（不給則從 stdin 讀）
- `--label`：可重複，標 issue 用。建議用 `daily` / `weekly` / `monthly`
- `--dry-run`：只印出，不 POST
- `--fetch-recent`：印出最近 N 期同 label 的 issues 內容（給 routine 跨期記憶用）
- `--limit`：搭配 `--fetch-recent`，預設 7

**環境變數**：
- `GITHUB_TOKEN`（必填）— PAT，需要 `Contents: read` + `Issues: write`。如果 repo 是 private 還必須有 read。
- `GITHUB_REPO`（選填）— `owner/repo` 格式，預設 `hank800620/morning-brief`

---

## Setup（如果要從零再建一次）

### 1. 產 GitHub PAT

到 <https://github.com/settings/tokens?type=beta> 建一個 fine-grained PAT，repo 範圍只勾此 repo，permission：
- `Contents: Read`
- `Issues: Read and Write`

### 2. 建立 Routine

由 Claude Code 的 `/schedule` 指令建立。Routine prompt 內會嵌入：
- GitHub PAT（routine 設定僅你看得到）
- repo URL
- 完整 brief 格式規範

---

## 本地測試

`morning_brief.py` 是 stdlib-only，不用裝套件：

```bash
export GITHUB_TOKEN="ghp_xxx..."
export GITHUB_REPO="hank800620/morning-brief"

# Dry-run
python morning_brief.py --subject "[test] hello" --label daily --dry-run <<< "# Hello"

# 真的開 issue
python morning_brief.py --subject "[test] hello" --label daily <<< "# Hello"
```

---

## 調整內容

- **新聞風格、分類、字數**：在 routine prompt 裡（用 `/schedule update` 修改）
- **執行時間**：routine 的 cron expression（UTC）
- **目標 repo**：routine prompt 裡的 `GITHUB_REPO`
