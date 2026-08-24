# 02 — Multi-folder incremental maintenance

Use this prompt for routine maintenance across an explicitly listed set of folders. Replace `<TARGETS>` and `<RECENTNESS_RULE>` before use.

**English:** Copy only the language section you intend to use.

**繁中：** 實際交給 Agent 時，只需複製你要使用的語言區段，不需要同時貼英文與中文。

## English prompt

Review only `<TARGETS>`. Use `INCREMENTAL_MAINTENANCE` and `<RECENTNESS_RULE>` to limit work to new or recently changed items.

### Rules

- Inventory read-only before proposing any change. Do not treat a prior inventory as permission to mutate.
- Do not expand the folder list, recurse into unlisted folders, or follow links into other workspaces.
- Compare current metadata with the last approved ledger when one is available. If there is no trusted baseline, say so and use the current scan only.
- Classify additions and changes by content, ownership, canonical-source evidence, lifecycle, and path dependencies.
- Preserve existing structure. A maintenance run should not redesign a folder because one new item is awkward.
- Keep secrets, credential stores, private configuration, and unresolved path-dependent items untouched.
- Ask only material preference questions. Default destructive deletion to confirmation and do not delete duplicates automatically.
- Wait for explicit approval before moving, renaming, archiving, overwriting, or deleting.

### Output

Return a per-folder summary with: inspected boundary, included items, skipped items and why, new or changed signals, proposed actions, confidence, material questions, and a consolidated dry-run change set. Mark each item `no-change`, `needs-review`, or `approved-candidate`; none is approved merely by the label.

After approval, execute only approved entries. Re-check each pre-condition, maintain a ledger, stop on unexpected collisions, and validate that no folder outside `<TARGETS>` changed. Report `ORGANIZATION_PASS`, `PARTIAL_WITH_UNRESOLVED_ITEMS`, or `NO_CHANGE_NEEDED_PROOF`. A later maintenance run should not re-propose the same change without new evidence.

## 繁體中文提示詞

只檢視明確列出的 `<TARGETS>`，使用 `INCREMENTAL_MAINTENANCE` 與 `<RECENTNESS_RULE>`，只處理新增或近期變動項目。

先唯讀 inventory，再提出 change set。不可擴大資料夾清單、遞迴未列出的資料夾，或沿連結進入其他工作區。若有上次核准的 ledger，才可與它比較；沒有可信 baseline 就明確說明，只依本次 scan 判斷。

依內容、所有權、canonical source 證據、生命週期與路徑相依性分類。保留既有結構，不因一個新項目就重設計整個資料夾。秘密、憑證儲存、私人設定與未解決的路徑相依項目維持不動。只問會實質改變結果的偏好；刪除預設要確認，不能自動刪除 duplicate。

核准前不得移動、改名、封存、覆寫或刪除。回傳每個資料夾的邊界、納入與略過項目、變動訊號、建議動作、信心度、重大問題與合併後的 dry-run change set。核准後只執行已核准項目，重新檢查前置條件、維持 ledger、遇到衝突即停止，並驗證範圍外沒有變更。回報 `ORGANIZATION_PASS`、`PARTIAL_WITH_UNRESOLVED_ITEMS` 或 `NO_CHANGE_NEEDED_PROOF`。
