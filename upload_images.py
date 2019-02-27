from instabot import Bot
import os
from dotenv import load_dotenv

def upload_images_to_instagram(your_login, your_password, images_dir_path):
    '''	This function uploads images to Instartam.
    '''
    bot = Bot()
    bot.login(username=your_login, password=your_password)
    image_list = os.listdir(images_dir_path)
    for image_item in image_list:
        bot.upload_photo(os.path.join(images_dir_path, image_item))

if __name__ == '__main__':
    load_dotenv()
    images_dir_path = os.path.join(os.getcwd(), "images")
    upload_images_to_instagram(os.getenv('your_login'), os.getenv('your_password'), images_dir_path)
