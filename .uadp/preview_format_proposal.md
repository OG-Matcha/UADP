# Preview 格式建議草案

> **針對 open_questions 中的「AUDIT 階段的 Preview 具體格式」**  
> **提案時間：** 2025-01-27  
> **提案者：** [MODE: AUDITOR]

---

## 1. Preview 的定義與目的

### 1.1 定義

**Preview** 是 AUDIT 階段產出的「可視化驗收報告」，用於向使用者（特別是非技術使用者）展示專案的完成狀態與功能運作情況。

### 1.2 目的

1. **驗證功能完整性：** 讓使用者確認所有功能都已實作
2. **視覺化展示：** 用圖片、影片或可執行的環境展示成果
3. **快速驗收：** 非技術使用者可以快速理解專案狀態
4. **決策支援：** 幫助使用者決定是否進入下一階段或部署

---

## 2. Preview 格式提案

### 2.1 混合格式（推薦）

**採用多種格式組合，滿足不同使用者的需求：**

#### 格式 A：Markdown 報告 + 截圖（主要格式）

**結構：**
```
.uadp/preview/
├── preview_report.md          # 主要報告（Markdown）
├── screenshots/               # 截圖目錄
│   ├── feature_1.png
│   ├── feature_2.png
│   └── ...
├── execution_log.txt          # 執行日誌（可選）
└── preview_summary.json       # 結構化摘要（可選）
```

**內容：**
- **preview_report.md** 包含：
  - 功能清單與完成狀態
  - 每個功能的截圖與說明
  - 測試執行結果摘要
  - 已知問題與限制

**優點：**
- 人類可讀（Markdown）
- 版本控制友好
- 易於分享與審查

---

#### 格式 B：可執行的預覽環境（進階格式）

**結構：**
```
.uadp/preview/
├── preview_instructions.md   # 預覽說明
├── run_preview.sh             # 啟動腳本（Shell）
└── docker-compose.yml         # Docker 環境（可選）
```

**內容：**
- **preview_instructions.md** 包含：
  - 如何啟動預覽環境
  - 如何存取預覽功能
  - 測試帳號與密碼（如需要）

**優點：**
- 使用者可以實際操作
- 最接近真實環境
- 適合需要互動的專案

---

#### 格式 C：Demo 影片（可選格式）

**結構：**
```
.uadp/preview/
├── demo_video.mp4             # 演示影片
└── demo_script.txt            # 影片腳本（文字版）
```

**內容：**
- 錄製關鍵功能的使用流程
- 包含旁白說明（可選）

**優點：**
- 最直觀的展示方式
- 適合複雜的互動流程
- 非技術使用者最容易理解

**缺點：**
- 檔案較大，不適合版本控制
- 需要額外的錄製工具

---

### 2.2 格式選擇邏輯

**根據專案類型自動選擇：**

| 專案類型 | 推薦格式 | 理由 |
|---------|---------|------|
| Web 應用 | Markdown + 截圖 + 可執行環境 | 需要展示 UI 與互動 |
| 手機 App | Markdown + 截圖 + Demo 影片 | 需要展示多個畫面與流程 |
| 後端 API | Markdown + 執行日誌 + API 文件 | 重點在功能與效能 |
| CLI 工具 | Markdown + 執行日誌 + 範例輸出 | 重點在命令與輸出 |

---

## 3. Preview 內容標準

### 3.1 必須包含的內容

1. **功能清單：** 列出所有已實作的功能與狀態
2. **視覺化證據：** 截圖、影片或執行結果
3. **測試結果摘要：** 測試通過率與覆蓋率
4. **已知問題：** 列出已知的限制與問題

### 3.2 可選內容

1. **效能指標：** 回應時間、記憶體使用等
2. **使用說明：** 如何操作與使用
3. **技術架構圖：** 系統架構說明（技術使用者）

---

## 4. Preview 生成流程

### 4.1 自動生成（推薦）

**在 AUDIT 階段，AI 自動：**
1. 執行所有測試並記錄結果
2. 啟動應用並截圖（Web/App）
3. 執行關鍵功能並記錄輸出（CLI/API）
4. 生成 preview_report.md
5. 產出 preview_summary.json

### 4.2 手動生成（備選）

**如果自動生成失敗：**
1. AI 提供「Preview 生成指南」
2. 使用者手動執行並上傳截圖/影片
3. AI 協助整理成 preview_report.md

---

## 5. Preview 範例結構

### 5.1 preview_report.md 範例

```markdown
# 專案 Preview 報告

> **生成時間：** 2025-01-27  
> **專案名稱：** 記帳 App  
> **階段：** AUDIT

---

## 1. 功能完成度

| 功能 | 狀態 | 截圖 |
|------|------|------|
| 新增記帳 | ✅ 完成 | [screenshots/add_record.png](./screenshots/add_record.png) |
| 查看統計 | ✅ 完成 | [screenshots/statistics.png](./screenshots/statistics.png) |
| 匯出報表 | ⚠️ 部分完成 | [screenshots/export.png](./screenshots/export.png) |

---

## 2. 測試結果

- **單元測試：** 45/50 通過（90%）
- **整合測試：** 12/12 通過（100%）
- **E2E 測試：** 8/10 通過（80%）

---

## 3. 已知問題

1. 匯出功能僅支援 CSV 格式，PDF 格式尚未實作
2. 統計圖表在手機上顯示可能過小

---

## 4. 如何預覽

### 方式 A：執行應用

```bash
flutter run
```

### 方式 B：查看截圖

所有截圖位於 `screenshots/` 目錄

---

## 5. 下一步建議

1. 完成 PDF 匯出功能
2. 優化手機版統計圖表顯示
3. 進行使用者測試
```

---

## 6. 技術實作建議

### 6.1 截圖自動化

**Web 應用：**
- 使用 Playwright 或 Puppeteer 自動截圖
- 在 CI/CD 流程中執行

**手機 App：**
- 使用 Flutter 的 `golden` 測試自動截圖
- 或手動截圖後上傳

### 6.2 執行日誌收集

**後端 API：**
- 記錄所有 API 請求與回應
- 包含效能指標（回應時間、狀態碼）

**CLI 工具：**
- 記錄命令執行與輸出
- 包含錯誤情況的處理

---

## 7. 建議採用的格式

### 7.1 主要格式：Markdown + 截圖

**理由：**
- 最通用，適合所有專案類型
- 版本控制友好
- 易於分享與審查
- 非技術使用者也能理解

### 7.2 輔助格式：可執行環境（如需要）

**理由：**
- 提供實際操作體驗
- 適合需要互動驗證的專案

### 7.3 可選格式：Demo 影片

**理由：**
- 最直觀，但檔案較大
- 建議僅在複雜流程時使用

---

## 8. 更新 contract.json 建議

建議在 `contract.json` 的 `technical_freedom.audit` 中新增：

```json
"preview_format": {
  "primary": "Markdown + Screenshots",
  "secondary": "Executable Environment (optional)",
  "optional": "Demo Video (for complex flows)",
  "structure": {
    "preview_report": ".uadp/preview/preview_report.md",
    "screenshots": ".uadp/preview/screenshots/",
    "execution_log": ".uadp/preview/execution_log.txt",
    "preview_summary": ".uadp/preview/preview_summary.json"
  }
}
```

---

**提案完成時間：** 2025-01-27  
**提案者：** [MODE: AUDITOR]  
**狀態：** 待審查

