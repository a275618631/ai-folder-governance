# 05 — Project workspace governance

Use this optional advanced prompt when one project spans a human workspace and a machine workspace.

**English:** Copy only the language section you intend to use.

**繁中：** 實際交給 Agent 時，只需複製你要使用的語言區段，不需要同時貼英文與中文。

## English prompt

Govern `<PROJECT_ID>` across:

- Human Workspace: `<HUMAN_WORKSPACE>`
- Machine Workspace: `<MACHINE_WORKSPACE>`

Scope is limited to these two explicitly named workspaces and their documented references.

The providers are implementation details. Do not assume a particular vendor, URL shape, or integration.

### Required review

1. Confirm that the project identity is stable and distinct from display names, folder names, and repository labels.
2. Inventory both workspaces read-only within their declared boundaries.
3. Map artifact classes to one explicit source of truth. Examples include code, tests, decisions, briefs, datasets, and release records.
4. Record reference integrity: how one workspace points to the other, which identifiers are stable, and who owns each decision.
5. Classify copies as canonical, reference, export, historical, or unresolved with evidence.
6. Select the smallest lifecycle or organization mode that addresses the request.
7. Ask only questions whose answers could change identity, source of truth, ownership, retention, or a proposed mutation.

### Safety and approval

Do not publish provider identifiers, private links, credentials, session data, or sensitive file contents. Do not treat an export as authoritative merely because it is newer. Do not move or rename an item before checking its cross-workspace references. Do not merge, archive, overwrite, or delete during review. Produce a dry-run change set and wait for explicit approval.

### Required output

Return:

- identity record;
- workspace boundary table;
- source-of-truth map;
- reference-integrity findings;
- lifecycle and organization recommendation;
- unresolved questions and risks;
- approved-candidate change set with post-conditions;
- validation plan for both workspaces.

After approval, execute only the approved subset and validate both workspaces independently. Report if one side cannot be verified. A successful local check cannot substitute for remote verification, and vice versa.

## 繁體中文提示詞

這是選用的進階 Prompt，適用於一個專案跨越人類工作區與機器工作區的情況。

請跨以下兩個工作區治理 `<PROJECT_ID>`：

- Human Workspace：`<HUMAN_WORKSPACE>`
- Machine Workspace：`<MACHINE_WORKSPACE>`

提供者只是實作細節，不要假設特定廠商、URL 形式或整合方式。

### 必要檢視

1. 確認 project identity 穩定，且與 display name、資料夾名稱、Repository label 分離。
2. 在各自宣告邊界內唯讀 inventory 兩個工作區。
3. 為 code、tests、decisions、briefs、datasets、release records 等 artifact class 指定單一 source of truth。
4. 記錄 reference integrity：兩邊如何互指、哪些 identifier 穩定、誰擁有決策。
5. 以證據將副本分類為 canonical、reference、export、historical 或 unresolved。
6. 使用能滿足要求的最小生命週期或整理模式。
7. 只詢問答案會改變 identity、source of truth、所有權、保留政策或變更的問題。

### 安全與核准

不要發布提供者識別碼、私人連結、憑證、工作階段資料或敏感內容。不能只因 export 較新就把它當權威來源。移動或改名前要檢查跨工作區參照；審查時不可合併、封存、覆寫或刪除。先產出 dry-run change set，再等待明確核准。

### 必要輸出

回傳 identity record、工作區邊界表、source-of-truth map、reference-integrity findings、生命週期與整理建議、未解決問題與風險、含 post-condition 的 approved-candidate change set，以及兩邊工作區的驗證計畫。

核准後只執行已核准子集合，並分別驗證兩個工作區。如果其中一邊無法驗證，要明確回報；本機檢查不能代替遠端驗證，反之亦然。
