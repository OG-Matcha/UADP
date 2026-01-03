# UADP 框架檔案架構

> **最後更新：** 2026-01-04  
> **當前階段：** PLANNING（模板狀態）  
> **版本：** 1.0

---

## 完整目錄結構

```
UADP/
├── .uadp/                          # UADP 框架核心目錄
│   ├── state.json                  # 狀態機（當前階段、歷史記錄）
│   ├── contract.json               # 契約文件（需求、約束、里程碑）
│   ├── amendments.md               # 自主修正紀錄（目前為空）
│   │
│   ├── adapters/                   # 技術棧適配器目錄
│   │   ├── README.md               # 適配器目錄說明
│   │   ├── mobile-flutter.mdc     # Flutter 行動應用適配器
│   │   ├── web-modern.mdc          # React/Vite Web 適配器
│   │   └── backend-api.mdc         # Node.js/Python 後端適配器
│   │
│   ├── schemas/                    # JSON Schema 定義目錄
│   │   ├── state.schema.json       # state.json 的 Schema
│   │   └── contract.schema.json    # contract.json 的 Schema
│   │
│   ├── logs/                       # 決策紀錄目錄
│   │   ├── decisions.md            # 技術決策紀錄
│   │   └── release_v1.0_checklist.md  # v1.0 發布檢查清單（已歸檔）
│   │
│   │
│   ├── FILE_STRUCTURE.md            # 本檔案（核心資產）
│   ├── user_guide_plain.md          # 白話使用者指南（核心資產）
│   ├── preview_format_proposal.md  # Preview 格式建議草案（核心資產）
│   └── plain_language_template.md  # 白話翻譯模板草案（核心資產）
│   │
│   # 以下為執行產出（應被 .gitignore 排除）：
│   # ├── diagnosis_report.md       # DIAGNOSIS 階段產出
│   # ├── diagnosis_summary.json    # DIAGNOSIS 階段產出
│   # ├── audit_report.md            # AUDIT 階段產出
│   # └── preview/                   # AUDIT 階段產出
│
├── .cursor/                        # Cursor IDE 配置目錄
│   └── rules/                      # Cursor Rules 規則檔案
│       ├── uadp-core.mdc           # 核心規則（狀態機、行為準則）
│       ├── uadp-agent-roles.mdc    # 角色行為定義（4 種角色）
│       └── uadp-qa-standard.mdc    # QA 標準與測試鎖定邏輯
│
└── scripts/                         # 輔助工具腳本目錄
    ├── setup_doctor.py             # 環境診斷工具
    └── validate_schema.py          # JSON Schema 驗證工具
```

---

## 檔案說明

### 核心配置檔案

#### `.uadp/state.json`
- **用途：** 狀態機，記錄當前 SDLC 階段與歷史
- **關鍵欄位：**
  - `current_phase`: 當前階段（PLANNING/DIAGNOSIS/IMPLEMENTATION/AUDIT）
  - `phase_history`: 階段歷史記錄
  - `completed_steps`: 已完成步驟列表
  - `test_hashes`: 測試檔案 Hash 記錄（測試鎖定機制）

#### `.uadp/contract.json`
- **用途：** 契約文件，定義專案需求、約束與里程碑
- **關鍵區塊：**
  - `metadata`: 專案名稱、技術棧、目標使用者
  - `requirements.hard_constraints`: 核心約束（不可變）
  - `requirements.technical_freedom`: 技術自由度
  - `milestones`: 階段性任務與驗收標準
  - `open_questions`: 待解決問題（已全部解決）

#### `.uadp/amendments.md`
- **用途：** 記錄所有未經使用者預先核准的技術變更
- **格式：** `[AMENDMENT] 原因: <描述> | 做法: <方案> | 影響: <對功能的改變>`
- **目前狀態：** 空（所有變更均經過確認）

---

### 規則檔案（`.cursor/rules/`）

#### `uadp-core.mdc`
- **用途：** 核心規則，定義 SDLC 狀態機與核心行為準則
- **內容：**
  - 系統聲明
  - 開發生命週期（4 個階段）
  - 自主修正協議
  - 測試鎖定機制
  - 角色定義與轉換指令
  - 檔案操作與記憶規範

#### `uadp-agent-roles.mdc`
- **用途：** 定義 4 種角色的行為規範
- **角色：**
  - `[MODE: ARCHITECT]`: 架構師（禁止寫代碼）
  - `[MODE: CODER]`: 工程師（禁止修改測試）
  - `[MODE: QA]`: 測試員（禁止修改實作）
  - `[MODE: AUDITOR]`: 審計員（禁止實作與測試）

#### `uadp-qa-standard.mdc`
- **用途：** QA 標準與測試鎖定邏輯
- **內容：**
  - 測試鎖定機制（雜湊鎖定）
  - 測試生成標準（邊界、錯誤路徑、UI、整合）
  - 測試框架選擇
  - 違規檢測與處理

---

### 適配器（`.uadp/adapters/`）

#### `mobile-flutter.mdc`
- **用途：** Flutter 行動應用適配器
- **觸發條件：** 偵測到 `pubspec.yaml`
- **內容：** 測試框架配置、編碼規範、最佳實踐

#### `web-modern.mdc`
- **用途：** React/Vite Web 適配器
- **觸發條件：** 偵測到 `package.json` 且包含 `react` 與 `vite`
- **內容：** 測試框架配置、組件設計、狀態管理

#### `backend-api.mdc`
- **用途：** Node.js/Python 後端適配器
- **觸發條件：** 偵測到 `package.json` 或 `requirements.txt`
- **內容：** 測試框架配置、API 設計原則、安全性最佳實踐

---

### JSON Schema（`.uadp/schemas/`）

#### `state.schema.json`
- **用途：** 驗證 `state.json` 的結構與類型
- **驗證項目：** 階段枚舉、時間格式、必要欄位

#### `contract.schema.json`
- **用途：** 驗證 `contract.json` 的結構與類型
- **驗證項目：** 契約版本、metadata、requirements、milestones

---

### 工具腳本（`scripts/`）

#### `setup_doctor.py`
- **用途：** 環境診斷工具
- **功能：**
  - 讀取 `contract.json` 並執行診斷
  - 檢查檔案結構、依賴項、contract 結構
  - 自動偵測適配器
  - 產出 `diagnosis_report.md` 與 `diagnosis_summary.json`
- **執行：** `python scripts/setup_doctor.py`

#### `validate_schema.py`
- **用途：** JSON Schema 驗證工具
- **功能：** 驗證 `state.json` 與 `contract.json` 是否符合 Schema
- **執行：** `python scripts/validate_schema.py`（需要 `jsonschema` 庫）

---

### 報告與文件

#### `.uadp/diagnosis_report.md`
- **用途：** 環境診斷報告（DIAGNOSIS 階段產出）
- **內容：** 環境資訊、檢查結果、診斷範圍檢測清單

#### `.uadp/diagnosis_summary.json`
- **用途：** 診斷摘要（結構化資料）
- **內容：** 機器可讀的診斷結果

#### `.uadp/audit_report.md`
- **用途：** 最終審計報告（AUDIT 階段產出）
- **內容：** 階段完成度、技術決策審查、交付物清單、品質指標

#### `.uadp/user_guide_plain.md`
- **用途：** 白話使用者指南（非技術使用者）
- **內容：** 框架說明、能力介紹、使用步驟、常見問題

#### `.uadp/preview_format_proposal.md`
- **用途：** Preview 格式建議草案
- **內容：** Preview 定義、格式提案、生成流程

#### `.uadp/plain_language_template.md`
- **用途：** 白話翻譯模板草案
- **內容：** 5 種翻譯模板、翻譯流程、品質檢查清單

---

### 決策紀錄

#### `.uadp/logs/decisions.md`
- **用途：** 記錄重大技術決策與選擇理由
- **內容：** 決策時間、決策內容、決策理由、參考文件

---

## 檔案統計

| 類別 | 檔案數量 | 說明 |
|------|---------|------|
| 核心配置 | 3 | state.json, contract.json, amendments.md |
| 規則檔案 | 3 | uadp-core.mdc, uadp-agent-roles.mdc, uadp-qa-standard.mdc |
| 適配器 | 4 | 3 個適配器 + README.md |
| JSON Schema | 2 | state.schema.json, contract.schema.json |
| 工具腳本 | 2 | setup_doctor.py, validate_schema.py |
| 報告文件 | 6 | 診斷報告、審計報告、使用者指南、提案草案 |
| 決策紀錄 | 1 | decisions.md |
| **總計** | **21** | |

---

## 檔案關係圖

```
state.json (狀態機)
    ↓
contract.json (契約)
    ↓
.cursor/rules/ (規則檔案)
    ├── uadp-core.mdc (核心規則)
    ├── uadp-agent-roles.mdc (角色定義)
    └── uadp-qa-standard.mdc (QA 標準)
    ↓
.uadp/adapters/ (適配器)
    ├── mobile-flutter.mdc
    ├── web-modern.mdc
    └── backend-api.mdc
    ↓
scripts/ (工具)
    ├── setup_doctor.py (診斷)
    └── validate_schema.py (驗證)
    ↓
.uadp/schemas/ (Schema)
    ├── state.schema.json
    └── contract.schema.json
```

---

## 檔案修改建議

### 可修改檔案
- ✅ `.uadp/adapters/*.mdc` - 可自訂適配器
- ✅ `.cursor/rules/*.mdc` - 可擴展規則（需謹慎）
- ✅ `scripts/*.py` - 可擴展工具功能

### 不建議修改檔案
- ⚠️ `.uadp/state.json` - 由 AI 自動管理
- ⚠️ `.uadp/contract.json` - 應透過 PLANNING 階段更新
- ⚠️ `.uadp/schemas/*.json` - Schema 變更需同步更新驗證邏輯

---

**最後更新：** 2026-01-04  
**維護者：** UADP Framework

