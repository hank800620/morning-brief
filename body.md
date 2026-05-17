# 📊 Hank's Weekly Brief · 2026-05-18 (2026-W21)
**Window: 2026-05-11 06:30 → 2026-05-18 06:30 (Asia/Taipei)**

---

## 1️⃣ 🧠 Weekly Insight
**本週主旋律:** Google I/O 決戰前夕 × Hormuz 史上最大供應衝擊 × 川習後晶片管制延續 — 三條軌道同步加速，MTK 從晶片商升格為 AI Agent 基礎設施核心

**結構性變化:**
- **Gemini Intelligence 5/13 Android Show 預亮相**，系統級跨 App AI 代理從「概念」轉為明天（5/19）落地產品；Android NPU 需求規格從「單場景推理」升維為「持續背景執行 × 跨 App 上下文管理 × 螢幕視覺解析」三合一。
- **Hormuz 供應衝擊被 IEA 確認為史上最大**：4 月 Brent 均值 $117/bbl，全球供應驟降 10.1 mb/d；BOM 成本 $100+ 結構性鎖定，edge AI SoC TCO 差異化從「加分項」升格為「採購必需理由」。
- **川習峰會後中美科技脫鉤進入 6–12 個月緩衝確認期**，中國 12 天爆出 4 個 frontier 級開源 AI 模型（GLM-5.1 / MiniMax M2.7 / Kimi K2.6 / DeepSeek V4），自主 AI 路線顯著加速；Qualcomm CEO 宣示「edge AI 獲勝 = AI 競賽獲勝」，正面與 MTK 軌道交叉。

**對你的下一步:**
- **明天 5/19 I/O 後 48 小時：** 確認 Gemini 4.0 edge API 路線圖；評估 MTK 第二 ASIC（Google TPU 客製）技術對齊緊急程度。
- **本週：** 更新 BOM Scenario C（Brent $120+）觸發條件；edge AI TCO 論述升格為客戶主訴求，量化能源成本差距。
- **5/25 前（Computex 倒數 7 天）：** 完成「MTK Dimensity Agent Phone vs. N1 AI PC SoC」定位文件，搶先 NVIDIA 媒體框架。

---

## 2️⃣ 🪞 上週對賬（W20 → W21）

| 狀態 | W20 預測 | W21 驗證 |
|------|----------|----------|
| ✅ Confirmed | Google I/O Gemini Intelligence 跨 App 代理落地 | 5/13 Android Show 預亮相確認；跨 App 操作 + 螢幕理解 + Googlebook，5/19 主題演講加碼 |
| ✅ Confirmed | 川習峰會 Scenario B（6 個月展延）概率 65% | 峰會落幕，晶片管制「非主要議題」；H200 維持「美批 / 中待命」，Scenario B 完全驗證 |
| ✅ Confirmed | MTK 雙 NPU 架構（OpenAI 手機）持續確認 | wccftech / AndroidAuthority：N2P 2nm 製程細節補全；量產加速至 2027 H1 |
| ✅ Confirmed | TSMC 5/14 技術研討會，AI 高原論排除 | Applied Materials + TSMC EPIC Center 合作揭幕；台灣成全球 AI 供應鏈戰略中心 |
| ⏳ Pending | MATCH Act 全院表決 | 無新動態，繼續追蹤 |
| ❌ Refuted | 川習中介美伊停火 → Brent 回落至 $85–90 | 停火未成；IEA 確認史上最大供應衝擊，4 月均值 $117；W20 弱訊號 2 樂觀情境出局 |

---

## 3️⃣ 🔭 本週 5 條主軸線

### 主軸 1: Google I/O 前夕——Gemini Intelligence 登場，MTK NPU 算力需求規格劇烈升維
- **重要性:** ⭐⭐⭐⭐⭐
- **發生了什麼:** 5/13–14「Android Show: I/O Edition」預亮相：Gemini Intelligence 跨 App 系統代理（自動填表/購物/訂位 + 螢幕即時理解）正式發布；Googlebook（Magic Pointer 召喚 Gemini）由 Acer/ASUS/Dell/HP/Lenovo 出貨；Gemini 4.0 + Omni 影片生成器明天 5/19 主題演講全揭幕。
- **Insight:** Android NPU 需求從「TOPS 數字競賽」升維為「持續背景推理 × 多 App 上下文 × 視覺解析」三合一。MTK 是否進入 Gemini Intelligence 官方 SoC 認證清單，將成為 2027 Android OEM 旗艦機型 SoC 選擇的關鍵因素；MTK 第二 ASIC（Google TPU 客製）必須在 5/19 後確認 workload 規格對齊。
- **來源:** [Android Central — I/O 2026 Live Blog](https://www.androidcentral.com/phones/live/google-i-o-2026-live-blog-android-17-android-xr-glasses-and-all-the-gemini-ai-news) | [Digitimes — Google Android Gemini AI 2026](https://www.digitimes.com/news/a20260513VL201/google-android-gemini-ai-2026.html)

### 主軸 2: 川習峰會後格局確立——Scenario B 驗證 + 中國 AI 開源 12 天 4 模型爆發
- **重要性:** ⭐⭐⭐⭐⭐
- **發生了什麼:** 峰會落幕：關稅 145% → 30%，Boeing 200 架確認，但晶片管制「非主要議題」，Jensen Huang 隨行未解鎖 H200；中美科技脫鉤進入「暫停而非解凍」6–12 個月緩衝期。同週中國 12 天爆出 4 個 frontier 級開源模型（GLM-5.1 / MiniMax M2.7 / Kimi K2.6 / DeepSeek V4），均在 agentic engineering benchmarks 達到西方 frontier 水準；中國 AI 晶片國內市占率預計 2026 年達 50%。
- **Insight:** 中國 AI 開源爆發是「以開源換生態影響力」的系統性策略，12 天 4 模型顯示迭代進入週更節奏。對 MTK：中國 OEM（MTK 主要客戶群）旗艦機型將面臨支援 DeepSeek V4 / Kimi K2.6 on-device 部署的市場壓力；晶片管制延續確認 MTK ASIC 自主路線差異化窗口持續有效；Google TPU 第二 ASIC 是中立於管制博弈的最佳收入多元化路線。
- **來源:** [abhs.in — US-China Trade Truce May 12](https://www.abhs.in/blog/us-china-trade-truce-beijing-summit-chip-export-controls-semiconductor-may-2026) | [Built In — Trump Lifts AI Chip Ban China](https://builtin.com/articles/trump-lifts-ai-chip-ban-china-nvidia)

### 主軸 3: Hormuz 史上最大供應衝擊——Brent $117，亞洲製造業 BOM 進入新均衡
- **重要性:** ⭐⭐⭐⭐⭐
- **發生了什麼:** IEA 確認霍姆斯海峽危機為史上最大油市供應中斷：全球供應驟降 10.1 mb/d → 97 mb/d；4 月 Brent 均值 $117/bbl（vs. 2 月 $71）；亞洲煉廠削減 6 mb/d 產出；LPG/乙烷缺口使印度、東南亞食品與肥料通膨飆升。物理原油現貨一度逼近 $150/bbl。
- **Insight:** $117 不是峰值，是均值。BOM Scenario C（$120+ 結構性高位）觸發條件已接近現實。對 MTK：(1) edge AI SoC 低功耗特性的 TCO 優勢可直接量化為美元節省，$117 Brent 使「MTK NPU vs. GPU 推理省電 X 倍」立即轉化為年度成本差異；(2) 亞洲 OEM 在高 BOM 壓力下更傾向 SoC 整合方案（MTK 優勢），而非多晶片模組。
- **來源:** [Discovery Alert — Hormuz Oil Supply 2026](https://discoveryalert.com.au/strait-hormuz-oil-supply-disruption-price-impact-2026/) | [IEA — Oil Market Report April 2026](https://www.iea.org/reports/oil-market-report-april-2026)

### 主軸 4: TSMC 2026 技術研討會——N2P/A16 藍圖揭幕，台灣成全球 AI 供應鏈戰略中心
- **重要性:** ⭐⭐⭐⭐
- **發生了什麼:** 5/14 TSMC Technology Symposium（新竹）：(1) AI 應用從雲端快速擴展至 edge，驅動計算密度/高頻寬連結/能效三重需求爆增；(2) N2P 全面加速布局，先進封裝需求與 N2P 並進；(3) Applied Materials + TSMC EPIC Center 合作揭幕，聯合加速 AI 晶片開發流程；(4) 2026 CapEx $52–56B 創歷史新高。Computex 分析：台灣正成為 AI 供應鏈地緣戰略中心，ASIC/NPU/先進封裝取代傳統 PC SoC 為最高優先。
- **Insight:** TSMC N2P 搶先布局直接影響 MTK Dimensity 9600 量產排程確定性——OpenAI 手機 2027 H1 量產的產能鎖定窗口現在需要行動。N2P 優先產能競爭（Apple A20 / Nvidia / Google / MTK）已開始，建議 MTK 業務團隊在 5/25 前確認 2026 Q4–2027 Q1 wafer 排程鎖單狀態。
- **來源:** [Digitimes — TSMC Technology Packaging 2026](https://www.digitimes.com/news/a20260514PD231/tsmc-technology-packaging-demand-2026.html) | [tspasemiconductor — Computex 2026 Taiwan AI Supply Chain](https://tspasemiconductor.substack.com/p/computex-2026-why-taiwan-is-becoming)

### 主軸 5: Qualcomm CEO 宣示「edge AI 獲勝 = AI 競賽獲勝」——MTK vs. Qualcomm 正面對決升溫
- **重要性:** ⭐⭐⭐⭐
- **發生了什麼:** Qualcomm CEO 公開宣示 edge AI 競賽勝者將贏得整個 AI 競賽，宣告從手機晶片商全面轉型 edge AI 平台；Snapdragon X2 Elite Extreme 宣稱 85 TOPS NPU + 100 TOPS+ 整合算力；Qualcomm AI Hub 持續擴大 on-device LLM 認證生態。對照：MTK 因 OpenAI 捨 Qualcomm 選 Dimensity 9600，在旗艦 AI 手機賽道取得明確技術背書。
- **Insight:** 兩年後的 SoC 市場將由 edge AI 能力決定勝負。MTK 的競爭優勢需從「OpenAI 選 MTK」的外部背書出發，積極補強 Gemini Nano / Claude Edge 認證清單。Snapdragon X2 攻 AI PC，MTK Dimensity 9600 鞏固 AI 手機 Agent——垂直市場分割對 MTK 有利，Computex 前應強化此差異化論述。
- **來源:** [Motley Fool — Qualcomm CEO Edge AI](https://www.fool.com/investing/2026/04/11/qualcomms-ceo-says-the-winner-of-edge-ai-will-win/) | [science-technology.news — Qualcomm Strategic Pivot](https://science-technology.news-articles.net/content/2026/05/11/qualcomm-s-strategic-pivot-moving-beyond-mobile-to-the-ai-driven-edge.html)

---

## 4️⃣ ⚠️ 本週 2 個最重要弱訊號

### 弱訊號 1: 中國 AI 開源「週更」化——12 天 4 個 frontier 模型，on-device ASIC 推論需求端規格快速升維
- **為什麼你不該略過:** GLM-5.1 / MiniMax M2.7 / Kimi K2.6 / DeepSeek V4 在 12 天內連發，均達 frontier agentic benchmark 水準。這是中國 AI 生態在晶片管制壓力下「以開源換生態影響力」的系統性策略。對 MTK：中國 OEM 旗艦機型將面臨「必須支援 DeepSeek V4 / Kimi K2.6 on-device 部署」的市場壓力，NPU 推論規格將在 H2 2026 產品規劃周期快速升維。若 MTK NPU 路線圖未在本季確認對這四個模型的優化支持，OEM 可能轉向 Qualcomm AI Hub 已認證的替代方案。
- **追蹤指標:** 中國 OEM（OPPO/小米/VIVO）H2 2026 旗艦 AI 功能清單中 DeepSeek V4 / Kimi K2.6 on-device 部署需求；MTK NPU SDK 是否在 Q2 內發布對應優化包
- **來源:** [Built In — Trump Lifts AI Chip Ban China](https://builtin.com/articles/trump-lifts-ai-chip-ban-china-nvidia) | [semiconductorsinsight — US China H200](https://semiconductorsinsight.com/us-china-chip-export-controls-h200-2026/)

### 弱訊號 2: Applied Materials + TSMC EPIC Center——AI 晶片製造「設計 × 製造共演化」新模式起跑
- **為什麼你不該略過:** Applied Materials 與 TSMC 聯合成立 EPIC Center，目標加速 AI 晶片從設計到量產的迭代週期——半導體史上首次設備商與晶圓廠在同一屋簷下進行聯合製程開發，N2P/A16 迭代速度預計提升 30%+。對 MTK：若 EPIC Center 優先服務超大規模 ASIC 客戶（Apple / Nvidia / Google），MTK 進入 EPIC Center 合作機制將直接縮短第二 ASIC（Google TPU 客製）的設計驗證週期，是 2027 年底量產時程的關鍵加速槓桿。
- **追蹤指標:** TSMC EPIC Center 合作客戶清單；MTK 設計中心是否加入聯合開發計畫；EPIC Center 第一批流片時程
- **來源:** [Digitimes — Applied Materials TSMC EPIC Center](https://www.digitimes.com/news/a20260512PR200/applied-materials-tsmc-development-partnership-equipment.html) | [Semiwiki — TSMC Technology Symposium 2026](https://semiwiki.com/semiconductor-manufacturers/tsmc/368690-tsmc-technology-symposium-2026-overview/)

---

## 5️⃣ 🎤 Monday Talking Points + 部門策略

### Talking Point 1: 「明天 Google I/O 後，MTK NPU 的 Gemini Intelligence 支援狀態是什麼？」
> Gemini Intelligence 跨 App 系統代理昨天（5/13）預亮相，今天是 5/19 主題演講。Android OEM 下一輪旗艦必須支援持續背景 AI 推理——不再是 NPU TOPS 數字競賽，而是「持續背景 + 多 App 上下文 + 螢幕視覺」三合一架構競賽。MTK Dimensity 是否在 Gemini Intelligence 官方認證清單上？

**背後的部門策略:** 若尚未在清單，本週啟動與 Google Android 團隊技術對齊會議；若已在清單，立即轉化為 OEM 客戶銷售論述——Computex 前是最佳媒體窗口。

### Talking Point 2: 「OpenAI 選 MTK 捨 Qualcomm——2027 N2P wafer 排程鎖單了嗎？」
> Dimensity 9600 N2P 2nm 量產 2027 H1，但 TSMC N2P 產能在 Apple A20 / Nvidia / Google TPU 搶訂下極度緊張。MTK OpenAI 手機專案的 wafer 排程鎖單是否本季落實？

**背後的部門策略:** 若尚未鎖定，5/25 前與 TSMC 業務窗口確認是緊急優先事項；鎖定後，量產確定性直接強化 2027 ASIC 業績能見度論述。

### Talking Point 3–5:
- **TP3:** 「Brent $117——edge AI SoC TCO 現在可以用美元數字量化：客戶每部署一台 MTK NPU vs. GPU 推理方案，年度能源成本差距是多少？立即準備這張數字。」
- **TP4:** 「Qualcomm CEO 說 edge AI 獲勝 = AI 競賽獲勝——MTK 『Dimensity 9600 Agent Phone（手機型態）vs. Snapdragon X2 AI PC』不重疊差異化定位文件 5/25 前必須完成。」
- **TP5:** 「中國 12 天 4 個 frontier AI 模型：MTK NPU SDK 是否把 DeepSeek V4 和 Kimi K2.6 加入 on-device 優化支援清單？中國 OEM Q2 旗艦規格討論現在需要答案。」

---

## 6️⃣ 📅 下週重點關注

### 📆 預定事件
- **5/19（明天）** Google I/O 主題演講（10 AM PT / 凌晨 1 AM 台北）— 看點：Gemini 4.0 發布、Gemini Intelligence 完整演示、edge deployment API 路線圖、Android 17 NPU API 更新
- **5/19 後 48 小時** MTK 第二 ASIC（Google TPU 客製）workload 規格對齊評估窗口
- **5/25** Computex 媒體日前一週窗口 — MTK edge AI 定位文件截止日

### 📊 下週要追的數字
- Brent crude spot price（Hormuz 緩解 vs. 持續，$100+ vs. $90 結構分水嶺）
- Google I/O Gemini 4.0 性能 benchmark（vs. GPT-5.5）
- MTK Gemini Intelligence 官方 SoC 認證清單收錄狀態

### ⚠️ 可能引爆的風險
- **Gemini Intelligence 認證清單排除 MTK**：若 5/19 I/O 公告僅支援 Qualcomm Snapdragon，MTK 2027 Android OEM 旗艦份額承壓
- **Hormuz 升級**：以黎停火失效 + 伊朗局勢惡化 → Brent 突破 $130，BOM Scenario C 完全觸發，Q3 量產需啟動緊急應對
- **MATCH Act 突然排程**：若本週全院表決通過，稀土管制 A/B/C 情境概率重洗牌，需 24 小時內更新情境分析

---

## 7️⃣ 🚫 Skip Pile

- **UAE 退出 OPEC 細節**：Hormuz 能源主軸已充分涵蓋，個別供應商格局調整無立即 MTK 行動點。
- **OpenAI 控告蘋果最新進展**：W20 已覆蓋核心邏輯（AI 生態整合走向法律戰），本週無重大新發展。
- **GLM-5.1 / MiniMax M2.7 個別技術細節**：弱訊號 1 以「中國 AI 開源週更化」整體趨勢涵蓋，個別 benchmark 無 MTK 立即行動點。
- **波音 200 架採購 / 農業大豆**：川習峰會非半導體議題，無 MTK 相關性。
- **Googlebook 硬件規格細節**（Acer/ASUS 出貨）：MTK 非 Googlebook SoC 供應商，暫無直接業務影響。

---

*[daily](https://github.com/hank800620/morning-brief/issues?q=is%3Aissue+label%3Adaily) · [weekly](https://github.com/hank800620/morning-brief/issues?q=is%3Aissue+label%3Aweekly)*
