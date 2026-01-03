# UADP 框架資產清單

> **最後更新：** 2025-01-27  
> **用途：** 區分核心框架資產與專案特定執行產出

---

## ✅ 核心框架資產（應提交至 Git）

這些檔案是框架的核心部分，應該被版本控制追蹤。

### 規則檔案（`.cursor/rules/`）

| 檔案 | 狀態 | 說明 |
|------|------|------|
| `uadp-core.mdc` | ✅ 核心資產 | 核心規則（狀態機、行為準則） |
| `uadp-agent-roles.mdc` | ✅ 核心資產 | 角色行為定義（4 種角色） |
| `uadp-qa-standard.mdc` | ✅ 核心資產 | QA 標準與測試鎖定邏輯 |

### 適配器模板（`.uadp/adapters/`）

| 檔案 | 狀態 | 說明 |
|------|------|------|
| `README.md` | ✅ 核心資產 | 適配器目錄說明 |
| `mobile-flutter.mdc` | ✅ 核心資產 | Flutter 行動應用適配器 |
| `web-modern.mdc` | ✅ 核心資產 | React/Vite Web 適配器 |
| `backend-api.mdc` | ✅ 核心資產 | Node.js/Python 後端適配器 |

### JSON Schema（`.uadp/schemas/`）

| 檔案 | 狀態 | 說明 |
|------|------|------|
| `state.schema.json` | ✅ 核心資產 | state.json 的 Schema |
| `contract.schema.json` | ✅ 核心資產 | contract.json 的 Schema |

### 工具腳本（`scripts/`）

| 檔案 | 狀態 | 說明 |
|------|------|------|
| `setup_doctor.py` | ✅ 核心資產 | 環境診斷工具 |
| `validate_schema.py` | ✅ 核心資產 | JSON Schema 驗證工具 |

### 文件與模板（`.uadp/`）

| 檔案 | 狀態 | 說明 |
|------|------|------|
| `FILE_STRUCTURE.md` | ✅ 核心資產 | 檔案架構說明 |
| `user_guide_plain.md` | ✅ 核心資產 | 白話使用者指南 |
| `preview_format_proposal.md` | ✅ 核心資產 | Preview 格式建議草案 |
| `plain_language_template.md` | ✅ 核心資產 | 白話翻譯模板草案 |

### 根目錄檔案

| 檔案 | 狀態 | 說明 |
|------|------|------|
| `README.md` | ✅ 核心資產 | 專案說明文件 |
| `.gitignore` | ✅ 核心資產 | Git 忽略規則 |

---

## 📝 模板檔案（應提交至 Git，但內容為空）

這些檔案是模板，使用者專案會產生自己的內容。

| 檔案 | 狀態 | 說明 |
|------|------|------|
| `.uadp/state.json` | ✅ 模板 | 狀態機模板（current_phase: PLANNING） |
| `.uadp/contract.json` | ⚠️ 注意 | 此檔案在框架中不存在，由使用者專案生成 |
| `.uadp/amendments.md` | ✅ 模板 | 自主修正紀錄模板（僅格式，無內容） |
| `.uadp/logs/decisions.md` | ✅ 模板 | 技術決策紀錄模板（僅格式，無內容） |

**注意：** `contract.json` 在框架倉庫中不存在，因為它是專案特定的契約文件。

---

## ❌ 執行產出（應被 .gitignore 排除）

這些檔案是專案執行過程中產生的，不應提交至 Git。

### DIAGNOSIS 階段產出

| 檔案 | 狀態 | 說明 |
|------|------|------|
| `.uadp/diagnosis_report.md` | ❌ 執行產出 | 環境診斷報告 |
| `.uadp/diagnosis_summary.json` | ❌ 執行產出 | 診斷摘要（結構化資料） |

### AUDIT 階段產出

| 檔案 | 狀態 | 說明 |
|------|------|------|
| `.uadp/audit_report.md` | ❌ 執行產出 | 最終審計報告 |
| `.uadp/preview/` | ❌ 執行產出 | Preview 目錄（截圖、影片等） |
| `.uadp/preview_report.md` | ❌ 執行產出 | Preview 報告 |
| `.uadp/preview_summary.json` | ❌ 執行產出 | Preview 摘要 |
| `.uadp/plain_language_report.md` | ❌ 執行產出 | 白話報告（專案特定） |

### 其他執行產出

| 檔案 | 狀態 | 說明 |
|------|------|------|
| `.uadp/execution_log.txt` | ❌ 執行產出 | 執行日誌 |

---

## 📊 統計摘要

| 類別 | 數量 | 說明 |
|------|------|------|
| **核心規則檔案** | 3 | 核心框架規則 |
| **適配器模板** | 4 | 技術棧適配器 |
| **JSON Schema** | 2 | 資料驗證 Schema |
| **工具腳本** | 2 | 診斷與驗證工具 |
| **文件與模板** | 5 | 說明文件與模板 |
| **模板檔案** | 3 | 空模板（state.json, amendments.md, decisions.md） |
| **執行產出** | 7+ | 專案執行產出（應被忽略） |
| **總核心資產** | **19** | 應提交至 Git |

---

## 🔍 驗證檢查清單

在提交至 Git 前，請確認：

- [ ] 所有核心規則檔案（`.cursor/rules/*.mdc`）已提交
- [ ] 所有適配器模板（`.uadp/adapters/*.mdc`）已提交
- [ ] 所有 JSON Schema（`.uadp/schemas/*.json`）已提交
- [ ] 所有工具腳本（`scripts/*.py`）已提交
- [ ] 所有文件（`README.md`, `.uadp/*.md`）已提交
- [ ] `.gitignore` 已正確配置，排除執行產出
- [ ] `state.json` 已重置為模板狀態（PLANNING）
- [ ] `amendments.md` 已重置為模板狀態（僅格式）
- [ ] `decisions.md` 已重置為模板狀態（僅格式）
- [ ] 所有執行產出（診斷報告、審計報告等）已被 `.gitignore` 排除

---

**最後更新：** 2025-01-27  
**維護者：** UADP Framework

