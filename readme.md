### A short description of the project
This project is dedicated to obtaining photographs from the Network related to space and the space industry. The *fetch_spacex.py* file allows you to get photos from the last launch of the SpaceX rocket, and the *fetch_hubble.py* file allows you to take pictures from space taken with the Hubble telescope. Downloaded photos will be stored in the *"images"* folder. Another file - *upload_images.py* - makes it possible to upload these photos to the network "Instagram".
### Environmental Requirement
It is recommended to deploy the application in a virtual environment (for example, this way: (https://python-scripts.com/virtualenv)), and then install the required modules from the requirements.txt (by this way).
```python3
pip install pip
pip freeze
freeze install -r requirements.txt
```
### How to install
All scripts work autonomously and use the corresponding *APIs*. Instagram account data should be written to the *.env* file (by assigning the login and password values ​​of a specific user to the environment variables *your_login* and *your_password*) and place it in the same directory as the *upload_images.py* file.