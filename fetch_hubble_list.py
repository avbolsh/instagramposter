import requests
import argparse


def set_script_arguments():
    parser = argparse.ArgumentParser(description="Get list of images from hubble.com")
    parser.add_argument("-name", help="Name of hubble`s collection images",
                        type=str)
    return parser.parse_args()


def get_list_of_img(collection_name):
    url = f"http://hubblesite.org/api/v3/images/{collection_name}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def main():
    args = set_script_arguments()
    img_list = get_list_of_img(args.name)
    for img in img_list:
        print(img["id"], end=" ")
    print()


if __name__ == "__main__":
    main()