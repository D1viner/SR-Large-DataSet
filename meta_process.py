import os
import random
from PIL import Image, ImageOps

input_folder = "./meta_data"
output_folder = "./processed_data"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)


def crop_image(image, size):
    width, height = image.size
    left = (width - size) // 2
    top = (height - size) // 2
    right = left + size
    bottom = top + size
    cropped_image = image.crop((left, top, right, bottom))
    return cropped_image


def augment_image(image):
    if random.random() < 0.5:
        image = ImageOps.flip(image)

    angle = random.randint(-45, 45)
    image = image.rotate(angle)

    return image


def process_image(input_path, output_path):
    image = Image.open(input_path)
    size = min(image.width, image.height)
    if image.width * image.height > 89478485:
        image = image.resize((image.width // 2, image.height // 2), Image.BICUBIC)

    cropped_image = crop_image(image, size)

    if random.random() < 0.05:
        augmented_image = augment_image(cropped_image)
    else:
        augmented_image = cropped_image

    augmented_image.save(output_path, optimize=True, quality=95, subsampling=0)
    print(output_path)
    image.close()


processed_folders = os.listdir(input_folder)

cloud_data_index = processed_folders.index("plant_dataset")+1

for subfolder_name in processed_folders[cloud_data_index:]:
    input_subfolder = os.path.join(input_folder, subfolder_name)
    output_subfolder = os.path.join(output_folder, subfolder_name)
    if not os.path.exists(output_subfolder):
        os.makedirs(output_subfolder)

    for root, dirs, files in os.walk(input_subfolder):

        for file_name in files:
            if file_name.lower().endswith((".jpg", ".png", ".jpeg")):
                input_path = os.path.join(root, file_name)
                output_path = os.path.join(output_subfolder, file_name)
                process_image(input_path, output_path)
