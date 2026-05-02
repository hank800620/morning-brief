# ☀️ Hank's Morning Brief · 2026-05-03 (週日)
**Window: 2026-05-02 07:00 → 2026-05-03 07:00 (Asia/Taipei)**

## ⚡ 30-Second TLDR
- DeepSeek V4-Pro 以 MIT 授權開源（1.6 兆參數），聲稱超越 GPT-5.2 與 Gemini 3.0，低成本 AI 模型競爭進入新一輪通縮循環。
- OpenAI 終止微軟獨家協議、轉向 AWS+Google 雙雲，$250 億年化收入支撐 IPO 路線圖，AI 平台壟斷格局開始碎片化。
- 川普北京行倒數 11 天，王毅—盧比奧電話確認峰會如期，稀土「聯合貿易委員會」框架浮現，是本季 MTK 最大外部政策變數。

---

## 🧠 Today's Insight
**本日摘要重點:** DeepSeek V4 開源（成本通縮）+ OpenAI 去獨家（平台碎片化）+ Gemini 3.1 Ultra 2M context 三件事同時發生，AI 模型市場在一週內重新洗牌：成本持續向零，「誰控制分發入口」取代「誰有最強模型」成為新戰場。
**未來發展方向:** 模型成本趨零之後，算力效率、設備端控制與應用生態黏著度是下一場競賽；OpenAI 多雲化意味著「推論就近發生」壓力增大，edge AI SoC 差異化邏輯獲得平台結構支撐。峰會後稀土+晶片管制框架將在 5/15 後 24 小時內重塑 AI 硬體供應鏈談判格局。
**對你的意義:** DeepSeek V4 MIT 授權提供了免費量化基座——V4-Pro 49B active params 經 INT4 量化後約需 25GB，已是旗艦 SoC 可支撐尺寸，MTK 現在就應啟動 V4 邊緣量化 benchmark；OpenAI-AWS 整合意味著 ChatGPT 後端轉移，MTK 合作談判需同步評估 AWS Frontier 對接路徑。

---

## 1️⃣ 🤖 AI / 科技

### ① ⭐⭐⭐⭐⭐ DeepSeek V4-Pro 開源發布：MIT 授權 + 1.6 兆參數，聲稱超越 GPT-5.2 【⭐連續追蹤】
**摘要:** DeepSeek 於 4 月 24 日發布 V4 Preview，兩版本：V4-Pro（1.6 兆參數、49B active，MIT 授權）與 V4-Flash（284B 參數、13B active）。V4-Pro-Max 在部分推理基準聲稱超越 OpenAI GPT-5.2 和 Gemini 3.0 Pro；V4-Flash 定價 $0.14/$0.28 per M tokens，比主流競品便宜 60-80%。同時針對 Huawei Ascend 950 完整優化，中國算力閉環加速。全球開發者已開始以 V4 + GPT-5.5 + Claude Opus 4.7 組合構建 Multi-model routing 架構。
**Insight:** MIT 授權意味著 MTK 可直接以 V4 為邊緣量化基座，無授權風險。V4-Pro 49B active params 在 INT4 量化後約需 ~25GB，是 2nm 旗艦 SoC 首次能支撐的尺寸門檻——邊緣部署可行性從概念進入具體 benchmark 競賽。中國市場方面，V4 讓應用開發者完整繞開 OpenAI/Anthropic，MTK edge AI SoC 中國需求將因此加速，但 Huawei Ascend 整合仍是首要競爭壓力。
🔗 [TechCrunch](https://techcrunch.com/2026/04/24/deepseek-previews-new-ai-model-that-closes-the-gap-with-frontier-models/) | [AI Leaderboard](https://www.buildfastwithai.com/blogs/best-ai-models-may-2026-leaderboard)

### ② ⭐⭐⭐⭐ OpenAI 終止 Microsoft 獨家協議、IPO 路線圖啟動，AI 平台進入多雲分發時代
**摘要:** 4 月 27 日，OpenAI 與 Microsoft 宣布終止獨家授權條款，授權改為非獨家至 2032 年，Microsoft 無需繼續支付收益分成；OpenAI 可同時服務 AWS、Google Cloud。背景：Amazon 2 月已承諾 $500 億投資，AWS 成為 OpenAI Frontier agent 平台獨家基礎設施。OpenAI 年化收入突破 $250 億，Anthropic 接近 $190 億，OpenAI IPO 預計 2026 年底前。
**Insight:** OpenAI 從「微軟獨家」轉向「多雲分發」標誌著 AI 平台去中心化加速，ChatGPT 在終端的入口優勢可能被「設備端 AI + 就近雲端推論」取代。MTK 的機會：確保下一代旗艦 SoC 能無縫對接 OpenAI Frontier（AWS 後端）+ Anthropic（Google Cloud 後端），避免被綁定任何單一雲商，與平台碎片化趨勢完全一致，是絕佳談判窗口。
🔗 [BNN Bloomberg](https://www.bnnbloomberg.ca/business/artificial-intelligence/2026/04/27/microsoft-will-no-longer-have-exclusive-access-to-openais-technology/) | [Axios](https://www.axios.com/2026/04/28/openai-microsoft-cloud-amazon)

### ③ ⭐⭐⭐⭐ Google Gemini 3.1 Ultra：200 萬 Token Context + 沙盒程式碼執行，Flash-Lite 速度提升 2.5 倍
**摘要:** Google 發布 Gemini 3.1 Ultra（200 萬 token context window，原生跨文字/圖片/音訊/影片），加入沙盒程式碼執行（模型可中途寫程式、執行、測試並回傳結果）；Gemini 3.1 Flash-Lite 速度提升 2.5 倍、輸出快 45%，定價 $0.25/M input tokens。Gemini 3.1 Pro（2 月上線）在 GPQA Diamond 科學推理達 94.3%，ARC-AGI-2 達 77.1%。
**Insight:** 200 萬 token context 讓「整個程式碼倉庫 + 所有 API 文件」一次入 context，對企業 DevOps Agent（code review、legacy migration）是破局性能力。Flash-Lite 主動壓縮 AI API 毛利、搶佔開發者 default model 位置，意味著 on-device AI 必須在延遲和隱私兩個維度有清晰差異化，否則開發者選 $0.25/M 雲端 API 的理由更充分——邊緣 AI 的護城河必須更深。
🔗 [Google Blog](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-pro/) | [LLM Stats](https://llm-stats.com/llm-updates)

---

## 2️⃣ 🏭 科技產業

### ④ ⭐⭐⭐⭐ HBM4 16Hi 上半年量產，記憶體通膨（Memflation）從資料中心蔓延至消費端
**摘要:** SK Hynix 與 Samsung HBM4（16 層，2TB/s 帶寬，較 HBM3e 提升 1.5 倍）確認 2026 上半年進入量產，NVIDIA B200/H200 系列為主要出口。同步，「Memflation」從 AI 資料中心蔓延至消費端：手機和 PC BOM 成本因 DRAM/NAND 漲價上升 5-12%，中低端 SoC 廠商毛利受壓。Deloitte 報告指出記憶體漲價將持續至 2026 全年，僅下半年略為緩解。
**Insight:** Memflation 對 MTK 的即期影響是中低端 SoC 線（Dimensity 6000/7000 系列）出貨量壓力——手機廠商縮減記憶體規格或延遲升級，將推遲中端換機潮。反向邏輯：HBM4 量產帶來的伺服器 AI 性能躍升，進一步放大雲端 vs. 邊緣推論效能差距，MTK 旗艦 edge SoC 需積極追趕，維持「邊緣效率優於雲端 API」的差異化論點可信度。
🔗 [Deloitte Semiconductor Outlook](https://www.deloitte.com/us/en/insights/industry/technology/technology-media-telecom-outlooks/semiconductor-industry-outlook.html) | [Yahoo Finance](https://finance.yahoo.com/sectors/technology/article/semiconductor-industry-revenue-to-hit-13-trillion-in-2026-as-memory-crunch-hits-consumers-151202545.html)

### ⑤ ⭐⭐⭐⭐⭐ 川習峰會倒數 11 天：王毅—盧比奧通話確認，稀土「聯合貿易委員會」框架浮現 【⭐連續追蹤】
**摘要:** 5 月 1 日，外長王毅與國務卿盧比奧通話，確認 5 月 14-15 日北京峰會如期。美貿易代表格里爾強調目標是「穩定」非重置；巴黎通道已建立稀土供應 + 聯合貿易委員會（Board of Trade）框架輪廓。台灣、晶片出口管制預計無法達成實質協議，但貿易 / 投資框架有望有具體落地。媒體報導峰會安保安排含「防投毒與防幕僚爭執」，雙方不信任基礎依舊。
**Insight:** 稀土「聯合貿易委員會」若峰會後正式宣布，將是美中供應鏈最重要制度性安排之一——MTK 在稀土（封裝材料）和算力出口管制兩個面向均直接受影響。5/14 是本季最大外部觀測節點：建議 MTK 內部在峰會前完成情境規劃（正面：管制大幅鬆綁；負面：台灣議題升溫，TSMC 供應鏈不確定性上升）。峰會結果將在 24-48 小時內影響 TSMC 股價與中國 AI 算力採購意願。
🔗 [UPI](https://www.upi.com/Top_News/World-News/2026/05/01/us-diplomatic-trade-officials-held-calls/2531777685144/) | [SCMP](https://www.scmp.com/news/china/diplomacy/article/3352220/china-trip-will-go-ahead-planned-and-it-will-be-amazing-trump-insists) | [The Diplomat](https://thediplomat.com/2026/05/the-real-role-of-a-trump-xi-meeting/)

### ⑥ ⭐⭐⭐ Glass4Chips Summit（5/14-15）：玻璃基板取代有機基板，美國押注下一代 AI 封裝主導權
**摘要:** 美國首屆 Glass4Chips Summit 將於 5 月 14-15 日在紐約 Albany 召開（FuzeHub + SEMI + IEEE 主辦），聚焦玻璃基板（Glass Substrate）取代傳統有機基板的技術路徑：更高耐熱性、更低信號損耗，適合 AI/6G/量子晶片。Intel 已投資 Corning 進行玻璃封裝概念驗證；TSMC 亦在評估；美國政府列為先進封裝國產化優先項目。
**Insight:** 玻璃基板若 2027-2028 年進入量產，將重塑先進封裝地理格局——目前集中台灣（CoWoS）和韓國的封裝能力，可能出現「美國玻璃基板 + 亞洲 silicon」混合供應鏈。短期（2026-27）不影響手機 SoC；中期（2028+），cost-down 成功後 edge AI SoC 的 chiplet 整合密度可受益。MTK 應追蹤此技術路線，評估未來封裝合作選項多樣化的可能性。
🔗 [Manila Times / Globe Newswire](https://www.manilatimes.net/2026/05/01/tmt-newswire/globenewswire/us-semiconductor-industry-convenes-at-glass4chips-summit-on-may-14-15/2333131/amp)

---

## 3️⃣ 🌍 國際新聞

### ⑦ ⭐⭐⭐ 伊朗戰後核武論：「政權若存活，核武是唯一理性安全選項」，中東商業風險無法切割
**摘要:** 5 月 1 日，GeopoliticalMonitor 分析：美-以-海灣聯軍打擊後伊朗若政權存活，取得核武是阻止下一輪打擊的唯一邏輯（北韓模式複製）。伊朗戰爭已將波斯灣推入「商業暴露無法脫離地緣衝突」的新風險類別。中東局勢同步促使阿聯酋加速退出 OPEC，改走雙邊能源協議路徑；沙烏地面臨 OPEC 崩解壓力。
**Insight:** 中東高風險化是川普 5/14 北京行的重要背景——習近平必然將「全球秩序管理需要中美合作」作為籌碼。更長遠：美軍事資源被中東持續消耗，台海危機的「美國注意力成本」上升，地緣風險溢價已需計入 TSMC 供應鏈穩定性評估。AI 資料中心電力需求 + 中東能源供應不確定性 = edge AI 去中心化推論的商業邏輯再次獲得能源結構支撐。
🔗 [GeopoliticalMonitor](https://www.geopoliticalmonitor.com/) | [Foreign Policy: 2026 Risks](https://foreignpolicy.com/2026/01/02/top-10-risks-2026-ukraine-trump/)

### ⑧ ⭐⭐⭐ 阿聯酋退出 OPEC：美國從「秩序擔保人」轉型為「不可或缺供應商」，能源秩序重組
**摘要:** 阿聯酋正式退出 OPEC（決策積累 15 年，伊朗戰爭加速觸發），轉向雙邊能源定價協議。分析指出美國正從多邊秩序擔保人轉向「向依賴國販售安全保障的不可或缺供應商」（realpolitik 轉型）；沙烏地阿拉伯面臨 OPEC 崩解風險，正與北京重啟「石油人民幣」機制談判；伊朗、歐洲、東南亞均感受到此結構壓力。
**Insight:** UAE-OPEC 退出 + 「石油人民幣」若同步成立，是美元霸權最大結構性挑戰之一。對科技產業間接影響：能源供應不確定 → 電力成本上升 → AI 資料中心 OPEX 壓力 → 加速 edge AI / 分散式推論商業邏輯。MTK 的 edge AI 論述在「能源與地緣雙重不確定」的框架下，比任何時候都更具說服力——這是對外部投資人和企業客戶最有力的 positioning 論述。
🔗 [Time: Top 10 Global Risks 2026](https://time.com/7343169/top-10-global-risks-2026/) | [CFR 2026 Foreign Policy](https://www.cfr.org/articles/visualizing-2026-five-foreign-policy-trends-watch)

---

## ⚠️ 弱訊號

1. **Multi-model AI Agent Routing 成為隱形基礎設施** — 開發者正在同時路由 GPT-5.5 / DeepSeek V4 / Claude Opus 4.7，依成本、速度、任務類型動態分配，催生新一層「LLM 路由中間件」。主流媒體幾乎未報導，但這個架構模式正在快速成為 2026 年 AI 應用開發的標準實踐。對 MTK 意涵：edge SoC 上的 on-device model 未來可能不是單一模型，而是「小模型本地決策 + 路由至雲端大模型」的混合架構，硬體設計需為此預留通訊與排程算力。🔗 [aithority.com](https://aithority.com/machine-learning/from-gpt-5-5-to-deepseek-v4-how-developers-are-building-smarter-ai-agents-with-multi-model-routing-in-2026/)

2. **Glass4Chips = 美國重奪先進封裝主導權的長線布局** — 本次 Summit 同時有 SEMI 和 IEEE 主辦，是技術標準化的前置步驟，意味著美國正在「標準制定 → 生態綁定」的既有路徑上推進玻璃基板。這比單純技術研發更值得追蹤——誰先制定玻璃基板封裝標準，誰就掌握下一代 AI 晶片封裝格局。🔗 [SEMI / Glass4Chips Summit](https://www.manilatimes.net/2026/05/01/tmt-newswire/globenewswire/us-semiconductor-industry-convenes-at-glass4chips-summit-on-may-14-15/2333131/amp)

---

*[daily issues](https://github.com/hank800620/morning-brief/issues?q=is%3Aissue+label%3Adaily)*
