import os
import requests

	
def download_image(image_name, image_url):
    ''' This function downloads images as binary-data files
    to "images" folder.
    '''
    filename = os.path.join(images_dir_path, image_name)
    response = requests.get(image_url)
    with open(filename, "bw") as file:
        file.write(response.content)


def detect_image_extention(url):
    '''	This function catches image's extention.
    '''
    url_list = url.split('.')
    return url_list[-1]


def fetch_hubble_image(url_image_api, image_id):
    ''' This function fetches image from "hubblesite" API. 
    '''
    response = requests.get(url_image_api + str(image_id))
    data = response.json()["image_files"][-1]
    image_extention = detect_image_extention(data['file_url']) 
    image_name = "{}.{}".format(image_id, image_extention)
    image_url = data['file_url']
    return download_image(image_name, image_url) 


def fletch_hubble_image_collection(url_collection_api, collection_name, url_image_api):
    ''' This function fetches a collection of images from "hubblesite" API.
    '''
    response = requests.get(url_collection_api, collection_name)
    data_collection = response.json()
    for item in data_collection:
        fetch_hubble_image(url_image_api, item['id'])


if __name__ == '__main__':

    url_collection_api = 'http://hubblesite.org/api/v3/images/'
    collection_name = 'spacecraft'
    url_image_api = 'http://hubblesite.org/api/v3/image/'

    current_dir_path = os.getcwd()
    images_dir_path = os.path.join(current_dir_path, "images")
    os.makedirs(images_dir_path, exist_ok=True)

    fletch_hubble_image_collection(url_collection_api, collection_name, url_image_api)