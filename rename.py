import os

folder_path = './LR_3x/bear_dataset'
prefix = 'bear_'

file_list = os.listdir(folder_path)
file_list.sort()

for i, file_name in enumerate(file_list):
    if file_name.endswith('.png') or file_name.endswith('.jpg'):
        new_name = prefix + str(i + 1) + file_name[-4:]
        file_path = os.path.join(folder_path, file_name)
        new_path = os.path.join(folder_path, new_name)
        os.rename(file_path, new_path)
    elif file_name.endswith('.jpeg'):
        new_name = prefix + str(i + 1) + file_name[-5:]
        file_path = os.path.join(folder_path, file_name)
        new_path = os.path.join(folder_path, new_name)
        os.rename(file_path, new_path)
