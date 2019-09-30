import os
from PIL import Image
import argparse


def crop_img(path_to_img):
    image = Image.open(path_to_img)

    img_width = image.width
    img_height = image.height
    min_side = min(img_height, img_width)
    coordinates = (0, 0, min_side, min_side)

    cropped = image.crop(coordinates)
    dir_for_cropped = os.path.join(os.path.dirname(path_to_img), "cropped")

    if not os.path.exists(dir_for_cropped):
        os.makedirs(dir_for_cropped)

    base_file_name = os.path.basename(path_to_img)
    name_cropped_file = f"cropped_{base_file_name}"

    cropped.save(os.path.join(dir_for_cropped, name_cropped_file)


def crop_all_img(path_to_dir):
    img_names = [name for name in os.listdir(path_to_dir)
                 if os.path.isfile(os.path.join(path_to_dir, name))]
    for img in img_names:
        crop_img(os.path.join(path_to_dir, img))
        print(f"Done! {img} was cropped! ")


def set_script_arguments():
    parser = argparse.ArgumentParser(description="Crop images")
    parser.add_argument("path", help="Path to directory with images for cropping")
    return parser.parse_args()


def main():
    arg = set_script_arguments()
    crop_all_img(arg.path)


if __name__ == "__main__":
    main()
