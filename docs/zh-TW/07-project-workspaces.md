# 7. 專案工作區

這個選用模組治理一個跨越兩個工作區的專案：

```text
One Project
├── Human Workspace   文件、決策、brief、核准
└── Machine Workspace 程式碼、測試、自動化、發布產物
```

兩個工作區可以使用不同或相同的提供者。文件提供者與 Git 提供者只是例子，不是硬性要求。

## Stable identity

使用不會隨顯示名稱、資料夾名稱或 Repository label 改變的 `project_id`。把人類可讀的 `display_name` 與 identifier 分開。

## Source-of-truth separation

為每種 artifact class 宣告一個 source of truth。例如程式碼與測試可以由 machine workspace 掌握權威性，而決策紀錄由 human workspace 掌握。副本、export 或連結不能因為較新或較容易找到就成為 canonical。

## Reference integrity

記錄兩個工作區如何互相參照：stable project identity、文件化的相對參照、release 或 decision identifier，以及所有權。移動或改名前檢查這些參照，無法檢查時維持不動。

## Lifecycle review

專案審查可以分類為：

- `active`：由明確 owner 維護的目前工作；
- `related`：與其他專案相關，但尚未準備合併；
- `historical`：保留作為脈絡、不再活躍；
- `archive`：依刻意的保留政策留存；
- `duplicate`：identity 與目的相同，且有更強 canonical candidate；
- `delete-candidate`：只有明確確認後才可能刪除。

這些是帶證據的決策，不是自動產生的資料夾名稱。

## Identity 範本

可以從 [identity template](../../skills/ai-folder-governance/assets/project-identity.example.yaml) 開始。在私人工作區替換成使用者自己的值；不要發布真實的提供者識別碼。
