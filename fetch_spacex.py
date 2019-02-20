import os
import requests


def download_image(image_name, image_url):
    '''	This function downloads images as binary-data files
    to "images" folder.
    '''
    filename = os.path.join(images_dir_path, image_name)
    response = requests.get(image_url)
    with open(filename, "bw") as file:
        file.write(response.content)


def fetch_spacex_last_launch(url_api):
    '''	This function fetches images about last launch 
    from "spacexdata" API. 
    '''
    response = requests.get(url_api)
    data = response.json()["links"]["flickr_images"]
    for  number, item in enumerate(data):
        image_name = "spacex{}.jpg".format(number+1)
        image_url = item
        download_image(image_name, image_url)


if __name__ == '__main__':
    
    mask_api = "https://api.spacexdata.com/v3/launches/latest"

    current_dir_path = os.getcwd()
    images_dir_path = os.path.join(current_dir_path, "images")
    os.makedirs(images_dir_path, exist_ok=True)

    fetch_spacex_last_launch(mask_api)