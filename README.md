# FastAPI 與 [TaskFlowDAG](https://github.com/Mahopanda/TaskFlowDAG) 資料處理整合應用介紹

這個範例使用了 FastAPI 來建構 RESTful API 以及 [TaskFlowDAG](https://github.com/Mahopanda/TaskFlowDAG) 來進行數據處理。

## 核心功能
1. 資料處理: 使用 Dag 來定義和執行一個數據處理流程，這包括了：
    * Categorize: 根據 attribute 的值分類數據。
    * Normalize: 將 value 正規化到 0 到 1 的範圍內，並基於該值決定後續的流程。
    * Filter Text: 如果正規化後的值大於 0.5，這個節點將從 text 中去除非字母字符。
    * No Filter: 如果正規化後的值小於或等於 0.5，數據將直接被傳遞下去而不作更改。
2. API 端點: 提供了一個 POST 端點 /process/，這個端點接受輸入數據，然後將其通過上面定義的 Dag 進行處理，最後返回處理後的資料。
