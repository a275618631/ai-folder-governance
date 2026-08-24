# 4. 偏好設定

偏好會影響整理選擇，但不能關閉安全不變量。

## 漸進式探索

1. 先唯讀檢查。
2. 能推論就不要問。
3. 只問答案可能實質改變計畫的最小問題集合。
4. 提供只套用本次工作階段，或儲存到目標資料夾的選擇。

不要每次都詢問所有偏好。

## 偏好維度

| 維度 | 選項 | 何時詢問 |
| --- | --- | --- |
| 重整程度 | `preserve-first`、`moderate`、`redesign` | 建議目的地會改變現有結構。 |
| 深度 | `current`、`one-level`、`recursive` | 要求沒有明確邊界。 |
| 封存 | `keep-in-place`、`archive`、`ask-per-item` | 舊資料或歷史資料需要生命週期判斷。 |
| 刪除 | 預設 `confirm` | 任何刪除或覆寫被提出時。 |
| 命名語言 | `keep` 或指定語言 | 確實需要改名，且語言會影響搜尋。 |
| 日期前綴 | `never`、`when-useful`、`always` | 確實需要改名，日期可改善尋找。 |
| 命名風格 | `concise`、`descriptive` | 確實需要改名，兩種風格都合理。 |

## 設定範例

檔案是選用的，僅套用到指定資料夾或工作階段：

```yaml
version: 1

organization:
  depth: recursive
  structure_policy: preserve-first

archive:
  strategy: semantic

delete:
  mode: confirm
  exact_duplicates: allow

naming:
  language: keep
  date_prefix: when-useful
  style: descriptive

safety:
  secret_black_box: true
  check_path_dependencies: true
```

第一次檢視後，Agent 可以詢問要選擇「Save preferences for this folder」或「Session only」。

## 設定規則

- 未知 key 要回報，不可默默解讀。
- 無效值要停止受影響的規劃。
- 安全 key 是斷言，不是開關；設成 false 不能停用對應不變量。
- 偏好檔不是權威性、所有權或刪除權限的證明。
- 後續執行應說明哪些儲存偏好影響了計畫。
