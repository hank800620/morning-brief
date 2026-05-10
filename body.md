# 📊 Hank's Weekly Brief · 2026-05-11 (2026-W20)
**Window: 2026-05-04 06:30 → 2026-05-11 06:30 (Asia/Taipei)**

---

## 1️⃣ 🧠 Weekly Insight
**本週主旋律:** 三力匯聚前夕——川習峰會最後 72 小時（稀土⇔晶片籌碼雙向鎖定、伊朗議題搶鏡）、TSMC 4 月月報確認 AI 需求連五季無高原（$13.08B, +17.5% YoY）、MTK Q1 確認雙 ASIC 路線（Q4 $2B + Google TPU 客製第二項目設計中）。Claude Opus 4.7 + Google I/O 前夕 Gemini 4 同週加入，AI 模型迭代週期從「季更」進化為「月更」。本週是 2026 H1 政策-商業決策密度最高的一週。

**結構性變化:**
- **MTK 雙 ASIC 路線確立（不可逆）：** Q1 法說確認第一 ASIC（美超大規模客戶）Q4 $2B 在軌，第二 ASIC（Google TPU 客製）設計中、2027 年底量產——AI ASIC 業務從單客戶走向多客戶平台戰略，估值基礎已轉換為「多年期業績股」。
- **TSMC 4 月月報排除高原論：** 4 月通常是 TSMC 最弱月（Q2 首月），仍維持 +17.5% YoY，說明 AI 訂單持續填補季節性空缺，Q2 $39–40.2B 達成路線無懸念。

**對你的下一步:**
- **5/15 峰會後 24 小時內：** 召開稀土三情境（A=快速鬆綁/B=6 個月展延/C=緊縮）緊急更新會議，根據峰會聲明調整概率分佈——伊朗插隊使 Scenario B 概率暫升至 65%。
- **本週：** Google TPU 第二 ASIC 項目確認——哪個設計團隊對接？Q2 資源是否已反映？峰會前確認內部進度。
- **Computex 前（5/25）：** 完成「MTK edge AI SoC vs N1 AI PC SoC」定位文件，搶媒體框架先機。

---

## 2️⃣ 🪞 上週對賬（W19 → W20）

上週週報（2026-W19，窗口 05-04 06:30 → 05-11 06:30）預測追蹤：

| 狀態 | 預測 | 本週驗證 |
|------|------|----------|
| ✅ **Confirmed** | TSMC 5/10 月報發布，判斷 AI 需求高原期 | 5/8 提前發布，April $13.08B (+17.5% YoY)，無高原；Q2 $39–40.2B 達成路線清晰 |
| ✅ **Confirmed** | N1 SoC Computex 倒數繼續 | 倒數 21 天（6/1），無重大出貨時程更新，媒體敘事仍由 NVIDIA 主導 |
| ✅ **Confirmed** | MTK on-device licensing 談判窗口打開 | Q1 法說確認 Google TPU 第二 ASIC 項目 + OpenAI 手機雙 NPU 架構曝光，on-device AI 多路並進 |
| ⏳ **Pending** | MATCH Act 全院表決時程 | 仍待排程，本週無新動態 |
| ⏳ **Pending** | NIST CAISI DeepSeek V4-Pro 評估報告 | 評估進行中，尚未發布，繼續追蹤 |

---

## 3️⃣ 🔭 本週 5 條主軸線

### 主軸 1: 川習峰會最後 72 小時——伊朗搶鏡，稀土/晶片底牌雙向鎖定
- **重要性:** ⭐⭐⭐⭐⭐
- **發生了什麼:** 5/14–15 北京峰會確認倒數，本週最新動態：(1) CNBC (5/8)：伊朗戰事議題預計佔據大量峰會議程，稀土/關稅談判窗口被壓縮；(2) 聯合新聞網引述分析：中方保留稀土出口底牌，美方保留晶片出口管制底牌，不期待重大讓步；(3) Board of Trade 框架 + 農業採購（大豆/波音）仍是最可能落地的具體產出；(4) 台灣、AI 技術管制、芬太尼並列議題，峰會議程高度複雜。
- **Insight:** 伊朗插隊意味著稀土/晶片議題可能從「主菜」降格為「甜點」——Board of Trade 框架若在峰會後數週才落地細節，MTK 稀土供應風險窗口延長，但「底牌鎖定」也意味著中方不會在峰會上主動升級管制（以保留籌碼），短期最糟情境（立即全面禁止）概率下降。對 MTK：峰會後 24 小時聯合聲明是稀土情境判斷的最重要即時訊號，若無稀土鬆綁細節，請把 Scenario B（6 個月展延）概率從 55% 調升至 65%。
- **來源:** [CNBC — Iran focus may delay rare earth progress](https://www.cnbc.com/2026/05/08/iran-focus-at-trump-xi-summit-may-delay-progress-on-tariffs-rare-earths.html) | [聯合新聞網 — 川習會各取所需保留底牌](https://udn.com/news/story/124870/9494098) | [China Briefing — Summit outcomes](https://www.china-briefing.com/news/trump-xi-meeting-outcomes-and-implications/)

### 主軸 2: TSMC 4 月月報 $13.08B +17.5% YoY，AI 需求連五季確認無高原
- **重要性:** ⭐⭐⭐⭐⭐
- **發生了什麼:** TSMC 5/8 提前發布 4 月月報，April 合併收入約 $13.08B USD（YoY +17.5%、MoM -1.1%）；前四月累計 YTD +29.9% YoY（NTD 1,544.83B）。Q2 指引 $39–40.2B 維持，全年 +30% YoY 展望不變。Digitimes 分析：「2026 年前四個月收入因 AI 熱潮激增 30%」。
- **Insight:** 4 月是 TSMC 歷史上季節性最弱月（Q2 首月），仍維持 +17.5% YoY 說明 AI 訂單填補了季節性空缺，高原論可排除。對 MTK：H2 Dimensity 9400/9500 3nm 產能排程談判底氣充足，TSMC 客戶優先序在 AI 飽和下更清晰，建議在 5/14 峰會前鎖定 H2 wafer 排程；4 月月報同時確認 Q2 $39–40.2B 第一個月已完成 1/3，路線無懸念，H2 估值邏輯穩固。
- **來源:** [TSMC April 2026 Revenue Report](https://pr.tsmc.com/english/news/3305) | [Digitimes — TSMC 2026 surges 30%](https://www.digitimes.com/news/a20260508VL206/tsmc-revenue-2026-nyse-growth.html) | [Yahoo Finance — TSMC strong April growth](https://finance.yahoo.com/sectors/technology/articles/tsmc-posts-strong-april-revenue-100149186.html)

### 主軸 3: MTK Q1 業績——雙 ASIC 路線確立，OpenAI 手機雙 NPU 架構曝光
- **重要性:** ⭐⭐⭐⭐⭐
- **發生了什麼:** MTK Q1 FY2026 法說要點：(1) AI ASIC 第一項目（美超大規模雲端客戶）on schedule，Q4 2026 貢獻 $2B 收入；(2) **第二個 AI ASIC 項目（Google TPU 客製化）設計中，目標 2027 年底量產**；(3) Smart Edge 部門 +13% YoY，逐漸取代手機（-15% YoY）為主要成長引擎。Q1 整體收入 NT$149.2B，略勝市場預期。OpenAI 手機新細節：郭明錤確認雙 NPU 架構（AI 算力分層）、LPDDR6 + UFS 5.0、pKVM + inline hashing 安全設計，目標 2027H1 量產，出貨目標 3,000 萬支（兩年）。
- **Insight:** 「Google TPU 第二個 ASIC 項目設計中」是本週最低調但最重要的 MTK 新聞——AI ASIC 業務從單客戶走向多客戶平台，2027 以後 ASIC 年收入可能從 $2B 擴展至 $5B+。OpenAI 手機雙 NPU 架構意味著下一代 NPU 設計需對齊「算力分層 + 持久上下文管理 + 多模態即時推論」，不只是單純提升 TOPS 數字。對你：確認負責 Google TPU 第二項目的設計團隊，Q2 資源分配是否已反映；並用 OpenAI 選 MTK 超高通的事實作為 B2B/B2G 推廣的外部背書。
- **來源:** [Futurum — MTK Q1 FY2026 Earnings](https://futurumgroup.com/insights/mediatek-q1-fy-2026-earnings-driven-by-ai-asic-ramp-visibility/) | [電腦王阿達 — 郭明錤 OpenAI 手機分析](https://www.koc.com.tw/archives/641727) | [Gizmochina — OpenAI phone Dimensity 9600 N2P](https://www.gizmochina.com/2026/05/05/open-ai-phone-chipset-launch-timeframe/)

### 主軸 4: Claude Opus 4.7 發布 + Google I/O 前夕 Gemini 4，AI 模型迭代進入「月更」時代
- **重要性:** ⭐⭐⭐⭐
- **發生了什麼:** (1) Anthropic 發布 Claude Opus 4.7：進階軟體工程能力提升（最難任務顯著進步），視覺解析力大幅提高；Anthropic 與 SpaceX Colossus 1 數據中心達成協議，Claude Code 5 小時使用限制翻倍；(2) Google I/O 前夕（預計 5/13–14），PCWorld 報導 Gemini 4 預計整合圖像/影片生成能力、走出 chatbox 走向 Agent 執行模式；(3) GPT-5.5 Instant（幻覺率降 52.5%）本週持續推送為 ChatGPT 全球預設——三大 frontier AI 廠在 5 月同步更新主力版本。
- **Insight:** AI 模型能力周期從「季更」進化為「月更」，on-device AI 的能力差距（vs 雲端 frontier）正以月為單位縮小。對 MTK：Google I/O Gemini 4 若開放 edge deployment API，將是 MTK-Google 技術合作（第二個 ASIC 項目）的直接技術對齊信號，需在 I/O 後 48 小時內評估；Claude Opus 4.7 的視覺解析提升同時意味著多模態邊緣推論的需求端規格正在快速提升，NPU 路線圖需要對應更新。
- **來源:** [Anthropic — Claude Opus 4.7](https://www.anthropic.com/news/claude-opus-4-7) | [PCWorld — Gemini leaps out of chatbox at Google I/O](https://www.pcworld.com/article/3134059/gemini-may-finally-leap-out-of-the-chatbox-at-google-i-o.html)

### 主軸 5: Computex 倒數 21 天——N1 SoC 亮相前 MTK 定位先機窗口
- **重要性:** ⭐⭐⭐⭐
- **發生了什麼:** Computex 6/1 倒數 21 天，Jensen Huang 主講環節確認揭曉 N1/N1X（20 Arm 核心 + 6,144 CUDA Blackwell + 128GB LPDDR5X）。本週無 N1 新規格洩露，但 N1 大量出貨仍滑至 H2 2026，Asus/Dell/Lenovo 在工程板階段。MTK 方面：OpenAI AI Agent 手機天璣 9600 客製版確認，強化「on-device Agent」敘事素材。
- **Insight:** N1 SoC 在 Computex 亮相後媒體敘事將被 NVIDIA 主導 1–2 週，MTK 有 21 天窗口先發聲。最強定位論述：Dimensity 9500 + OpenAI Agent 手機 = 「真正 on-device AI Agent」（持久上下文 + 相機感測器整合 + 手機形態 + 隱私），而 N1 AI PC SoC 無法進入手機形態——這是不重疊的差異化，而非正面對抗。建議 5/25 前完成定位文件，Computex 後立即對媒體推送 MTK 視角。
- **來源:** [Tom's Hardware — N1 mass rollout H2 2026](https://www.tomshardware.com/pc-components/cpus/nvidia-and-mediateks-ai-cpu-may-not-see-mass-rollout-until-late-2026-asus-dell-and-lenovo-reportedly-developing-n1x-desktops-and-laptops) | [TechNews — OpenAI AI Agent Phone MTK](https://technews.tw/2026/05/05/openai-ai-agent-phone/)

---

## 4️⃣ ⚠️ 本週 2 個最重要弱訊號

### 弱訊號 1: Google I/O Gemini 4 走出 chatbox 成 Agent——MTK-Google ASIC 第二項目技術對齊節點
- **為什麼你不該略過:** Google I/O (5/13–14) 預計推出 Gemini 4 整合圖像/影片生成並走向 Agent 執行模式，同一週 MTK 確認第二 ASIC 項目為 Google TPU 客製化。這不是巧合——Google 在 Agent inference 效率需求上的升級，將直接定義 MTK 第二 ASIC 項目的 workload 規格。若 Gemini 4 在 I/O 開放 on-device 或 edge inference API，MTK 第二 ASIC 的設計週期需立即對齊，否則 Qualcomm AI Hub 可能率先接入，MTK 失去先佔優勢。這是個「只有一次」的技術路線對齊機會窗口。
- **追蹤指標:** Google I/O Gemini 4 是否公布 edge deployment API 路線圖；MTK 第二 ASIC 量產時程（目前 2027 年底）是否在 I/O 後更新；Google Cloud Next 2026 TPU v6 相關公告時程
- **來源:** [PCWorld — Gemini at Google I/O](https://www.pcworld.com/article/3134059/gemini-may-finally-leap-out-of-the-chatbox-at-google-i-o.html) | [Futurum — MTK Q1](https://futurumgroup.com/insights/mediatek-q1-fy-2026-earnings-driven-by-ai-asic-ramp-visibility/)

### 弱訊號 2: 川習峰會後中國或扮演美伊中介——閃電停火對亞洲製造業毛利率的雙向非對稱衝擊
- **為什麼你不該略過:** CNBC 報導伊朗議題主導峰會議程，背後潛台詞：中國可能以「促成美伊停火」換取美國在稀土/台灣上的讓步。若停火成真，Brent 可能從 $101 急速回落至 $85–90，帶動亞洲製造業利潤率反彈（能源佔半導體製造成本約 8–12%）；反之若談判破裂，$110+ 持續，TSMC H2 wafer 報價重談壓力上升。這是雙向非對稱風險：正向（停火）→ MTK H2 毛利率改善約 1–2%；負向（油價飆升）→ TSMC 成本壓力轉嫁，每塊 wafer 成本上升 5–8%。峰會後週一油價走向是最快的市場驗證訊號。
- **追蹤指標:** 5/15 峰會後美伊談判媒體報導；Brent 5/16 週一開盤走向；TSMC H2 wafer 報價是否在 5–6 月出現調整
- **來源:** [CNBC — Iran focus at Trump-Xi summit](https://www.cnbc.com/2026/05/08/iran-focus-at-trump-xi-summit-may-delay-progress-on-tariffs-rare-earths.html) | [CNA — 美財長稀土大豆待川習定案](https://www.cna.com.tw/news/aopl/202510270011.aspx)

---

## 5️⃣ 🎤 Monday Talking Points + 部門策略

### Talking Point 1
> 「TSMC 4 月月報 $13.08B、YoY +17.5%，AI 晶片需求連五季無高原。這代表台積電 3nm/2nm 產能持續緊張——我們 H2 Dimensity 晶圓排程要在 5/14 峰會結果確認前先鎖定，不能等到稀土情境清晰再動作。」

**背後的部門策略:** 晶圓排程的確定性即競爭力，在 AI 需求飽和的市場中，鎖定排程的時機比議價更重要。現在談比 6/1 Computex 後談便宜且有把握。

### Talking Point 2
> 「MTK Q1 法說確認：第一個 ASIC（超大規模客戶）Q4 $2B 在軌，第二個 ASIC（Google TPU 客製）已啟動設計、2027 年底量產。我們的 AI ASIC 業務正式從單客戶走向多客戶平台——這是估值重構的業績基礎，也是本季最優先的跨組協作事項。」

**背後的部門策略:** Q2 應立即確認 Google TPU 第二項目的設計資源配置，避免因 Computex 和峰會期間的外部雜訊而延遲內部決策。

### Talking Point 3
> 「郭明錤確認 OpenAI AI Agent 手機選定天璣 9600 客製版（雙 NPU 架構），目標 2027H1 量產、兩年 3,000 萬支出貨。這是 MTK NPU 能力最強的外部背書，B2B/B2G 推廣中可直接引用。同時也意味著下一代 NPU 規格需對齊 Agent 需求：算力分層、持久上下文管理、多模態即時推論。」

**背後的部門策略:** OpenAI 手機訂單是 NPU 路線圖的設計錨點，應在 Q2 內完成「Agent-first NPU」需求文件，避免 2028 節點設計時再返工。

### Talking Points 4–5

**TP4 — Google I/O 後 48 小時技術評估:**
> 「Google I/O (5/13–14) 預計揭曉 Gemini 4 Agent 模式，我們的 Google TPU 第二 ASIC 項目的 workload 規格可能在 I/O 後需要更新。請在 5/15（川習峰會同天）把 I/O 技術評估結果送到我這裡，讓我同步判斷兩個重大事件的交互影響。」

**TP5 — Computex 21 天倒數定位先機:**
> 「N1 SoC 在 Computex 亮相後，NVIDIA 會主導媒體敘事 1–2 週。MTK 應在 6/1 前發布『Edge AI SoC vs AI PC SoC』差異化觀點——N1 無法裝進手機，Dimensity 9500 + OpenAI Agent 手機才能做到真正 on-device AI Agent，這是不重疊的定位，而非正面競爭。」

---

## 6️⃣ 📅 下週重點關注

### 📆 預定事件

- **5/13–14** Google I/O — 看點：Gemini 4 發布規格（Agent 模式/edge API）、Gemini 4 vs GPT-5.5 Instant benchmark 數字、Google-MTK 技術合作是否有新公告
- **5/14–15** 川習北京峰會 — 看點：峰會後 24 小時聯合聲明稀土段落、Board of Trade 框架細節、伊朗議題是否佔據全部議程導致稀土/晶片推後
- **Computex 倒數 21→14 天** — 看點：N1/N1X 最終規格確認、Jensen Huang 演講預告素材、Asus/Dell/Lenovo N1X 產品線時程更新

### 📊 下週要追的數字

- 川習峰會後聯合聲明/各自公報中稀土/晶片出口相關段落
- Google I/O Gemini 4 benchmark（vs GPT-5.5 Instant 幻覺率/推論速度）
- Brent 原油 5/16 週一開盤價（峰會後第一個交易日，美伊談判信號）
- MTK 股價 5/15 收盤後市場反應（ASIC $2B 路線確認 + 峰會結果組合效應）

### ⚠️ 可能引爆的風險

- 伊朗議題完全主導川習峰會，稀土/晶片談判推後至 6 月，MTK 供應鏈不確定性窗口延長 4–6 週
- Google I/O Gemini 4 開放 edge deployment API，Qualcomm AI Hub 率先接入，MTK 落後反應喪失技術對齊先機
- 美伊談判峰會後破裂，Brent 衝破 $110，TSMC H2 wafer 報價重談壓力上升，壓縮 MTK H2 毛利率預估

---

## 7️⃣ 🚫 Skip Pile

- **Grok 4.3 OCI 上線:** 多雲 AI 部署成熟度確認——上週 daily 已完整分析，本週無新增結構性信號，跳過。
- **BILL/Upwork 裁員案例:** AI 替代白領個案——上週 daily 已追蹤，屬上升趨勢的延續案例，無新框架，跳過。
- **MATCH Act 全院表決:** 仍待全院排程，本週零新動態——等正式排程後追蹤。
- **Anthropic SpaceX Colossus 1 協議:** Claude Code 用量翻倍的算力背景——對 MTK 業務無直接影響，跳過。
- **NIST CAISI DeepSeek V4-Pro 中期更新:** 評估進行中，尚無新報告——等結果出爐後一次性分析。

---

*[daily](https://github.com/hank800620/morning-brief/issues?q=is%3Aissue+label%3Adaily) · [weekly](https://github.com/hank800620/morning-brief/issues?q=is%3Aissue+label%3Aweekly)*
