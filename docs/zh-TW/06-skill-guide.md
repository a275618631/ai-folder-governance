# 6. Skill 指南

內含 Skill 是 Agent Skills 相容 Runtime 的入口。它刻意保持精簡，讓 Agent 能逐步載入必要的詳細指引。

套件遵循 [Agent Skills specification](https://agentskills.io/specification)。官方格式以 `SKILL.md` 為核心，並可選擇包含 references 與 assets 等資源。

## 套件形狀

```text
skills/ai-folder-governance/
├── SKILL.md
├── references/
└── assets/
```

資料夾名稱與 YAML front matter 的 `name` 都是 `ai-folder-governance`。

## 安裝

把完整的 `skills/ai-folder-governance/` 目錄複製到 Agent Runtime 支援的 skills 目錄，保留資料夾名稱。不要把私人設定或產生的報告複製進 Skill 套件。

## 啟用與路由

當使用者要檢查、分類、整理、改名、封存或治理資料夾與專案工作區時，應啟用 Skill。依任務路由：

- 所有整理要求都讀 core rules；
- 讀取內容或變更前讀 safety invariants；
- 選擇會改變計畫時讀 preference discovery；
- 決定範圍與深度時讀 organization modes；
- 執行前後讀 acceptance gates；
- 只有跨工作區的專案 identity 才讀 project-workspaces。

不要每次都載入所有 reference；reference 是維護細節，`SKILL.md` 是啟用與流程契約。

## Runtime 預期

Skill 不假設特定提供者、Shell、檔案 API 或語言。Host Agent 必須把唯讀檢查、核准、執行與驗證翻譯成自身可用工具。如果能力不存在，應回報限制，不能假裝成功。

請使用 [Runtime 能力](08-runtime-capabilities.md) 區分 `Tested`、`Designed for` 與 `Format compatible`；本 Repository 不宣稱所有 Agent 都支援。

## 測試 Skill 變更

執行 Repository validator。若行為有實質變化，以虛構資料夾測試：包含一個有歧義的 duplicate、一個有路徑相依性的檔案，以及一個看起來像秘密的檔案。確認 Skill 會安全處理、在變更前等待核准，並回報 unresolved items。
