# Eason文本相似度比較器

1. 此專案用於處理指定資料夾中的 `.md` 文件，對每行內容進行正則匹配與特徵提取，並生成包含處理結果的 `.txt` 文件。
2. 基於 OpenAI 的 CLIP 模型對文本特徵進行相似度計算。

## 環境依賴

### Python 版本

請使用 Python 3.10 或更高版本。

### 安裝依賴

在專案目錄下，執行以下命令以安裝所需的依賴：
```bash
cd Eason_CLIP_T2T_CSIM
```
```bash
conda create -n eason_t2t python=3.10
```
```bash
conda activate eason_t2t
```

```bash
pip install -r requirements.txt
```

### 使用說明
命令行參數
運行該腳本時，需要通過命令行指定輸入資料夾和輸出資料夾路徑。具體命令格式如下：

```bash
python beforeSD_yuri.py <input_folder> <output_folder>
```
<input_folder>：包含 .md 文件的資料夾路徑。
<output_folder>：處理後 .txt 文件的輸出路徑。

命令行參數
運行該腳本時，需要通過命令行指定輸入資料夾和比較資料夾路徑。具體命令格式如下：

```bash
python clip_csim.py <input_folder> <compare_folder>
```
<input_folder> :輸入資料夾
<compare_folder>:比較資料夾

### 範例
假設您的輸入資料夾路徑為 ./generate，輸出資料夾路徑為 ./generate_txt，則命令如下：

```bash
python beforeSD_yuri.py ./generate2 ./generate_txt
```
假設您的輸入資料夾路徑為 ./original，輸出資料夾路徑為 ./original_txt，則命令如下：

```bash
python beforeSD_yuri.py ./original ./original_txt
```
輸出結果
執行後，生成的 .txt 文件將保存在指定的輸出資料夾中，文件名格式為原 .md 文件名去除特定前綴後的識別碼。
每個 .txt 文件包含處理後的屬性資訊，並使用逗號分隔。

假設您的輸入資料夾路徑為 ./generate_txt，比較資料夾路徑為 ./original_txt，則命令如下：
```bash
python clip_csim.py ./generate_txt ./original_txt
```
執行後，顯示兩個資料夾對應txt的相似度分數，以及每組pair的相似度分數。

### 注意事項
輸入的 .md 文件需符合特定格式，每行必須包含加粗的屬性關鍵字和對應的描述資訊，否則無法正確解析。
若輸出目錄不存在，程式將自動創建。
