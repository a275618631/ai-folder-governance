# 2. 運作方式

## 六個階段

### 1. 理解

在明確範圍內唯讀檢查。記錄路徑、檔案類型、時間、大小、可見標題、所有權訊號、連結、重複指標與可能的路徑相依性。不要為了改善分類而打開可能包含秘密的內容。

### 2. 分類

依用途與權威性分類，不只依主題。可使用 working material、canonical source、reference、export、historical record、archive candidate、duplicate candidate 與 unresolved 等標籤。

每個標籤都要記錄證據與信心度；推測不是事實。

### 3. 規劃

選擇能滿足要求的最小整理模式，產出 dry-run change set，包含：

- 目前路徑與建議路徑；
- 動作類型；
- 理由與證據；
- 信心度；
- 相依性影響；
- 需要使用者決定的項目；
- 後置條件。

### 4. 必要時詢問

只詢問會實質影響結果的問題。例如是否封存舊專案資料可能很重要；兩個等價資料夾名稱的偏好，除非真的要改名，否則不重要。

### 5. 執行

移動、改名、封存或刪除前等待明確核准。逐項或以可回復的小批次執行，維持 change ledger；若預期的前置條件不成立就停止。

### 6. 驗證

重新掃描目標。確認核准的目的地存在、來源項目已按計畫處理、連結與路徑相依性仍有效或已刻意更新、範圍外沒有變更，且報告符合實際結果。

## 整理模式

| 模式 | 邊界 | 適用情境 |
| --- | --- | --- |
| `SHALLOW_ORGANIZE` | 只處理直接子項 | 有界線的單資料夾整理。 |
| `INCREMENTAL_MAINTENANCE` | 新增或近期變動項目 | 低干擾的日常維護。 |
| `RECURSIVE_DEEP_ORGANIZE` | 完整遞迴樹 | 刻意進行的專案或封存審查。 |
| `PROJECT_LIFECYCLE_REVIEW` | 專案 identity 與生命週期 | 判斷 active、related、historical、archive、duplicate 或 delete-candidate。 |

不能把 shallow 請求默默擴大成 recursive；若真的需要更深視角，先說明理由並請求擴大範圍。

## 穩定結果狀態

- `SCAN_PASS`：在範圍內完成檢視。
- `PLAN_READY`：dry-run change set 已可審查。
- `WAITING_FOR_APPROVAL`：已提出變更但尚未授權。
- `ORGANIZATION_PASS`：已執行並驗證核准變更。
- `PARTIAL_WITH_UNRESOLVED_ITEMS`：安全工作已完成，歧義或受阻項目維持不動。
- `NO_CHANGE_NEEDED_PROOF`：沒有合理變更，且提供證據。

## Idempotency 檢查

執行後用相同檢查邏輯重跑。穩定結果不應產生新的移動或改名提案，除非出現新檔案、新證據或偏好改變。如果每次都提出另一輪整理，代表分類方式或驗收標準還不夠穩定。
