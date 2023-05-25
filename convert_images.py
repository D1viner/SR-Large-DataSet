import os
from PIL import Image


def convert_images(folder_path, output_format):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            if file.lower().endswith(('.jpg', '.jpeg', '.png')):
                try:
                    image = Image.open(file_path)
                    output_path = os.path.splitext(file_path)[0] + '.' + output_format
                    image.save(output_path, format=output_format)
                    print(f"Converted {file_path} to {output_path}")

                    # 删除原始图片
                    if not file.lower().endswith('.png'):
                        os.remove(file_path)
                        print(f"Deleted {file_path}")

                except Exception as e:
                    print(f"Error converting {file_path}: {str(e)}")


# 调用示例
folder_path = './HR'  # 替换为实际的文件夹路径
output_format = 'png'  # 替换为你希望的输出格式

convert_images(folder_path, output_format)
