import os
import torch
import torch.nn.functional as F
from transformers import CLIPModel, CLIPTokenizer
import argparse

def main(args):
    # 加载 CLIP 模型和分词器
    model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
    tokenizer = CLIPTokenizer.from_pretrained("openai/clip-vit-base-patch32")

    # 获取文件列表
    files1 = sorted(os.listdir(args.folder1))
    files2 = sorted(os.listdir(args.folder2))

    # 创建一个字典来存储文件名的共同部分
    file_pairs = {}

    # 遍历第一个文件夹中的文件
    for file1 in files1:
        common_part = file1.split('_')[-1]  # 假设共同部分在下划线之前
        file_pairs[common_part] = [file1, None]

    # 遍历第二个文件夹中的文件
    for file2 in files2:
        common_part = file2.split('_')[-1]  # 假设共同部分在下划线之前
        if common_part in file_pairs:
            file_pairs[common_part][1] = file2

    similarities = []

    # 遍历每对文件
    for common_part, (file1, file2) in file_pairs.items():
        if file2 is None:
            continue  # 跳过没有匹配的文件对

        # 读取文件内容
        with open(os.path.join(args.folder1, file1), 'r', encoding='utf-8') as f:
            text1 = f.read()
        with open(os.path.join(args.folder2, file2), 'r', encoding='utf-8') as f:
            text2 = f.read()

        # 编码文本
        inputs1 = tokenizer(text1, return_tensors="pt")
        inputs2 = tokenizer(text2, return_tensors="pt")

        # 获取文本特征
        with torch.no_grad():
            outputs1 = model.get_text_features(**inputs1)
            outputs2 = model.get_text_features(**inputs2)

        # 计算余弦相似度
        similarity = F.cosine_similarity(outputs1, outputs2)
        print(f"比较文件: {file1} 和 {file2}的相似度: {similarity.item()}")
        similarities.append(similarity.item())

    # 计算平均相似度
    average_similarity = sum(similarities) / len(similarities) if similarities else 0
    print(f"平均相似度: {average_similarity}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="计算两个文件夹中对应文本文件的相似度")
    parser.add_argument("folder1", type=str, help="第一个文件夹路径")
    parser.add_argument("folder2", type=str, help="第二个文件夹路径")
    args = parser.parse_args()
    main(args)
