# ☀️ Hank's Morning Brief · 2026-05-12 (週二)
**Window: 2026-05-11 07:00 → 2026-05-12 07:00 (Asia/Taipei)**

## ⚡ 30-Second TLDR
- ⭐ 川習峰會倒數 48 小時：首爾 Bessent × 何立峰預備談判今日啟動，Musk / Cook / Fink 等 10+ CEO 隨行北京，本週是年度最高密度地緣政治節點——今天是情境通報最後更新窗口。
- ⭐ 美伊霍爾木茲協議瀕臨破局：川普稱伊朗回應「完全無法接受」，美軍已開火攔截兩艘伊朗油輪，能源成本 Scenario C 觸發概率急升。
- Gemini 3.1 Pro 霸榜全推理 benchmark（GPQA Diamond 94.3% / ARC-AGI-2 77.1%），Microsoft-OpenAI 同步鬆綁獨家協議開放多雲——AI 競爭正式進入多極化時代。

---

## 🧠 Today's Insight
**本日摘要重點:** 今天（5/12）是年度最高密度決策窗口——首爾 Bessent × 何立峰預備談判正式開啟，北京川習峰會倒數 48 小時，美伊霍爾木茲協議同步跌入破局危機，三條線索在 72 小時內同時進入決定性時刻；任何延誤情境通報更新都將造成供應鏈決策落差。
**未來發展方向:** 首爾談判若順利，北京峰會將宣布 Board of Trade 框架 + Boeing 500 架訂單，稀土/晶片管制 Scenario A 概率從 55% 上調至 60%；霍爾木茲若持續僵局，Brent 可能突破 $110+，直接壓縮亞洲製造業 BOM；Gemini 3.1 Pro 登頂疊加 Microsoft-OpenAI 多雲化，AI 競爭格局從「雙雄壟斷」走向「多極競標」，on-device AI 的差異化定位更加重要。
**對你的意義:** ①**今天是硬截止**：Scenario A 概率可上調至 60%，但同步需設 Scenario C 霍爾木茲破局觸發條件（Brent > $108 持續 3 天）；②Jensen Huang 被排除在 CEO 訪問團之外是關鍵弱訊號——晶片出口管制仍是硬邊界，MTK ASIC 路線在此背景下差異化更顯著；③Gemini 3.1 Pro ARC-AGI-2 77.1% 可作為 MTK NPU on-device 推理能力的外部基準，評估 Dimensity 旗艦在類似任務上的差距。

---

## 1️⃣ 🤖 AI / 科技

### ① ⭐⭐⭐⭐ Gemini 3.1 Pro 霸榜全推理 benchmark：GPQA Diamond 94.3%、ARC-AGI-2 77.1%，2026 最強模型確立
**摘要:** Google DeepMind Gemini 3.1 Pro 截至 2026 年 5 月已領先所有已發布推理 benchmark：GPQA Diamond（研究生級科學推理）94.3%、ARC-AGI-2（防記憶化新型推理）77.1%，同期 GPT-5.5 與 Claude Opus 4.7 均落後。同時 AI 模型競爭進一步多極化——GPT-5.5（OpenAI）、Claude Opus 4.7（Anthropic）、Gemini 3.1 Pro（Google DeepMind）、Grok 4（xAI）、DeepSeek V4 Pro（DeepSeek）五強並立，無單一模型全面制霸。
**Insight:** Gemini 3.1 Pro 登頂代表 Google DeepMind 在「高難度推理」賽道完成反超。對 MTK：①ARC-AGI-2 77.1% 是 on-device NPU 推理能力的最高外部基準，Dimensity 旗艦 NPU 若能跑到 30-40%，即具「本機可用 AGI 推理」的市場論述；②多極化 AI 市場意味設備端需支援多模型切換（multi-model edge inference），MTK NPU 的 multi-tenant 架構規劃需提前。
🔗 [Best AI Models May 2026 – Medium](https://medium.com/@sanjeevpatel3007/best-ai-models-in-2026-the-complete-honest-ranking-d67b63cf3543) | [AI Model Release Timeline – AI Flash Report](https://aiflashreport.com/model-releases.html)

---

### ② ⭐⭐⭐⭐ Microsoft-OpenAI 鬆綁獨家：非獨家多雲、AGI 條款刪除、2032 授權確認——雲端 AI 獨占時代終結
**摘要:** Microsoft 與 OpenAI 4/27 宣布合作架構重大重組：從獨家授權轉為「非獨家授權」，OpenAI 可將全部產品服務於 AWS、Google Cloud 等任何提供商；微軟不再支付 OpenAI 收益分成；AGI 定義觸發條款完全刪除；授權期延至 2032 年。背景：OpenAI 此前已與 Amazon 達成 $500 億戰略投資，並將 $380 億 AWS 協議擴至 $1,380 億（八年）。微軟股價當日下跌 2.1%，Azure AI 市場份額壓力上升。
**Insight:** 這是 AI 雲端基礎設施格局的結構性轉折——OpenAI 模型不再是 Azure 獨占武器，AWS / GCP 均可合法競標大型企業客戶。對 MTK：on-device AI 的「無雲端依賴」價值主張在多雲競爭加劇的背景下更具吸引力——企業採購方不再只有「選哪個雲」的問題，也有「是否要脫雲」的選項；edge AI SoC 可定位為「雲端多極化時代的中立算力層」。
🔗 [Microsoft-OpenAI non-exclusive – CNBC](https://www.cnbc.com/2026/04/27/openai-microsoft-partnership-revenue-cap.html) | [Next phase of Microsoft OpenAI – Microsoft Blog](https://blogs.microsoft.com/blog/2026/04/27/the-next-phase-of-the-microsoft-openai-partnership/)

---

### ③ ⭐⭐⭐ OpenAI 推 GPT-Realtime-2 + Realtime-Translate：即時多語音翻譯進 API，語音 AI Agent 時代開啟
**摘要:** OpenAI 新增三款即時語音 API 模型：GPT-Realtime-2（強化即時語音推理）、GPT-Realtime-Translate（即時多語言語音翻譯）、GPT-Realtime-Whisper（串流語音轉文字）。Realtime-Translate 可在通話中即時跨語言翻譯，首批支援語言涵蓋英、中、日、西等主要語言。此舉直接挑戰 Google Translate 實時翻譯與 Microsoft Teams 即時字幕的市場地位。
**Insight:** 語音 AI Agent 從「輔助工具」進入「原生通訊基礎設施」——即時翻譯 API 化代表任何 App 均可零成本嵌入跨語言能力。對 MTK：①Dimensity 旗艦 APU 若能本機執行 Realtime-Whisper 級別的串流語音辨識，可大幅降低延遲與隱私風險；②MTK 的 on-device 語音 AI 路線圖需對齊「多語言即時推理」作為 2027 差異化 spec。
🔗 [GPT-5.5 Instant default – TechCrunch](https://techcrunch.com/2026/05/05/openai-releases-gpt-5-5-instant-a-new-default-model-for-chatgpt/) | [OpenAI Release Notes May 2026 – Releasebot](https://releasebot.io/updates/openai)

---

## 2️⃣ 🏭 科技產業

### ④ ⭐⭐⭐⭐⭐ ⭐ 【決戰前夕】川習峰會首爾預備談判今日啟動：Musk / Cook / Fink 等 10+ CEO 赴京，Boeing 500 架訂單接近落地
**摘要:** ⭐（跨期主題加星）美財長 Bessent 與中方副總理何立峰 5/12-13 在首爾進行「最終預備談判」，Trump 隨後 5/14 抵達北京出席川習峰會。白宮確認邀請 Elon Musk（Tesla）、Tim Cook（Apple）、Larry Fink（BlackRock）、David Solomon（Goldman Sachs）、Jane Fraser（Citigroup）、Stephen Schwarzman（Blackstone）等逾 10 位頂尖 CEO 同行——是近年規模最大的美商業代表團。Boeing CEO Kelly Ortberg 亦在列，Boeing 500 架 737 Max 訂單接近宣布，將是波音史上最大單筆交易之一。峰會議程涵蓋貿易、AI、出口管制、台灣、伊朗戰爭。重要異常：Nvidia CEO Jensen Huang 未受邀（詳見弱訊號）。
**Insight:** CEO 陣容即是談判籌碼——Tesla / Apple / Boeing / Goldman 同行代表美方將以「商業大訂單」作為政治讓步的對等交換。對 MTK：①Board of Trade 框架若落地，Scenario A（稀土管制鬆綁）概率進一步上升，今天是情境通報最後更新窗口；②Apple（Tim Cook 出席）的中國供應鏈重組走向將影響台灣 IC 設計廠訂單結構；③Jensen Huang 缺席是硬訊號：GPU/AI 晶片出口管制不在談判桌上，MTK ASIC 的「非管制晶片」定位更具競爭優勢。
🔗 [Trump CEOs Beijing – CNBC](https://www.cnbc.com/2026/05/11/trump-ceos-elon-musk-tim-cook-larry-fink-xi-china-summit.html) | [Trump heads to China – SCMP](https://www.scmp.com/news/china/article/3353199/trump-heads-china-musk-cook-and-top-ceos-xi-talks)

---

### ⑤ ⭐⭐⭐ Stanford AI Index 2026：AI 採用率升至 17.8%，勞動市場衝擊開始量化，企業 AI 基礎設施化加速
**摘要:** Stanford HAI 發布 2026 年 AI Index 報告，12 大趨勢包括：全球工作年齡人口 AI 使用率從 16.3% 升至 17.8%（Q1 2026）；企業 AI 已從「應用工具」轉為「業務基礎設施層」；Cloudflare AI 使用量 +600% 同步裁員 20%、BILL 裁員 30%、Upwork 裁員 25%，AI 替代白領就業開始量化顯現；CMA 啟動 AI 算法定價調查，全球 AI 治理密度持續上升。報告指出 AI 投資與採用的地域分化加劇——亞洲追趕速度快於預期。
**Insight:** 17.8% 採用率看似不高，但增長斜率意味 2027 年可能突破 25% 的「主流門檻」，屆時 AI 替代勞動力的政策壓力將急速上升。對 MTK：①on-device AI 在「AI 就業衝擊」敘事下有「保護隱私 + 去中心化」的正面論述空間；②企業 AI 基礎設施化趨勢確認 MTK ASIC 路線正確——算力需求不會消失，只會從雲端向邊緣擴散。
🔗 [Stanford AI Index 2026 – Stanford HAI](https://hai.stanford.edu/news/inside-the-ai-index-12-takeaways-from-the-2026-report) | [AI diffusion 2026 – Microsoft](https://blogs.microsoft.com/on-the-issues/2026/05/07/the-state-of-global-ai-diffusion-in-2026/)

---

### ⑥ ⭐⭐⭐ ⭐ MTK AI ASIC 目標翻倍至 $20億 + TSMC 2nm 確認；手機 4nm 削單 -15%，算力重心加速轉移
**摘要:** ⭐（跨期主題加星）TrendForce：MediaTek 2026 AI ASIC 營收目標已從 $10 億翻倍至 $20 億，目標 10-15% 市場份額；TSMC 2nm N2P 製程確認由 MTK 與 Qualcomm 雙方採用，2026 年量產；同時兩家公司 4nm 智慧型手機 AP 訂單均縮減約 15%，手機 SoC 業務降至 MTK 總收入 49%（Q1 2026）。Digitimes 5/11：台灣股交所對 MTK 實施交易限制（5/7-5/20），因市值突破 $1,650 億美元歷史新高。
**Insight:** MTK 正發生業務結構性轉型——從「手機 AP 廠」向「AI ASIC + 旗艦 SoC 雙引擎」進化。ASIC 目標翻倍是外部市場最強背書，直接支撐 B2B 推廣中「MTK 不只是手機晶片廠」的定位；4nm 削單反映手機市場疲軟，但 ASIC 增長對沖，整體成長動能仍正向。
🔗 [MTK AI ASIC $2B target – TrendForce](https://www.trendforce.com/news/2026/04/30/news-mediatek-reportedly-doubles-2026-ai-asic-revenue-target-to-2b-aims-10-15-market-share/) | [Taiwan freezes MTK trading – Digitimes](https://www.digitimes.com/news/a20260511VL202/digitimes-asia-weekly-news-roundup-mediatek-nand-taiwan-2026.html)

---

## 3️⃣ 🌍 國際新聞

### ⑦ ⭐⭐⭐⭐ ⭐ 【霍爾木茲破局警報】川普稱伊朗回應「完全無法接受」，美軍開火攔截兩艘伊朗油輪
**摘要:** ⭐（跨期主題加星）美伊霍爾木茲談判 5/10 急遽惡化：川普公開表示伊朗對和平提案的回應「completely unacceptable」；美軍 5/8 已在霍爾木茲海峽對峙中開火、擊傷並制伏兩艘伊朗油輪。伊朗反提案要求：承認對霍爾木茲主權、戰爭賠償、解凍資產、全面撤除制裁——與美方立場差距甚大。目前霍爾木茲每日 2,000 萬桶石油（全球海運石油 20%）通行仍受限；Brent 油價維持高位，WTI 波動幅度本週持續 $88-107。背景：美軍已與伊朗進行實彈交火，衝突升級風險顯著。
**Insight:** 霍爾木茲協議從「可能本週落地」迅速轉向「短期破局風險」，是今天最重要的情境轉折信號。對 MTK：需立即觸發 Scenario C 評估條件——若 Brent 持續高於 $108 超過 3 天，台灣製造業 BOM 上升約 8-12%，AI 伺服器組裝成本壓力同步上升；能源假設需在今天峰會分析更新時同步修正。
🔗 [Iran war updates – NPR](https://www.npr.org/2026/05/08/g-s1-121061/iran-war-updates) | [Hormuz ceasefire oil rally – CNBC](https://www.cnbc.com/amp/2026/05/08/oil-prices-today-wti-brent-us-iran-fire-war-hormuz-ceasefire.html)

---

### ⑧ ⭐⭐⭐ 【亞洲政府 AI】日本政府 500 項行政業務導入自律型 AI，數位廳推「ガバメントAI・源内」2026 年正式上線
**摘要:** 日本政府宣布 2026 年起將 500 項府省廳業務（涵蓋預算資料製作、法規審查等）全面導入自律型 AI，由數位廳主導開發政府專屬生成 AI 系統「ガバメントAI・源内」（Government AI Gennai）。系統設計要求：符合日本個人資訊保護法、不對外傳送資料、整合行政知識庫。日經調查：國內企業 AI 採用率已達 30%，製造業、金融業領先。（來源：日本経済新聞 / Amiko Consulting 5/3-9 週報）
**Insight:** 日本政府級 AI 採用是「亞洲政府 AI 主權化」的明確信號——各國正從「採購美國 AI 服務」轉向「自建主權 AI 系統」。對 MTK：①on-device / 主權 AI 的硬體需求增加，edge AI SoC 在政府採購的合規性論述（資料不出境、TEE 隔離）更具說服力；②日本市場是 MTK 的潛在政府 AI 硬體機會，特別是 AIoT 與邊緣計算裝置。
🔗 [日本生成 AI 週報 5/3-9 – Amiko Consulting](https://amiko.consulting/2026%E5%B9%B45%E6%9C%883%E6%97%A5%E3%80%9C5%E6%9C%889%E6%97%A5%E9%80%B1%E3%81%AEai%E4%B8%BB%E8%A6%81%E3%83%8B%E3%83%A5%E3%83%BC%E3%82%B9%E3%81%A8%E8%A3%BD%E9%80%A0%E6%A5%AD%E3%81%B8%E3%81%AE%E7%A4%BA/) | [今日のAIニュース – note 猫P](https://note.com/nekopy222/n/n0e074677d2dc)

---

## ⚠️ 弱訊號

1. **Jensen Huang 缺席北京 CEO 訪問團** — 白宮邀請名單涵蓋 Tesla / Apple / Goldman / Boeing 等，但 Nvidia CEO Jensen Huang 明確未在受邀之列。這是一個低調但意義重大的訊號：AI 晶片（GPU）出口管制是此次峰會的硬邊界議題，不在商業交換桌上。MTK 的 AI ASIC（非美國出口管制清單）在此格局下定位更清晰。🔗 [Nvidia Jensen Huang not included – The Tech Portal](https://thetechportal.com/2026/05/12/elon-musk-tim-cook-among-ceos-to-join-trump-on-china-visit-nvidias-jensen-huang-not-included-report/)

2. **Qualcomm / MTK 同步砍手機 4nm 訂單 -15%，AMD Lisa Su 靜悄悄接單** — MTK 與 Qualcomm 從 TSMC 4nm/5nm 撤出產能，AMD 趁機填補 Lisa Su 利用旗艦 GPU/FPGA 擴大 TSMC 先進製程佔比。暗示：手機 AP 週期性低谷可能比預期更深，TSMC 先進製程競爭窗口正在位移——對 MTK 2nm 旗艦 SoC 量產時程的產能預留需再確認。🔗 [AMD cashes in on smartphone freeze – WCCFTech](https://wccftech.com/amds-lisa-su-quietly-cashes-in-on-the-smartphone-industrys-deep-freeze-as-mediatek-and-qualcomm-vacate-tsmcs-4nm-and-5nm-lines/)

---

*[daily issues](https://github.com/hank800620/morning-brief/issues?q=is%3Aissue+label%3Adaily)*
