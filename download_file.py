import requests
import os
import argparse


def download_pic(url, file_name):
    path_to_images = os.path.join(os.getcwd(), "images")

    if not os.path.exists(path_to_images):
        os.makedirs(path_to_images)

    response = requests.get(url, verify=False)
    response.raise_for_status()

    abs_file_path = os.path.join(path_to_images, file_name)

    with open(abs_file_path, 'wb') as file:
        file.write(response.content)


def set_script_arguments():
    parser = argparse.ArgumentParser(description="Download file from URL")
    parser.add_argument("-url", help="URL for downloading",
                        type=str)
    parser.add_argument("-file", help="File name", type=str)

    return parser.parse_args()


def main():
    arguments = set_script_arguments()
    url = arguments.url
    file_name = arguments.file
    try:
        download_pic(url, file_name)
    except requests.HTTPError:
        print("Wrong URL!")
    except requests.exceptions.MissingSchema:
        print("Incorrect URL!")


if __name__ == '__main__':
    main()