import sys
import subprocess
import os
import getpass
import shutil

JS_logo = fr'C:\Users\{getpass.getuser()}\Downloads\JS_Setup\icons\JS logo.ico'
phone_logo = fr'C:\Users\{getpass.getuser()}\Downloads\JS_Setup\icons\phone.ico'
target = rf"C:\Users\{getpass.getuser()}\Charonum\JS"

try:
    os.mkdir(rf"C:\Users\{getpass.getuser()}\Charonum\JS")
    shutil.move(JS_logo, target)
    shutil.move(phone_logo, target)
except:
    JS = fr'C:\Users\{getpass.getuser()}\Charonum\JS'
    for f in os.listdir(JS):
        os.remove(os.path.join(JS, f))

    shutil.move(JS_logo, target)
    shutil.move(phone_logo, target)

subprocess.call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
subprocess.call([sys.executable, "-m", "pip", "install", "requests"])
subprocess.call([sys.executable, "-m", "pip", "install", "wget"])

import requests
import wget

response = requests.get('https://raw.githubusercontent.com/Charonum/JSCode/main/Files.txt')
responsecontent = response.text

for file in responsecontent.split("\n"):
    file = file.replace("b'", "")
    file = file.replace("'", "")
    file = file.replace(r"\n", "")
    if file == "":
        pass
    else:
        url = f'https://raw.githubusercontent.com/Charonum/JSCode/main/code/windows/{file}'
        print(f"Fetching {url}")
        wget.download(url, rf"C:\Users\{getpass.getuser()}\Charonum\JS")

import getpass
print("Installing PyAudio...")
user = getpass.getuser()
os.chdir(fr"C:\Users\{user}\Downloads\JS_Setup\Setup_Files")
os.system("install.py")
