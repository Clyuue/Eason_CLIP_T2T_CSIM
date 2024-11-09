import re
import os
import argparse

def process_files(args):
    # 如果目標輸出目錄不存在，則創建
    if not os.path.exists(args.output_path):
        os.makedirs(args.output_path)

    # 遍歷指定資料夾中的所有文件
    for filename in os.listdir(args.file_path):
        # 確保只處理 .md 文件
        if filename.endswith(".md"):
            full_file_path = os.path.join(args.file_path, filename)

            # 開啟文件並逐行讀取內容
            with open(full_file_path, 'r', encoding='utf-8') as file:
                content = file.readlines()
                image_name = os.path.basename(filename).split('.')[0]

                # 用於存儲結果的列表
                results = []

                # 逐行處理文件內容
                for line in content:
                    line = line.strip()  # 去除首尾空格
                    print(f"正在處理行: '{line}'")  # 調試輸出每一行的內容

                    # 修改正則表達式來匹配行中的加粗和數字序號
                    match = re.match(r'^\d+\.\s*\*\*(\w+)\*\*:\s*(.*)$', line)
                    if match:
                        key = match.group(1).strip()  # 提取key
                        value = match.group(2).strip()  # 提取value
                        
                        # 如果 value 是 "None"，則跳過此屬性
                        if value.lower() == "none":
                            continue
                        
                        # 將 value 拆分為描述部分
                        value_parts = [v.strip() for v in value.split(',')]
                        joined_value = ' '.join(value_parts)  # 將拆分的值重新合併
                        
                        # 將 Gender, Race, Age 的值放在前面
                        if key == "Gender":
                            results.insert(0, joined_value)  # 放在列表的最前面
                        elif key == "Race":
                            results.insert(1, joined_value)  # 放在第二個位置
                        elif key == "Age":
                            results.insert(2, joined_value)  # 放在第三個位置
                        else:
                            # 其他特徵的值放在後面
                            results.append(f"{joined_value} {key}")

                    else:
                        print(f"無法匹配: '{line}'")

                # 確保有提取到的結果
                if results:
                    # 將結果轉換為字符串格式
                    result_str = ', '.join(results)  # 使用逗號連接
                    print(f"處理文件: {filename} -> {result_str}")

                    # 寫入數據
                    parts = image_name.split("_")
                    image_id = "_".join(parts[1:])
                    txt_file_path = os.path.join(args.output_path, f"{image_id}.txt")
                    with open(txt_file_path, 'w', encoding='utf-8') as output_file:
                        output_file.write(result_str + '\n')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="從指定的文件夾處理 .md 文件並輸出結果")
    parser.add_argument("file_path", type=str, help="輸入 .md 文件所在的資料夾路徑")
    parser.add_argument("output_path", type=str, help="輸出處理結果的資料夾路徑")
    args = parser.parse_args()
    process_files(args)
