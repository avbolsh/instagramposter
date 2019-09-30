import requests
from download_file import download_pic
import urllib3
from os import path


def fetch_spacex_last_launch():
    response = requests.get("https://api.spacexdata.com/v3/launches/latest")
    response.raise_for_status()
    last_launch_info = response.json()
    pic_links = last_launch_info["links"]["flickr_images"]
    for link_number, link in enumerate(pic_links):
        pic_ext = get_ext(link)
        download_pic(link, f"space_x_{link_number}{pic_ext}")
        print(f"Done! Pictures with number {link_number} was downloaded")


def get_ext(file_name):
    return path.splitext(file_name)[1]


def main():
    urllib3.disable_warnings()
    fetch_spacex_last_launch()


if __name__ == '__main__':
    main()
