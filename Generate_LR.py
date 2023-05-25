from PIL import Image
import os


def getSubFolders(folder_path):
    sub_folders = [folder_path + '/' + f.name for f in os.scandir(folder_path) if f.is_dir()]
    return sub_folders


def downSample(image_path, factor):
    with Image.open(image_path) as img:
        width, height = img.size
        downsampled = img.resize((int(width / factor), int(height / factor)))
        return downsampled


def downSample(image_path, factor):
    with Image.open(image_path) as img:
        width, height = img.size
        downsampled = img.resize((int(width / factor), int(height / factor)), resample=Image.BICUBIC)
        return downsampled


root_folder_path='./HR'
output_folder_path = './LR_4x'
factor = 4
for folder in getSubFolders(root_folder_path):
    for file in os.listdir(folder):
        if file.endswith('.png'):  # 只对jpg格式的图片进行处理
            image_path = os.path.join(folder, file)
            downsampled = downSample(image_path, factor)
            output_folder = os.path.join(output_folder_path, os.path.basename(folder))
            os.makedirs(output_folder, exist_ok=True)  # 如果输出文件夹不存在，则创建它
            downsampled.save(os.path.join(output_folder, file))
