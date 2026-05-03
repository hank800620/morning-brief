# 📊 Hank's Weekly Brief · 2026-05-04 (2026-W19)
**Window: 2026-04-27 06:30 → 2026-05-04 06:30 (Asia/Taipei)**

---

## 1️⃣ 🧠 Weekly Insight
**本週主旋律:** AI 平台去壟斷化——OpenAI 打破微軟獨家、擁抱 AWS $1,500 億、Q4 IPO 路線確立；DeepSeek V4-Pro MIT 開源讓 frontier 能力「公地化」；川習 5/14 北京峰會以 $1.2 兆稀土為籌碼，三條結構性力量同週匯聚，重塑 AI 硬體採購與供應鏈談判格局。

**結構性變化:** 兩件本週確定的不可逆之事：(1) OpenAI 正式解除與微軟的獨家綁定，確立 AWS 為 Frontier 企業平台「唯一第三方雲端分發合規夥伴」——AI 分發入口從壟斷走向多雲競爭，邊緣推論差異化窗口再次擴大；(2) DeepSeek V4-Pro MIT 授權完整開源且 NIST CAISI 官方評估啟動——frontier 模型能力從「付費服務」走向「公共基礎設施」，成本通縮加速。

**對你的下一步:**
- **立即（本週）:** 啟動 DeepSeek V4-Flash INT4/INT8 量化在 Dimensity 9400 上的 benchmark，MIT 授權無法律風險，比競爭對手早一週出數字就是差異化。
- **本週會議:** 把「OpenAI → AWS Frontier 合作」放入 cloud-edge roadmap，評估 MTK SoC 搭配 AWS Frontier API 的 sales narrative。
- **5/14 前:** 建立稀土供應風險矩陣——哪些 MTK 產線最依賴鎵、鍺、銻、石墨，在川習峰會前備妥 contingency 方案。

---

## 2️⃣ 🪞 上週對賬（W18 → W19）

上週週報（2026-W18，窗口 04-21 → 04-27）預測追蹤：

| 狀態 | 預測 | 本週驗證 |
|------|------|----------|
| ✅ **Confirmed** | 多雲分發加速邊緣推論需求差異化 | OpenAI 去獨家 + AWS Frontier 整合確認，Azure AI 獨家敘事終結，邊緣推論差異化窗口清晰化 |
| ✅ **Confirmed** | DeepSeek V4-Flash 量化版本驗證持續 | V4-Pro MIT 完整開源；NIST CAISI 5 月啟動官方評估，政策層面正式注意 |
| ✅ **Confirmed** | N1 SoC Computex 6/1 倒數（35 天 → 28 天） | 大量出貨確認滑至 H2 2026；Asus/Dell/Lenovo 三家 OEM 在管線；工程板在二手市場出現（$1,400） |
| ⏳ **Pending** | TSMC Q2 初步月報（5/10） | 倒數 6 天；TSMC 已預告 Q2 $39-40.2B，April 月報 5/10 發布 |
| ⏳ **Pending** | MATCH Act 正式立法時程 | 已通過 House Foreign Affairs Committee；仍待全院表決，時程未定 |

---

## 3️⃣ 🔭 本週 5 條主軸線

### 主軸 1: OpenAI 終止微軟獨家 + AWS 確立 Frontier 雲端夥伴，Q4 IPO ~$1 兆路線啟動
- **重要性:** ⭐⭐⭐⭐⭐
- **發生了什麼:** 4/27 OpenAI 與微軟重簽協議三大變動：(a) OpenAI 知識產權授權不再獨家，Microsoft 停止向 OpenAI 支付收益分成，OpenAI 向 Microsoft 的分成設總上限至 2030；(b) AWS 確認為 ChatGPT 企業平台 Frontier 的「唯一第三方雲端分發合規夥伴」，AWS 投資由 $380 億擴大至 8 年 $1,500 億；(c) OpenAI 正式啟動 Q4 2026 IPO 路線，目標估值接近 $1 兆，年化收入 $250 億已達門檻。
- **Insight:** Azure 失去獨家地位後，雲端廠商「靠 LLM 獨家差異化」的策略窗口已關閉——差異化全面轉移到 inference 效率、隱私、延遲。對 MTK：AWS Frontier 成為 OpenAI 企業入口，MTK SoC 若要搭配 ChatGPT Enterprise，AWS 合規路徑比 Azure 更重要。同時，IPO 敘事迫使 OpenAI 在 IPO 前後加速 on-device licensing 商業化——MTK NPU 合作機會窗口打開。
- **來源:** [CNBC — OpenAI-Microsoft Restructure](https://www.cnbc.com/2026/04/27/openai-microsoft-partnership-revenue-cap.html) | [TechCrunch — OpenAI Ends Microsoft Legal Peril](https://techcrunch.com/2026/04/27/openai-ends-microsoft-legal-peril-over-its-50b-amazon-deal/) | [Bloomberg — OpenAI Breaks Free](https://www.bloomberg.com/news/articles/2026-04-27/microsoft-to-stop-sharing-revenue-with-main-ai-partner-openai)

### 主軸 2: 川習北京峰會 5/14 確認，稀土 $1.2 兆籌碼 vs. 聯合貿委會框架
- **重要性:** ⭐⭐⭐⭐⭐
- **發生了什麼:** 川普 5/14-15 北京行確認（8 年來首位訪中美國總統）。籌碼格局：中方握稀土王牌（稀土相關產業佔美國 GDP 約 $1.2 兆），鎵鍺銻石墨 6 個月出口許可即將到期；美方持 Section 301 貿易調查施壓（3/12 發動）。預期產出：「聯合貿易委員會（Board of Trade）」框架、商業採購（大豆）、稀土許可 6 個月展延，不期待大協議。王毅—盧比奧電話已確認峰會如期。
- **Insight:** 本季 MTK 最大外部政策變數。若出口許可不展延（低概率但非零），MTK 上游在 Q3 面臨成本衝擊。即使峰會成功，中國也習慣用 6 個月展延維持持續施壓——替代供應鏈（澳洲、加拿大）的前置時程評估需在 5/13 前完成。峰會後 24 小時聲明是本季必追即時訊號。
- **來源:** [世界新聞網 — 習握 $1.2 兆稀土王牌](https://www.worldjournal.com/wj/story/124277/9471753) | [Foreign Policy — US-China Summit Analysis](https://foreignpolicy.com/2026/04/27/trump-xi-summit-us-china-trade-deal-taiwan-geopolitics/) | [CNA — 稀土出口管制溝通](https://www.cna.com.tw/news/acn/202604090219.aspx)

### 主軸 3: DeepSeek V4-Pro MIT 完整開源 + NIST CAISI 官方評估，frontier 能力正式「公地化」
- **重要性:** ⭐⭐⭐⭐⭐
- **發生了什麼:** DeepSeek V4-Pro（1.6T MoE 參數，49B active）MIT 授權完整開源上 Hugging Face；NIST CAISI（美國國家標準局 AI 安全中心）已於 5 月啟動 V4-Pro 評估——美國政府首次正式評估中國 frontier 開源模型。定價：V4-Flash $0.14/$0.28 per M tokens（比主流競品便宜 60-80%）。Huawei Ascend 優化已完成（1.50x-1.73x speedup on non-NVIDIA 平台）。
- **Insight:** MIT 授權 + NIST 評估雙重信號：MTK 可直接以 V4-Pro 為邊緣量化基座（INT4 量化後 ~25GB，是 2nm 旗艦 SoC 首次可支撐的尺寸）；美國政府「研究而非禁止」V4 說明開源策略穿透政策防火牆。Ascend 優化完成意味著 MTK NPU 應立即驗證兼容性，否則在中國市場「非 Ascend 平台」敘事落後。
- **來源:** [VentureBeat — DeepSeek V4 at 1/6 Cost](https://venturebeat.com/technology/deepseek-v4-arrives-with-near-state-of-the-art-intelligence-at-1-6th-the-cost-of-opus-4-7-gpt-5-5) | [NIST — CAISI Evaluation DeepSeek V4 Pro](https://www.nist.gov/news-events/news/2026/05/caisi-evaluation-deepseek-v4-pro) | [MIT Technology Review — Why DeepSeek V4 Matters](https://www.technologyreview.com/2026/04/24/1136422/why-deepseeks-v4-matters/)

### 主軸 4: TSMC 倒數 6 天月報（5/10）+ Q2 $39-40.2B 預告，AI 需求連五季創紀錄
- **重要性:** ⭐⭐⭐⭐
- **發生了什麼:** TSMC 將於 5/10 發布 4 月月報；Q1 已確認 $35.7B（+35% YoY）、淨利 +58%、連四季創紀錄；Q2 展望 $39-40.2B（+10% QoQ）。先進製程晶片佔晶圓收入 75%；全年預估 +30% YoY。TSMC 南京廠同期取得美年度出口許可，中國業務維穩。
- **Insight:** 5/10 月報是判斷「AI 晶片需求高原期是否到來」最即時指標。若 April 月報符合節奏（約 $12-13B/月），需求持續；若低於預期，可能預示川習峰會前企業暫緩採購。對 MTK：TSMC 先進製程產能飽和度直接影響 3nm/2nm Dimensity 晶圓排程，月報數字是 H2 交期談判的重要背景。
- **來源:** [CNBC — TSMC Q1 Revenue +35%](https://www.cnbc.com/2026/04/10/tsmc-q1-record-revenue-ai-chip-demand-strong.html) | [CNBC — TSMC Q1 Profit +58%](https://www.cnbc.com/2026/04/16/tsmc-q1-profit-58-percent-ai-chip-demand-strong.html) | [TSMC Investor Relations](https://investor.tsmc.com/english/monthly-revenue/2026)

### 主軸 5: NVIDIA Computex N1 SoC 倒數 28 天，大量出貨滑至 H2，MTK 品牌敘事窗口
- **重要性:** ⭐⭐⭐⭐
- **發生了什麼:** Computex 6/1 倒數 28 天，N1/N1X SoC 將在 Jensen Huang 主講環節正式揭曉：20 Arm 核心（MTK CPU IP）+ 6,144 CUDA 核心（Blackwell）+ 128GB LPDDR5X。新確認：大量出貨滑至 H2 2026，Asus/Dell/Lenovo 仍在開發；工程板已在二手市場以 $1,400 流出。
- **Insight:** N1 SoC 品牌敘事完全由 NVIDIA 掌控，MTK 的 CPU IP 授權角色如同 Arm 之於高通——有收入但無品牌溢價。「大量出貨滑至 H2」給了 MTK 6 個月窗口，在 Computex 前先建立 Dimensity 9500 的邊緣 AI 差異化敘事。建議：6/1 前完成「edge AI SoC vs AI PC SoC」定位文件，搶佔 Computex 後媒體框架。
- **來源:** [Tom's Hardware — N1 Mass Rollout Late 2026](https://www.tomshardware.com/pc-components/cpus/nvidia-and-mediateks-ai-cpu-may-not-see-mass-rollout-until-late-2026-asus-dell-and-lenovo-reportedly-developing-n1x-desktops-and-laptops) | [Igor's Lab — N1X Computex Demo](https://www.igorslab.de/en/nvidia-n1x-in-the-spotlight-at-computex-leak-points-to-2026-demo-but-only-a-late-market-launch/) | [Tweaktown — N1 Engineering Board](https://www.tweaktown.com/news/110944/nvidias-n1-soc-pictured-on-an-engineering-board-with-128gb-of-memory-for-local-ai/index.html)

---

## 4️⃣ ⚠️ 本週 2 個最重要弱訊號

### 弱訊號 1: NIST CAISI 首次官方評估中國開源模型——政策防火牆鬆動還是立法前哨？
- **為什麼你不該略過:** NIST AI 安全中心評估 DeepSeek V4-Pro，是美國政府首次正式評估中國 frontier AI 模型。雙面含義：（正面）若評估結果中立，將降低美國企業採用 V4 的合規顧慮，MIT 授權 + NIST 背書 = 開源 AI 最快進入企業採購的路徑；（負面）政府先評估、再立法是慣例——CAISI 報告可能成為後續採購禁令或 MATCH Act 新增條款的技術依據。無論哪個方向，3-6 個月政策走向決定 V4 在北美企業市場命運，也決定 MTK 在 V4 edge 版本上的投入優先度。
- **追蹤指標:** NIST CAISI 評估報告發布時程；MATCH Act 是否新增「AI 模型使用」條款；Fortune 500 法務部門對 V4 MIT 授權的合規指引
- **來源:** [NIST — CAISI DeepSeek V4 Pro](https://www.nist.gov/news-events/news/2026/05/caisi-evaluation-deepseek-v4-pro)

### 弱訊號 2: OpenAI IPO ~$1 兆估值路線確立——on-device licensing 談判在 S-1 申報前 12 個月啟動
- **為什麼你不該略過:** OpenAI Q4 IPO 目標估值 ~$1 兆，機構投資人需要看到清晰的收入擴張路徑。最快的路徑之一是 edge/on-device AI licensing（給 SoC 廠商收權利金），這直接意味著 OpenAI 在 S-1 申報前有強烈動機推進與 MTK、三星、高通的 on-device licensing 談判。Motley Fool 已在問「去獨家對微軟股東長期是否利好」，代表市場開始重新定價這段生態關係——MTK 的談判桌位因此改變，應主動接洽而非等待。
- **追蹤指標:** OpenAI S-1 申報時程（預期 Q3 2026）；OpenAI on-device licensing 首批合作公告（三星/MTK/高通任一）；Microsoft Copilot 在無獨家 OpenAI 技術後的產品策略調整
- **來源:** [Motley Fool — Microsoft-OpenAI Deal Long-term](https://www.fool.com/investing/2026/05/01/microsoft-amended-deal-openai-good-for-stock/) | [Globe and Mail — OpenAI Exclusivity Ends Ahead of IPO](https://www.theglobeandmail.com/business/international-business/us-business/article-openai-breaks-off-exclusivity-deal-with-microsoft/)

---

## 5️⃣ 🎤 Monday Talking Points + 部門策略

### Talking Point 1
> **「OpenAI 把 ChatGPT 企業後端搬到 AWS——我們的雲端 + 邊緣整合路線要跟著更新。」**

**背後的部門策略:** OpenAI Frontier 以 AWS 為唯一企業分發合規平台，意味著未來大部分 OpenAI 企業推論流量在 AWS 上。MTK 若要讓 Dimensity SoC 成為「ChatGPT on-device 的硬體基座」，應接洽 AWS Bedrock / Frontier on-device 協議，而非 Microsoft Azure AI。建議本週工程師建立 AWS Frontier API 文件分析，找出 on-device inference offload 的技術切入點。

### Talking Point 2
> **「DeepSeek V4-Pro MIT 開源了，我們 NPU 團隊這週就要開始跑 benchmark——競爭對手也在跑。」**

**背後的部門策略:** MIT 授權消除法務風險，NIST 評估代表政策曝光度升高。MTK NPU 在 V4-Flash INT4 量化的推論效率若本週出數字，可在 Computex 前形成差異化技術故事：「全球首個完整支援 DeepSeek V4 家族邊緣推論的商用 SoC」。這個敘事比等 N1 SoC 6/1 發表後再反應快一個月。

### Talking Point 3
> **「川習峰會 5/14，稀土出口許可 6 個月到期，我們需要一份供應鏈風險矩陣在 5/13 前完成。」**

**背後的部門策略:** 採購部門需在 5/13 前完成鎵、鍺、銻、石墨用量統計及澳洲、加拿大替代來源的前置時程評估。峰會成功不等於問題消失——中國習慣用 6 個月展延維持持續施壓，H2 規劃需納入此風險溢價。

### Talking Point 4 & 5
> **TP4: 「TSMC 5/10 月報是 H2 排程談判的背景數字——本週對齊 Q2 備料節奏。」**
> **TP5: 「N1 SoC 出貨滑至 H2，這 4 週是我們在 Computex 前建立 edge AI 敘事的窗口——需要一份 edge AI SoC vs AI PC SoC 定位文件在 5/25 前完成。」**

---

## 6️⃣ 📅 下週重點關注

### 📆 預定事件
- **5/10（週日）** TSMC 4 月份月報發布 — 看點：April 營收是否達 $12-13B，支撐 Q2 $39-40.2B 展望
- **5/14-15（週三~四）** 川習北京峰會 — 看點：稀土出口許可是否 6 個月展延、「聯合貿易委員會」框架細節、晶片管制鬆綁條件
- **5/20 前後** Microsoft Build 2026 — 看點：微軟在失去 OpenAI 獨家後的 Copilot/Azure AI 新策略

### 📊 下週要追的數字
- TSMC April 月報目標：~$12.5-13B（對齊 Q2 指引節奏）
- 川習峰會後 24 小時聲明：稀土出口許可展延期限 + 聯合委員會職權範圍
- N1 SoC Computex 倒數 21 天：任何 OEM 新確認或規格洩漏

### ⚠️ 可能引爆的風險
- **稀土出口許可未展延**（低概率，高衝擊）：中國若在峰會前或後不展延，鎵鍺管制立即生效，衝擊 MTK 及 TSMC H2 成本基線
- **MATCH Act 加速立法**：若在峰會前快速推進，可能引爆中方在峰會上的強硬立場，談判空間收窄
- **DeepSeek V4-Pro NIST 評估出現安全疑慮**：若 CAISI 報告發現後門，美國政府可能在 Q2 末發布採購禁令，影響開源生態整合計畫

---

## 7️⃣ 🚫 Skip Pile
- **Grok 4.3 發布**：功能更新但無架構突破，xAI 生態對 MTK 邊緣 AI 無直接影響，略過。
- **Microsoft Copilot 商業化細節**：失去 OpenAI 獨家後 Azure AI 定位待重整，等 Build 2026（5/20）再做系統性分析。
- **Intel Arc GPU 更新**：Intel 持續努力 edge AI 推論，但本週無 MTK 直接競爭敘事，略過。
- **Gemini 3.1 Flash-Lite $0.25/M 定價**：已納入上週 W18 分析，本週無新變動，跳過重複報導。
- **各大 AI 初創新融資輪**（a16z、Sequoia 等）：資金流向有趣但對 MTK H2 決策影響有限，略過。

---

*[daily](https://github.com/hank800620/morning-brief/issues?q=is%3Aissue+label%3Adaily) · [weekly](https://github.com/hank800620/morning-brief/issues?q=is%3Aissue+label%3Aweekly)*
