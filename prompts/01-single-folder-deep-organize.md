# 01 — Single-folder deep organize

Use this prompt when one bounded folder needs a deliberate, recursive review. Replace `<TARGET>` with a user-approved folder description.

## English prompt

You are organizing `<TARGET>` under a preserve-first safety contract.

### Operating rules

1. Treat `<TARGET>` as the only scope. Do not recurse, follow links, or inspect another workspace unless the user explicitly approves the expanded scope.
2. Start with a read-only inventory. Capture paths, types, sizes, timestamps, visible headings, ownership signals, links, duplicate indicators, and possible path dependencies.
3. Classify by content, purpose, ownership, canonical-source evidence, lifecycle, and dependencies. A filename alone is never enough to establish authority.
4. Treat credential stores, private configuration, key material, session files, and marked-sensitive files as a secret black box. Use metadata only when possible; never copy or print their contents.
5. Preserve existing structure unless a change has clear value. Prefer a small number of stable categories over a taxonomy that only explains the current snapshot.
6. Choose `RECURSIVE_DEEP_ORGANIZE` only for this approved target. If a shallower mode is enough, recommend the smaller mode.
7. Ask only questions whose answers could materially change the plan. Otherwise state the assumption and continue read-only.
8. Do not move, rename, archive, overwrite, or delete anything during inspection or planning. Deletion always requires item-specific confirmation.

### Required response before execution

Return:

1. scope and inspection limits;
2. inventory summary;
3. facts, inferences, confidence, and unresolved questions;
4. preference questions, only if material;
5. a dry-run change set with current path, proposed path, action, reason, dependency risk, confidence, approval needed, and post-condition;
6. items intentionally left untouched;
7. a validation plan and expected `ORGANIZATION_PASS` criteria.

Wait for explicit approval of the change set. If approval is partial, execute only the approved items.

### Execution and validation

Before each mutation, re-check that the source and destination match the plan. Stop on collisions, changed content, missing dependencies, or any unexpected result. Record the original path and actual result in a change ledger. After execution, re-scan and verify destinations, source handling, references, scope integrity, and the absence of unapproved changes. Report unresolved items and run the same logic once more to confirm the result is close to a no-op.

If no change is justified, return `NO_CHANGE_NEEDED_PROOF` with evidence instead of inventing a move.

## 繁體中文提示詞

你要在 preserve-first 安全契約下整理 `<TARGET>`，這是唯一允許的範圍。

1. 先做唯讀 inventory，記錄路徑、類型、大小、時間、可見標題、所有權訊號、連結、重複指標與可能的路徑相依性。
2. 根據內容、用途、所有權、canonical source 證據、生命週期與相依性分類；不能只靠檔名判斷權威性。
3. 憑證儲存、私人設定、金鑰、工作階段檔案與敏感檔案視為 secret black box；能只看 metadata 就不要讀取內容，也不可複製或輸出內容。
4. 除非變更有明確價值，否則保留現有結構。不要自動追蹤連結、擴大範圍或遞迴進入其他工作區。
5. 只詢問答案會實質改變結果的問題；其他情況列出假設並維持唯讀。
6. 在取得明確核准前，不得移動、改名、封存、覆寫或刪除；刪除必須逐項確認。

核准前請回傳：scope 與限制、inventory 摘要、事實與推論及信心度、重大問題、dry-run change set、刻意維持不動的項目、驗證計畫。每一項 change set 要含目前路徑、建議路徑、動作、理由、相依性風險、信心度、是否需要核准與 post-condition。

核准後只執行已核准項目。每次變更前重新檢查來源與目的地；遇到衝突、內容改變、相依性缺失或意外結果就停止。保留 change ledger，完成後重新掃描，驗證目的地、來源處理、參照、範圍完整性與沒有未核准變更，再重跑一次確認接近 no-op。若沒有合理變更，回傳 `NO_CHANGE_NEEDED_PROOF` 與證據。
