### A short description of the project
This project is dedicated to obtaining photographs from the Network related to space and the space industry. The *fetch_spacex.py* file allows you to get photos from the last launch of the SpaceX rocket, and the *fetch_hubble.py* file allows you to take pictures from space taken with the Hubble telescope. Downloaded photos will be stored in the *"images"* folder. Another file - *upload_images.py* - makes it possible to upload these photos to the network "Instagram".
### Environmental Requirement
It is recommended to deploy the application in a virtual environment (for example, this way: (https://python-scripts.com/virtualenv)), and then install the required modules from the requirements.txt (by this way).
```python
pip install pip
pip freeze
freeze install -r requirements.txt
```
### How to install and to use
All scripts work autonomously and use the corresponding *APIs*. Instagram account data should be written to the *.env* file. For this task you may create *.env* file and write a code in the file: 
```python
your_login=<here you should write your login in Instagram>
your_password=<here you should write your password in Instagram>
```
After that you should to start these scripts in terminal (one by one - wait then each of its finished itself work).
Attantion: it will create a folder *Images* if this folder did not exist yet.

At firsteval, for example:
```
python fetch_spacex.py
```
The second hand:
```
python fetch_hubble.py
```
And at the end, then folder *Images* will have contain a lot of photos, you can upload this images in Instagram:
```
python upload_images.py
```
Good luck!
