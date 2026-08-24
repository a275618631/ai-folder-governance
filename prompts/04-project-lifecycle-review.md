# 04 — Project lifecycle review

Use this prompt to review project identities and lifecycle status without immediately merging, archiving, or deleting anything.

## English prompt

Review the explicitly listed project roots `<PROJECTS>` using `PROJECT_LIFECYCLE_REVIEW`.

For each project, inspect read-only and produce:

1. stable identity signals: project ID, display name, owner, workspace locations, and cross-references;
2. purpose and current activity evidence;
3. canonical-source candidates for code, decisions, documents, tests, and releases;
4. relationship to other projects, including a possible merge candidate;
5. lifecycle label: `active`, `related`, `historical`, `archive`, `duplicate`, or `delete-candidate`;
6. confidence, conflicting evidence, and material questions;
7. a non-destructive recommendation and post-condition.

### Safety rules

- A similar name or topic does not prove duplicate identity.
- Do not merge projects, move roots, archive material, overwrite a source, or delete a candidate during review.
- Treat credentials, private configuration, session data, and sensitive content as opaque.
- Do not resolve a conflict by choosing the newest or largest folder without authority evidence.
- A `delete-candidate` label is a review outcome, not deletion permission.
- Ask only questions that could change the lifecycle label, canonical source, scope, or risk.

Return a decision table and a proposed next-step change set. Wait for explicit, item-specific approval before any mutation. After approved execution, validate identity references, source-of-truth declarations, cross-project links, retention outcomes, and the absence of out-of-scope changes.

## 繁體中文提示詞

使用 `PROJECT_LIFECYCLE_REVIEW`，只審查明確列出的 `<PROJECTS>`，不要立即合併、封存或刪除。

每個專案先唯讀檢查並回傳：stable identity 訊號（project ID、display name、owner、工作區位置與互相參照）、用途與目前活動證據、code/decision/document/test/release 的 canonical source candidate、與其他專案的關係及 merge candidate、生命週期標籤 `active`、`related`、`historical`、`archive`、`duplicate` 或 `delete-candidate`、信心度與衝突、重大問題、非破壞性建議及 post-condition。

相似名稱或主題不能證明 duplicate identity。審查時不可合併專案、移動根目錄、封存、覆寫來源或刪除候選項目。秘密、私人設定、工作階段資料與敏感內容視為 opaque。不可只因某資料夾較新或較大就判定權威性；`delete-candidate` 不是刪除許可。

回傳 decision table 與下一步 change set，等待逐項明確核准。執行後驗證 identity 參照、source-of-truth 宣告、跨專案連結、保留結果與範圍外沒有變更。
