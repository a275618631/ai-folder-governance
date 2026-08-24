# 8. Runtime 能力

框架會把 Agent 的推理能力與 Host Runtime 實際可做的事情分開。能力名稱不是平台支援聲明。

## 能力矩陣

| Host 能力 | Scan | Plan | Execute | Validate |
| --- | --- | --- | --- | --- |
| 只有聊天 | 使用者提供 inventory | 可以 | 不可以 | 比對下一次提供的 inventory，或回報限制 |
| 使用者提供 inventory | 檢視提供的證據 | 可以 | 不可以 | 只能依提供的證據驗證 |
| 唯讀檔案系統 | 讀取允許的 metadata 與內容 | 可以 | 不可以 | 唯讀重掃，回報無法證明的部分 |
| 可讀寫檔案系統 | 在範圍內讀取 | 可以 | 已核准的移動、改名或封存 | 重掃並驗證 post-condition |
| 遠端工作區 connector | 使用 connector 支援的讀取範圍 | 可以 | 只有具備寫入能力且獲得核准才可以 | 透過 connector 回讀 |
| Git 加檔案系統 | 檢查檔案、連結與 Git 狀態 | 可以 | 已核准檔案變更；commit 與 push 仍是分開動作 | 檔案檢查加 Git status、diff、test |

這張表描述的是決策邊界，不是自動授權。沒有寫入能力的 Runtime 必須回傳 `PLAN_READY`，不能回傳 `ORGANIZATION_PASS`。

## Tested 與 designed

請精確使用以下標籤：

- **Tested：** 特定 Runtime、版本或上下文、fixture、日期與限制已記錄在 [runtime verification](../../tests/runtime-verification.md)。
- **Designed for：** 流程是依該能力設計，但本版沒有宣稱實際執行過特定產品或提供者。
- **Format compatible：** Skill 套件符合 Agent Skills 檔案形狀；格式相容不代表行為支援已證實。

本版記錄目前 Codex Runtime 的 fixture-backed 驗證，但不宣稱所有 Agent、雲端提供者、檔案系統或 connector 都支援相同操作。

## 能力探索

規劃變更前確認：

1. 是否能在範圍內讀取 target；
2. 是否能檢查路徑相依性；
3. 是否能寫入、移動、改名、封存或刪除；
4. 是否能獨立回讀結果；
5. Git 動作是否可用，且是否取得分開核准。

只要缺少必要能力，就停在最高誠實狀態並回報限制。不能因為能對檔案聊天，就推論具備寫入或驗證能力。

## Runtime-neutral 回報

例如：

```text
runtime: read-only filesystem
scan: pass
plan: ready
execute: unavailable
validate: read-only re-scan only
result: PLAN_READY
```

避免使用「所有 Agent 都支援」這類未驗證聲明。
