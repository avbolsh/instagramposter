import requests
import argparse
from download_file import download_pic
import urllib3
import sys
from os import path


def get_hubble_img(list_img_id):
    for img_id in list_img_id:
        url = f"http://hubblesite.org/api/v3/image/{img_id}"
        response = requests.get(url)
        response.raise_for_status()
        full_img_info = response.json()["image_files"][-1]
        img_url = f"https:{full_img_info['file_url']}"
        img_extension = get_ext(img_url)
        file_name = f"{img_id}{img_extension}"
        download_pic(img_url, file_name)
        print(f"Done! {file_name} was downloaded")


def set_script_arguments():
    parser = argparse.ArgumentParser(description="Download image from hubble.com")
    parser.add_argument('list_img_id', type=int, nargs='*',
                        help='id(s) of image(s)')
    parser.add_argument('outfile', nargs='?', type=argparse.FileType('r'), default=sys.stdin)
    return parser.parse_args()


def get_ext(file_name):
    return path.splitext(file_name)[1]


def main():
    urllib3.disable_warnings()
    arg = set_script_arguments()

    if not arg.list_img_id:
        list_img_id = [int(id) for id in (arg.outfile.readline().strip().split(" "))]
    else:
        list_img_id = arg.list_img_id

    try:
        get_hubble_img(list_img_id)
    except requests.HTTPError:
        print("Something goes wrong...")


if __name__ == "__main__":
    main()
