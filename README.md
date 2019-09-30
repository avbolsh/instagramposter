# Space Instagram

## Description

There are a few scripts for downloading images from hubble.com and another sites and posting its in Instagram

## How to install

Python3 should be already installed. Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:

	pip install -r requirements.txt


## How it works

Scripts:

__downloadfile.py__ - allow to download any file, you have to add argumets: URL and file name

	python download_file -url <your_url> -file <your file name>

__fetch\_spacex.py__ - allow download from spacexdata.com last lauch\`s images

	python fetch_spacex.py

__fetch\_hubble\_list.py__ - allow to get images IDs from hubble colletion in stdout, you have to add argumets: name of collection

	python fetchhubblelist.py -name wallpaper

__fetch\_hybble.py__ - allow dowload images from hubble.com. You have to add arguments: id(s) images

	python fetch_hubble.py 1 2 3 10 

... or you may use script fetch\_hubble\_list.py for download all images from hubble\`s colliction
	
	python fetch_hubble_list - name wallpaper | python fetch_hubble.py

__crop\_it.py__ - allow crop images, you have to add arguments: directory with images, script crops all images from diretory

	python crop_it.py ~/devproject_3/images

__instaposter.py__ allow post all images from dirtctory

	pythin instaposter ~/devproject_3/images/cropped

## Project Goals

The code is written for educational purposes on online-course for web-developers dvmn.org.

