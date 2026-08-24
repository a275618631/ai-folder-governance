# 5. Prompt 指南

Prompt Pack 適用於可以檢查檔案系統、連線文件工作區或使用者提供 inventory 的 Agent。每個 Prompt 都能脫離 Skill 單獨使用。

每份 Prompt 頂端都說明：實際交給 Agent 時，只需複製你要使用的語言區段。

## 選擇 Prompt

| Prompt | 適用情境 |
| --- | --- |
| [01-single-folder-deep-organize](../../prompts/01-single-folder-deep-organize.md) | 需要仔細深度檢視一個資料夾。 |
| [02-multi-folder-maintenance](../../prompts/02-multi-folder-maintenance.md) | 多個資料夾需要增量維護。 |
| [03-web-review-and-local-handoff](../../prompts/03-web-review-and-local-handoff.md) | 一個 Agent 遠端盤點，另一個 Agent 執行本機變更。 |
| [04-project-lifecycle-review](../../prompts/04-project-lifecycle-review.md) | 專案資料夾需要生命週期判斷。 |
| [05-project-workspace-governance](../../prompts/05-project-workspace-governance.md) | 一個專案跨越人類與機器工作區。 |

## 改寫 Prompt 時必須保留

- 指定 target 與 scope；
- 先做唯讀檢視；
- 根據內容、所有權、權威性與相依性分類；
- 區分事實、推論與 unresolved questions；
- 明確選擇模式；
- 產出 dry-run change set；
- 在重大歧義與變更前詢問或等待核准；
- 保護秘密與路徑相依性；
- 驗證 post-condition 並回報維持不動的項目；
- 讓第二次執行接近 no-op。

## 安全提供上下文

只提供 target 描述、相關偏好與最小必要 inventory。不要將憑證內容、私人連結、工作階段資料或無關個資貼入 Prompt。若 Agent 無法安全檢查相依性，應要求它維持該項目不動。

## 審查回應

好的回應應分開列出 inventory、推理與不確定性、建議 change set、驗證報告。若回應直接跳到「完成」、隱藏假設，或把檔名當作 canonical 證明，應拒絕該結果。

如果 Host Runtime 沒有寫入或獨立驗證能力，Prompt 應停在 `PLAN_READY`，並說明缺少的能力。
