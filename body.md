# 📊 Hank's Weekly Brief · 2026-06-15 (2026-W25)
**Window: 2026-06-08 06:30 → 2026-06-15 06:30 (Asia/Taipei)**

---

## 1️⃣ 🧠 Weekly Insight
**本週主旋律:** 美伊日內瓦停戰簽成×Apple Gemini Siri 三層路由架構曝光×MTK AI ASIC 外資估值大幅上修 — 地緣風險解封、邊緣 AI 角色重組、聯發科再定價三合一

**結構性變化:**
- **荷莫茲正式重開：** 伊朗副外長確認協議於瑞士簽署，Trump 宣布「免費開放荷莫茲海峽」並撤除美軍封鎖。全球供應鏈 2026 最大尾端風險消除，能源成本↓→AI data center capex 擴張空間↑，台灣供應鏈緊急模式可轉常態規劃。
- **Apple Siri 三層路由架構揭露：** 設備端（Apple 自研小模型）→ Private Cloud Compute → Google Cloud（Blackwell B200 GPU）三層路由，等於公開宣告「最重推理交給 Google 雲端算力」。AAPL 首週 -3.11%，但業界普遍認定方向正確。on-device AI 的真實競爭維度已從「能力」收縮到「隱私+延遲+成本」。
- **MTK AI ASIC 估值重設：** 法說會 AI ASIC 目標翻倍至 $20B+；高盛以「AI Platform Company」框架將目標價上調至 5,000 TWD；摩根士丹利調至 2,088 TWD；2027 AI ASIC 市場預測從 2028 年提前兌現，$70–120B 規模成為主流預測。MTK Q1 2026 AI Edge 晶片佔比已達 46%。

**對你的下一步:**
- **停戰後 48 小時：** 確認台灣供應鏈「繞好望角備案」是否可轉回荷莫茲常規航線，計算物流成本節省；同步向 CEO 更新油價下跌→AI data center 能源成本↓的正面影響框架。
- **Apple 三層路由確立後：** 立即修訂 MTK edge AI SoC 對外敘事——主打「隱私不出設備、無 API 計費、毫秒延遲」三個差異化點，而非「模型能力追趕雲端」。
- **外資目標價大幅上修後：** Q2 法說前（預計 7 月底）準備「AI Platform Company 三引擎」估值拆解簡報，對準分析師重新定價邏輯。

---

## 2️⃣ 🪞 上週對賬（W24 預測 → W25 驗證）

| 狀態 | W24 預測 / 任務 | W25 驗證結果 |
|------|----------------|-------------|
| ✅ Confirmed | WWDC 2026 今日揭幕，Siri 多 AI 後端 | Gemini 1.2T 三層路由確認；iOS 27 多 AI 後端；Tim Cook 9/1 退休；John Ternus 接任 CEO；AAPL -3.11% |
| ✅ Confirmed | 美伊停戰備忘錄最終章進行中 | 伊朗副外長確認瑞士簽署；荷莫茲「免費開放」；美軍封鎖移除；W24 四日連線主題正式收口 |
| ✅ Confirmed | MTK COMPUTEX 後市場再定價 | 高盛 5,000 TWD + 摩根士丹利 2,088 TWD 大幅上修；AI ASIC 目標翻倍；2027 市場時程提前 |
| ✅ Confirmed | Anthropic IPO 持續推進 | OpenAI 同步推進 IPO 材料；Anthropic 程序繼續（W26 將有更多細節） |
| ⏳ Pending | MATCH Act 全院表決 | 連續五週無新動態，持續掛起 |

---

## 3️⃣ 🔭 本週 5 條主軸線

### 主軸 1: 美伊日內瓦協議正式簽署 — 荷莫茲重開，全球宏觀最大尾端風險解除
- **重要性:** ⭐⭐⭐⭐⭐
- **發生了什麼:** 伊朗副外長 Kazem Gharibabadi 確認停戰協議已完成定稿並於瑞士簽署。Trump 聲明即刻授權「免費開放荷莫茲海峽商業通行」，同步宣布撤除美國海軍封鎖線。根據 14 條草案：伊朗恢復 IAEA 核查合作、接受荷莫茲中立化監管；美國解凍伊朗 50% 凍結資產並啟動 $3,000 億重建基金框架。自 2026 年 4 月 8 日初步停火以來的地緣拉鋸局面正式落幕。
- **Insight:** 荷莫茲每日通過全球約 21% 原油，重開後 Brent 油價預計 2–4 週內下跌 10–15 美元。AI data center 電力通常以天然氣定價，能源成本壓力緩解→算力採購 ROI 改善→Hyperscaler capex 可能進一步上調。對 MTK DCS ASIC 業務：大型 AI 雲端客戶算力採購窗口擴大，是短期內推進 Hyperscaler 合約的最佳時機。台灣供應鏈「繞好望角」的額外成本（+40 天航程）可在未來 90 天內回歸荷莫茲航線，物流成本節省幅度顯著。
- **來源:** [Britannica 2026 Iran War Ceasefire](https://www.britannica.com/event/2026-Iran-war) | [Wikipedia 2026 Iran War Ceasefire](https://en.wikipedia.org/wiki/2026_Iran_war_ceasefire)

### 主軸 2: Apple WWDC 後首週 — Siri 三層路由架構曝光，AAPL -3.11%，業界謹慎看多
- **重要性:** ⭐⭐⭐⭐⭐
- **發生了什麼:** WWDC 結束後技術細節陸續浮現：Siri 採三層路由——簡單任務留在設備端（Apple 自研小模型）；中等複雜度到 Apple Private Cloud Compute；最重推理任務送至 Google Cloud（Blackwell B200 GPU 運算，Gemini 1.2T 自定義版本，Apple 據報每年授權費約 $10 億）。iOS 27 支援用戶自選 Gemini/Claude/ChatGPT 作為後端。AAPL 首週下跌 3.11%，分析師評語普遍為「方向正確但功能交付仍需數月」。
- **Insight:** 三層路由架構的揭露改變了 Edge AI SoC 競爭的基準線：設備端自研模型負責「快速、私密、無網路」任務；雲端負責「需要推理深度」的任務。MTK NPU 的競爭維度因此更清晰——不是要在設備上複製 Gemini 能力，而是在延遲<50ms、資料不離機、每次 inference 零 API 成本三個場景守住護城河。Apple 以 $10 億/年授權 Gemini，等於對市場公開說：「我們付得起，但你的手機晶片商不能讓每個用戶都這樣。」這正是 MTK 對 OEM 客戶最有力的成本差異化說詞。
- **來源:** [Phemex AAPL WWDC Reaction](https://phemex.com/academy/apple-wwdc-2026-siri-gemini-aapl-buyback) | [Digitimes Siri Gemini Analysis](https://www.digitimes.com/news/a20260609VL206/apple-apple-intelligence-siri-google-gemini-wwdc-2026.html)

### 主軸 3: MTK AI ASIC 法說上調目標 × 外資大幅上修估值 — 「AI Platform Company」定價時代開始
- **重要性:** ⭐⭐⭐⭐⭐ (直接相關)
- **發生了什麼:** MTK 法說會明確上調 AI ASIC 2026 年營收目標翻倍至逾 $20 億美元。高盛以「AI Platform Company」本益比框架將目標價從 1,800 TWD 大幅上修至 5,000 TWD（+178%）；摩根士丹利調至 2,088 TWD（+約 70%）；Google TPU 訂單放量為主要驅動力之一。MTK Q1 2026 財報顯示 AI Edge 晶片已佔總營收 46%，2027 年 AI ASIC 市場預測提前至 $70–120B，較 2028 年目標時程提早一年。
- **Insight:** 外資以「AI Platform Company」定價取代「手機晶片商 PE」，是資本市場對 COMPUTEX 三引擎（汽車+雲端 ASIC+PC AI）敘事的正式接受。但這也帶來更高期待門檻：下一個法說如果 AI ASIC 季度數字不達預期，修正幅度會比傳統 SoC 時代更劇烈（參考 Broadcom Q3 -14%）。MTK 需要建立「AI ASIC 季度指引」的投資人教育框架，強調多年合約而非單季數字。
- **來源:** [CMoney 聯發科法說 AI ASIC](https://cmnews.com.tw/article/newsyoudeservetoknow-c9c7c4d6-530c-11f1-8ddf-9bf378edae53) | [經濟日報 MTK 目標價](https://money.udn.com/money/story/5710/9476088)

### 主軸 4: OpenAI IPO 材料最終確認 + 生物防禦 AI — 算力需求再度量化
- **重要性:** ⭐⭐⭐
- **發生了什麼:** OpenAI 本週完成 Wall Street IPO 文件最終確認（Nasdaq/NYSE 選項評估中），同步推出生命科學 AI 模型更新（精準醫療、蛋白質結構分析）並啟動 AI 生物防禦計劃，作為 IPO 前的公共利益定性。微軟本週完成對 OpenAI $130 億投資 + Anthropic $50 億的雙線布局，但同步宣布加速內部 AI 自研以降低對外依賴。
- **Insight:** OpenAI S-1（IPO 申請書）一旦公開，其算力採購成本、Azure/Google 雲端支出比例、每 Token 推理成本等數字將成為業界「AI 算力定價錨」。MTK DCS ASIC 業務的 ROI 論述可直接對標 OpenAI S-1 的推理成本數字：「在 MTK XPU 上跑 vs. 在 Google Blackwell 上跑，每百萬 Token 成本差多少？」這是 W26 需要讓 BD 團隊準備的說法。
- **來源:** [MarketingProfs AI Update June 2026](https://www.marketingprofs.com/opinions/2026/54909/ai-update-june-5-2026-ai-news-and-views-from-the-past-week)

### 主軸 5: 中國國產 AI 晶片市佔率破 60% + Meta 可穿戴 AI 全面佈局
- **重要性:** ⭐⭐⭐
- **發生了什麼:** 中國 AI 晶片市場數據顯示，受美 BIS 出口管制影響，外資晶片（NVIDIA H800 等）市佔降至幾乎零，國產替代（寒武紀、壁仞、阿里真武等）市佔突破 60%，阿里巴巴發布真武 M890 自研 AI 晶片路線圖，被路透社評為「中國在自主研發 AI 晶片最具里程碑意義的展示」。同期，Meta 宣布 AI 眼鏡 + AI 項鍊（「AI Pendant」測試中）+ 企業版「Wearables for Work」三線並進的可穿戴 AI 戰略，並確認 2026 大幅提升可穿戴裝置銷售量；BYD 宣布進軍人形機器人市場。
- **Insight:** 中國 AI 晶片市佔破 60% 意味著「技術脫鉤第一個量化里程碑」正式達成。MTK 在中國市場的定位因此必須重新聚焦：雲端 AI 晶片在中國幾乎無市場空間（本土替代完成），但車載/IoT/工業邊緣 AI（Dimensity Auto / Genio 系列）仍有分散化的機會，因為這些場景對特定應用優化的需求比「主權AI算力」更具技術門檻。Meta 可穿戴 AI 三線布局則預示 2026 H2 邊緣 AI 場景多樣化：MTK Wi-Fi 8 + BT LE 晶片組可能是「Wearables for Work」的關鍵連接組件。
- **來源:** [STCN 國產AI晶片市佔](https://www.stcn.com/article/detail/3896923.html) | [BuildFastWithAI June 8 Roundup](https://www.buildfastwithai.com/blogs/ai-news-today-june-8-2026)

---

## 4️⃣ ⚠️ 本週 2 個最重要弱訊號

### 弱訊號 1: Apple 最重推理外包至 Google Blackwell B200 — Apple 自研 AI 晶片路徑是否已靜默放棄？
- **為什麼你不該錯過:** 三層路由中「最重推理 → Google Cloud Blackwell B200」的揭露，比「使用 Gemini 模型」更深一層：Apple 在 GPU 算力上也選擇外包給 Google，而非使用 Apple Silicon 自研的伺服器推理節點。若 Apple 確認不打算開發自研 AI 伺服器晶片（如傳聞中的「Atlas」），這代表高端伺服器推理市場的競爭者減少一個，MTK DCS ASIC 的潛在市場上限往上修。但也意味著「Apple 生態的 on-device NPU 算力天花板」被 Apple 自己確認了——設備端 NPU 更多扮演「快取/過濾層」而非「主力推理引擎」。
- **追蹤指標:** Apple Q2 法說 capex 細節（是否含 Google Cloud GPU 採購揭露）；Apple 內部 AI 伺服器晶片傳聞（「Atlas」計劃）是否有媒體跟進；Apple 對 Private Cloud Compute 規模的未來投入聲明
- **來源:** [Phemex AAPL WWDC Analysis](https://phemex.com/academy/apple-wwdc-2026-siri-gemini-aapl-buyback)

### 弱訊號 2: 阿里真武 M890 + 中國國產 AI 晶片破 60% — 「亞洲主權 AI 硬體」的第二個重要里程碑
- **為什麼你不該錯過:** 韓國（NAVER GW 級 AI 基礎設施）、日本（Rapidus 2nm）、中國（真武 M890 + 60% 市佔）三者同步進行，「亞洲 AI 主權硬體三角」正在快速具體化。中國的 60% 市佔是首個「去外資化完成」的量化里程碑，將成為其他亞洲國家政府評估自主 AI 晶片可行性的參考標竿。MTK 在非中國亞洲市場（東南亞、印度、中東）主打「非美系、非中系」的第三條邊緣 AI 路徑，此時窗口最佳。
- **追蹤指標:** 阿里真武 M890 量產時程與效能基準測試；東南亞/印度政府 AI 主權基礎設施招標動態；MTK 對東南亞政府 OEM 通路的新合約簽署
- **來源:** [STCN 國產AI晶片](https://www.stcn.com/article/detail/3896923.html)

---

## 5️⃣ 🎤 Monday Talking Points + 部門策略

### Talking Point 1
> 「停戰簽成，荷莫茲重開。這不只是和平新聞，是 AI 算力擴張最後一個宏觀障礙移除。下半年 Hyperscaler capex 有理由再往上。」

**背後的部門策略:** 能源成本↓ → AI 雲端 ROI↑ → Hyperscaler 採購預算擴大 → MTK DCS ASIC 潛在客戶採購窗口。本週應主動聯繫 DCS BD 團隊確認是否有 Hyperscaler 採購時程因能源成本改善而提前。

### Talking Point 2
> 「Apple 花 $10 億/年買 Gemini，讓 Google Blackwell 跑最重的推理。這是 on-device AI 最好的背書：能力交給雲端，隱私和延遲就是 NPU 的護城河。MTK 的 edge AI 定位需要重寫成這個語言。」

**背後的部門策略:** 把 MTK NPU 的差異化敘事從「能力競賽」轉向「三零保證」（零延遲、零 API 成本、零資料外傳），這是 Apple 自己用 $10 億/年驗證的市場需求。下週更新 OEM 簡報的首頁 Slide。

### Talking Point 3
> 「高盛把我們定價到 5,000 TWD，用的是 AI Platform Company 框架。問題是：我們有沒有準備好讓市場理解為什麼這個框架是對的？三引擎（C-X1 / DCS / N1X）合在一起的估值邏輯是什麼？」

**背後的部門策略:** Q2 法說前（7 月底）完成「AI Platform Company 三引擎拆解」投資人教育材料，重點在讓分析師理解三條業務線的相互強化關係，而非三個獨立 PE 倍數。

### Talking Point 4–5
> 「中國 AI 晶片市佔超 60%。這不是威脅，是指路牌：中國市場未來的戰場是邊緣 AI（車載/IoT），不是雲端 AI。MTK Dimensity Auto 和 Genio 在這個戰場有位置。」

> 「OpenAI IPO S-1 一旦公開，AI 算力成本就有了公開錨點。我們的 DCS ASIC 的成本論述需要對標那個數字——每百萬 Token 省下多少錢。BD 團隊現在就要準備這個計算。」

---

## 6️⃣ 📅 下週重點關注

### 📆 預定事件
- **2026-06-16–20** 荷莫茲重開後首週油價走勢 — 看點: Brent 是否跌破 $70，帶動 AI data center PPA 能源成本預期調降
- **2026-06-16–20** Apple iOS 27 developer beta 第一週反應 — 看點: Gemini 三層路由實際延遲數據 vs. 行銷承諾
- **2026-06-17** MTK 分析師法說後報告陸續出爐（摩根、高盛、花旗完整版） — 看點: 2027 AI ASIC $70–120B 市場假設細節
- **2026-06-20** MATCH Act 五週掛起後，是否出現新動態

### 📊 下週要追的數字
- Brent 原油現貨價格（荷莫茲重開後第一週均價）
- MTK 股價 vs. 外資新目標（5,000 TWD 高盛 / 2,088 TWD 摩根）距離
- OpenAI S-1 公開申請日期（若本週末前確認）
- Apple AAPL 股價第二週表現（-3.11% 後是否止穩）
- 中國真武 M890 基準測試數字（若 Alibaba 公開）

### ⚠️ 可能引爆的風險
- **伊朗國內強硬派反彈：** 伊斯蘭革命衛隊（IRGC）未公開表態支持停戰，若出現軍事挑釁事件，荷莫茲協議可能在 2–4 週內破局
- **Apple iOS 27 功能再次延遲：** Gemini 三層路由完整功能若推遲至 2027，AAPL 將面臨第三次消費者失望，股價有較大下行風險
- **MTK 外資目標價大幅上修後的業績壓力：** 高盛 5,000 TWD 等於市場期待值大幅提高，Q2 法說（7 月底）若 AI ASIC 季度數字不達新預期，修正風險加倍（參考 Broadcom Q3 -14%）

---

## 7️⃣ 🚫 Skip Pile

- **BYD 人形機器人進場：** 只有方向性聲明，無規格/時程/合作夥伴細節，下次有量產路線圖時再追。
- **Broadcom 股價 -14% 後市走勢：** 已在 W24 完整分析過基本面 vs. 情緒分離，本週無新基本面事件，跳過重複。
- **Meta AI 眼鏡 "Wearables for Work"：** 功能未正式發布，僅策略聲明，Q3 發布前不再追蹤。
- **墨芯 AI C 輪 10 億融資：** 中國 AI 晶片新創，MTK 直接競爭面有限，列觀察名單但不進主線。
- **微軟內部 AI 自研轉向：** 長線方向性訊號，具體產品尚不明確，不影響本週 MTK 決策，3 個月後若有發布再評估。

---

*[daily](https://github.com/hank800620/morning-brief/issues?q=is%3Aissue+label%3Adaily) · [weekly](https://github.com/hank800620/morning-brief/issues?q=is%3Aissue+label%3Aweekly)*
