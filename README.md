# UADP - Universal AI Development Protocol

> **將 Cursor 從代碼聊天機器人轉化為具備權力制衡、自主修正與標準開發流程的自動化軟體工廠**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/OG-Matcha/UADP/blob/main/LICENSE)
[![Version: 1.3](https://img.shields.io/badge/Version-1.3-blue.svg)](https://github.com/OG-Matcha/UADP)

---

## 🎯 願景與痛點

### 我們解決的問題

在 AI 輔助開發的時代，我們面臨以下核心挑戰：

1. **開發發散**：AI 在需求不明確時就開始寫 Code，導致後期架構崩潰
2. **AI 偷懶**：為了通過測試常會修改測試邏輯，而非修復代碼
3. **環境摩擦**：非技術者無法自行處理環境報錯
4. **黑箱作業**：缺乏「先執行後報告」的審計日誌

### UADP 的解決方案

UADP 是一個**元框架（Meta-Framework）**，它為 Cursor IDE 提供了一套完整的 AI 開發協議，透過：

- ✅ **蘇格拉底詰問法**：在寫代碼前先釐清需求
- ✅ **測試鎖定機制**：防止 AI 修改測試標準
- ✅ **環境自動診斷**：自動檢查與修復環境問題
- ✅ **完整審計追蹤**：記錄所有技術決策與變更

---

## 🏗️ 角色分工：蓋房子的比喻

想像你要蓋一間房子，UADP 就像一個專業的建築團隊，有明確的分工：

| 角色 | 比喻 | 職責 | 權限限制 |
|------|------|------|----------|
| **🏛️ Architect（架構師）** | 建築設計師 | 問清楚你要什麼樣的房子，畫設計圖 | ❌ 禁止寫代碼 |
| **🔍 QA（測試員）** | 檢查員 | 先寫檢查清單，確保房子符合標準 | ❌ 禁止修改實作 |
| **👷 Coder（工程師）** | 建築工人 | 按照設計圖蓋房子，通過檢查 | ❌ 禁止修改測試 |
| **📋 Auditor（審計員）** | 驗收員 | 最後檢查並用白話告訴你蓋了什麼 | ❌ 禁止實作與測試 |

### 權力制衡機制

- **測試鎖定**：檢查員寫的檢查清單，工人不能隨便改（防止偷懶）
- **對抗設計**：檢查員的目標是「找出問題」，工人的目標是「通過檢查」
- **審計追蹤**：所有變更都記錄在案，不會有「黑箱作業」

---

## ✨ 核心特色

### 1. 測試鎖定機制（Test Guard）

**問題：** AI 為了讓測試通過，常會修改測試邏輯而非修復代碼。

**解決方案：**
- 測試檔案生成後，計算 SHA-256 Hash 並鎖定
- Coder 角色**無權修改** `tests/` 目錄
- 若需修改，必須透過 Auditor 記錄理由並由 Architect 授權

### 2. 自主修正協議（Pivot & Execute）

**問題：** 遇到技術障礙時，AI 可能盲目重試或卡住。

**解決方案：**
- 連續兩次修復失敗 → 強制執行 `@Web` 搜尋最新解決方案
- 所有未經確認的變更 → 記錄至 `amendments.md`
- 以「系統穩定性」與「技術最適解」為第一優先

### 3. 自主鏈式執行（Autonomous Chaining）

**問題：** AI 在每個任務完成後停下來等待確認，導致執行中斷。

**解決方案：**
- **任務看板**：AI 維護 `.uadp/tasks.md`，追蹤所有任務狀態
- **自動銜接**：任務完成後自動切換至下一個任務，無需人工介入
- **鏈式執行**：禁止產出長篇結論，直接執行下一個步驟
- **長程指令**：支援一次性執行多個任務，提高效率

**效果：**
- ✅ 解決執行中斷問題
- ✅ 提高執行效率
- ✅ 支援長程複合指令

### 4. 技術適配器（Adapters）

**問題：** 不同技術棧需要不同的最佳實踐與測試框架。

**解決方案：**
- **自動偵測**：掃描專案檔案（如 `pubspec.yaml` → Flutter）
- **模板驅動**：適配器提供技術棧特定的規則與最佳實踐
- **可擴展**：技術領導者可自訂適配器

**目前支援：**
- 📱 **Flutter**：行動應用開發
- 🌐 **React/Vite**：現代 Web 開發
- 🔧 **Node.js/Python**：後端 API 開發

---

## 🚀 快速開始

### 前置需求

- [Cursor IDE](https://cursor.sh/)（推薦最新版本）
- Python 3.8+（用於診斷工具，**啟動腳本會自動安裝**）
- Git（用於版本控制，可選）

### 安裝步驟

#### 方式一：一鍵啟動（推薦）✨

**最簡單的方式，只需一個檔案就能啟動！**

**Windows 使用者：**
1. 📥 [下載啟動檔](https://github.com/OG-Matcha/UADP/releases/latest/download/UADP-Windows.bat) `UADP-Windows.bat`
2. 將檔案放到你的專案資料夾中
3. 雙擊 `UADP-Windows.bat`
4. 腳本會自動下載初始化引擎並完成設定

**macOS/Linux 使用者：**
1. 📥 [下載啟動檔](https://github.com/OG-Matcha/UADP/releases/latest/download/UADP-macOS.command) `UADP-macOS.command`
2. 將檔案放到你的專案資料夾中
3. 雙擊 `UADP-macOS.command`（macOS）或執行 `bash UADP-macOS.command`（Linux）
4. 腳本會自動下載初始化引擎並完成設定

**腳本會自動：**
- ✅ 檢查並安裝 Python（如需要）
- ✅ 從 GitHub 下載初始化引擎（如本地不存在）
- ✅ 安裝必要的依賴項（jsonschema）
- ✅ 建立 `.uadp/` 目錄結構（adapters, schemas, logs）
- ✅ 建立 `.cursor/rules/` 目錄與三個核心規則檔案
- ✅ 初始化 `state.json`（設為 PLANNING 階段）
- ✅ 建立 `amendments.md` 與 `decisions.md` 模板

**💡 零門檻特色：**
- **無需 Git Clone**：只需下載一個啟動檔即可
- **自動下載**：初始化引擎會自動從 GitHub 下載
- **完全獨立**：即使在空白資料夾中也能正常運作

**完成後，直接在 Cursor 中啟動蘇格拉底模式：**

#### 方式二：手動安裝

如果你需要更多控制，也可以手動複製檔案：

```bash
# 複製核心規則
cp -r .cursor/rules/ /path/to/your/project/.cursor/

# 複製 UADP 框架
cp -r .uadp/adapters/ /path/to/your/project/.uadp/
cp -r .uadp/schemas/ /path/to/your/project/.uadp/
cp -r scripts/ /path/to/your/project/

# 建立初始檔案
mkdir -p /path/to/your/project/.uadp/logs
touch /path/to/your/project/.uadp/state.json
touch /path/to/your/project/.uadp/contract.json
touch /path/to/your/project/.uadp/amendments.md
```

---

### 啟動蘇格拉底模式

告訴 AI：

```
[MODE: ARCHITECT] 我想做一個 [你的專案想法]
```

AI 會用蘇格拉底詰問法問你問題，幫你把模糊的想法變成清楚的規格。

---

## 📖 使用流程

### 階段 1：PLANNING（規劃）

**角色：** [MODE: ARCHITECT]

**任務：**
- 使用蘇格拉底詰問法釐清需求
- 區分「核心約束」與「技術自由度」
- 產出 `.uadp/contract.json`

**產出：** 契約文件（明確的需求規格）

---

### 階段 2：DIAGNOSIS（診斷）

**角色：** 自動執行

**任務：**
- 檢查當前技術棧、依賴項、環境變數
- 自動偵測適配器（Flutter/React/Backend）
- 產出環境狀態報告

**產出：** 診斷報告與摘要

---

### 階段 3：IMPLEMENTATION（實作）

**角色：** [MODE: QA] → [MODE: CODER] 循環

**任務：**
- QA 先產出測試檔案（記錄 Hash）
- Coder 實作代碼（通過測試）
- 遇到技術障礙時觸發自主修正協議

**產出：** 通過驗證的原始碼

---

### 階段 4：AUDIT（審計）

**角色：** [MODE: AUDITOR]

**任務：**
- 產出白話報告（非技術使用者可理解）
- 列出所有自主修正項
- 生成 Preview（截圖/可執行環境）

**產出：** 審計報告與 Preview

---

## 🔀 混合開發模式 (Hybrid Mode)

### 什麼是混合開發模式？

混合開發模式讓你可以**同時使用 ChatGPT/Gemini 與 Cursor IDE**，發揮兩者的優勢：

- **ChatGPT/Gemini**：作為「外部協調員」，協助需求釐清與白話溝通
- **Cursor IDE**：作為「實作引擎」，執行代碼生成與測試驗證

### 為什麼需要混合模式？

1. **更好的需求釐清**：ChatGPT/Gemini 擅長蘇格拉底詰問，能更深入地理解需求
2. **白話溝通**：非技術使用者更容易理解 ChatGPT/Gemini 的說明
3. **專業實作**：Cursor IDE 的 AI 具備完整的專案上下文，實作更精準

### 如何設定混合模式？

#### 步驟 1：上傳外部引導協議

1. 開啟 ChatGPT 或 Gemini
2. 上傳 `.uadp/UADP_EXTERNAL_PILOT.md` 檔案
3. 告訴 AI：「請閱讀這份文件，你現在是 UADP 外部協調員」

**檔案位置：**
- 初始化後，檔案位於：`.uadp/UADP_EXTERNAL_PILOT.md`
- 或從 GitHub 下載：[UADP_EXTERNAL_PILOT.md](https://raw.githubusercontent.com/OG-Matcha/UADP/main/.uadp/UADP_EXTERNAL_PILOT.md)

#### 步驟 2：標準作業流程 (SOP)

**完整流程：**

```
1. 在 ChatGPT/Gemini 中描述需求
   ↓
2. ChatGPT/Gemini 進行蘇格拉底詰問
   ↓
3. ChatGPT/Gemini 產出 [TO CURSOR] 代碼塊
   ↓
4. 複製代碼塊到 Cursor IDE
   ↓
5. Cursor 執行並產出結果
   ↓
6. 複製結果回到 ChatGPT/Gemini
   ↓
7. ChatGPT/Gemini 解讀結果並以白話說明
   ↓
8. 根據結果決定下一步
   ↓
9. 重複步驟 3-8，直到專案完成
```

#### 步驟 3：範例對話

**在 ChatGPT/Gemini 中：**

```
使用者：「我想做一個待辦事項 App」

ChatGPT/Gemini（外部協調員）：
「好的，讓我先了解一下你的需求：
1. 這個 App 的主要使用者是誰？（個人使用？團隊協作？）
2. 需要哪些核心功能？（新增、刪除、編輯？提醒？分類？）
3. 有什麼技術限制嗎？（必須用 Flutter？必須離線可用？）」

使用者：「個人使用，需要新增、刪除、編輯，還有分類功能。必須用 Flutter，要離線可用。」

ChatGPT/Gemini（外部協調員）：
「明白了！現在請將以下代碼塊複製到 Cursor IDE 中：」

[TO CURSOR]

請切換至 [MODE: ARCHITECT] 模式。

專案需求摘要：
- 專案類型：待辦事項 App
- 目標使用者：個人使用者
- 核心功能：
  - 新增、刪除、編輯待辦事項
  - 標記完成狀態
  - 分類管理（工作、個人、購物）
- 技術約束：
  - 必須使用 Flutter
  - 必須支援離線使用
- 技術自由度：
  - 狀態管理方案：可選（Provider、Riverpod、Bloc）
  - UI 風格：可選（Material Design、自訂設計）

請開始蘇格拉底詰問，並產出 contract.json。
```

**在 Cursor IDE 中：**

```
Cursor AI（ARCHITECT 模式）：
「好的，讓我再確認一些細節：
1. 分類是固定的（工作、個人、購物），還是可以自訂？
2. 需要提醒功能嗎？（推播通知？）
3. 資料儲存在哪裡？（本地 SQLite？雲端同步？）」

...（繼續蘇格拉底詰問）...

「已完成 contract.json，請查看 .uadp/contract.json」
```

**回到 ChatGPT/Gemini：**

```
使用者：「Cursor 說已完成 contract.json」

ChatGPT/Gemini（外部協調員）：
「✅ 太好了！需求釐清階段已完成。Cursor 已經產出了專案契約文件。

下一步：請將以下代碼塊複製到 Cursor IDE 中，開始環境診斷：」

[TO CURSOR]

請切換至 [MODE: CODER] 模式。

任務：執行環境診斷
- 檢查 Flutter SDK 版本
- 檢查依賴項是否正確安裝
- 檢查專案結構是否符合 Flutter 規範

請產出診斷報告。
```

### 關鍵檔案格式

#### [TO CURSOR] 代碼塊格式

**必須包含：**
- 角色切換指令（如：`[MODE: ARCHITECT]`）
- 明確的任務描述
- 必要的上下文資訊

**範例：**

```markdown
[TO CURSOR]

請切換至 [MODE: ARCHITECT] 模式。

專案需求：[描述]
請開始蘇格拉底詰問，並產出 contract.json。
```

#### 回傳結果解讀

**ChatGPT/Gemini 會：**
- ✅ 翻譯技術術語為白話
- ✅ 識別問題並建議解決方案
- ✅ 確認進度並引導下一步

**範例：**

```
Cursor 回傳：
```
✓ Flutter SDK version: 3.16.0
✓ Dependencies installed
✓ Project structure valid
```

ChatGPT/Gemini（外部協調員）：
「✅ 環境診斷完成！Flutter 開發環境已正確安裝，所有依賴項都已就緒，專案結構也符合規範。現在可以開始開發了！」

下一步：請產出 [TO CURSOR] 要求進入實作階段。
```

### 注意事項

- ✅ **主動詢問**：當需求不明確時，ChatGPT/Gemini 會主動使用蘇格拉底詰問法
- ✅ **確認理解**：在產出 [TO CURSOR] 前，ChatGPT/Gemini 會確認理解使用者的需求
- ✅ **追蹤進度**：ChatGPT/Gemini 會記錄當前階段，確保流程不跳躍
- ✅ **白話翻譯**：ChatGPT/Gemini 始終以非技術者能理解的語言說明

### 相關文件

- [外部引導協議完整文件](.uadp/UADP_EXTERNAL_PILOT.md) - 給 ChatGPT/Gemini 的詳細指令手冊

---

## 📁 專案結構

```
your-project/
├── .uadp/                    # UADP 框架目錄
│   ├── state.json            # 狀態機（由 AI 管理）
│   ├── contract.json         # 契約文件（PLANNING 階段產出）
│   ├── amendments.md         # 自主修正紀錄
│   ├── adapters/             # 適配器模板（核心資產）
│   ├── schemas/              # JSON Schema（核心資產）
│   └── logs/                 # 決策紀錄
├── .cursor/rules/            # Cursor Rules（核心資產）
│   ├── uadp-core.mdc
│   ├── uadp-agent-roles.mdc
│   ├── uadp-qa-standard.mdc
│   └── uadp-task-runner.mdc
└── scripts/                  # 工具腳本（核心資產）
    ├── setup_doctor.py
    └── validate_schema.py
```

詳細結構請參考 [FILE_STRUCTURE.md](.uadp/FILE_STRUCTURE.md)

---

## 🎓 學習資源

### 文件

- [快速啟動指南（小白專用）](.uadp/QUICK_START_GUIDE.md) - 圖解步驟，零技術門檻 ⭐
- [白話使用者指南](.uadp/user_guide_plain.md) - 給非技術使用者的簡單說明
- [檔案架構說明](.uadp/FILE_STRUCTURE.md) - 完整的檔案結構與說明
- [Preview 格式提案](.uadp/preview_format_proposal.md) - Preview 格式定義
- [白話翻譯模板](.uadp/plain_language_template.md) - 技術變更的白話翻譯模板

### 規則檔案

- [uadp-core.mdc](.cursor/rules/uadp-core.mdc) - 核心規則與狀態機
- [uadp-agent-roles.mdc](.cursor/rules/uadp-agent-roles.mdc) - 角色行為定義
- [uadp-qa-standard.mdc](.cursor/rules/uadp-qa-standard.mdc) - QA 標準與測試鎖定
- [uadp-task-runner.mdc](.cursor/rules/uadp-task-runner.mdc) - 任務驅動協議與鏈式執行

---

## 🔧 進階使用

### 自訂適配器

技術領導者可以建立自訂適配器：

1. 在 `.uadp/adapters/` 建立新的 `.mdc` 檔案
2. 定義技術棧特定的規則與最佳實踐
3. 在 `setup_doctor.py` 中新增自動偵測邏輯

### 擴展規則

可以新增自訂規則檔案到 `.cursor/rules/`，但需注意：
- 保持與核心規則的一致性
- 遵循 UADP 的設計原則
- 記錄決策理由

---

## 🤝 貢獻指南

我們歡迎所有形式的貢獻！

### 如何貢獻

1. Fork 本專案
2. 建立功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交變更 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 開啟 Pull Request

### 貢獻類型

- 🐛 Bug 修復
- ✨ 新功能（適配器、規則擴展）
- 📝 文件改進
- 🧪 測試案例

---

## 📄 授權

本專案採用 MIT 授權。詳見 [LICENSE](LICENSE) 檔案。

---

## 🙏 致謝

- 感謝所有貢獻者的支持
- 靈感來自 Linus Torvalds 的「Good Taste」設計哲學

---

## 📞 聯絡方式

- **Issues**: [GitHub Issues](https://github.com/OG-Matcha/UADP/issues)
- **Discussions**: [GitHub Discussions](https://github.com/OG-Matcha/UADP/discussions)

---

**讓 AI 開發更可靠、更透明、更高效。** 🚀

