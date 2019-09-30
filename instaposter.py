from instabot import Bot
from dotenv import load_dotenv
import argparse
import os


def post_it(path_to_dir, login, password):
    img_names = [name for name in os.listdir(path_to_dir)
                 if os.path.isfile(os.path.join(path_to_dir, name))]
    bot = Bot()
    bot.login(username=login, password=password)
    for img in img_names:
        bot.upload_photo(os.path.join(path_to_dir, img))


def set_script_arguments():
    parser = argparse.ArgumentParser(description="Post images from directory to Instagram")
    parser.add_argument('path_to_dir', help='Path to directory with images')
    return parser.parse_args()


def main():
    load_dotenv()
    USERNAME = os.getenv("USERNAME")
    PASSWORD = os.getenv("PASSWORD")
    arg = set_script_arguments()
    post_it(arg.path_to_dir, USERNAME, PASSWORD)


if __name__ == '__main__':
    main()
