import os
import pandas as pd

# 设定路径
train_dir = "data/train_images"
train_csv = "data/train_cultivar_mapping.csv"  # 确保文件存在


# 读取训练数据 CSV 文件
train_df = pd.read_csv(train_csv)

# 查看数据基本信息
print(train_df.info())  # 显示数据列信息
print(train_df.head())  # 显示前几行数据

# 获取 train_images 目录下所有的 PNG 图片
train_images = [img for img in os.listdir(train_dir) if img.endswith(".png")]

print(f"训练集总图像数: {len(train_images)}")
