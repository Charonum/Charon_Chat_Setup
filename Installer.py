import sys
import subprocess
import os
import getpass
import shutil
import zipfile

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

url = "https://github.com/Charonum/JS_Startup/archive/refs/heads/main.zip"
wget.download(url, rf"C:\Users\{getpass.getuser()}\Charonum\JS")

with zipfile.ZipFile(rf"C:\Users\{getpass.getuser()}\Charonum\JS\JS_Startup-main.zip", 'r') as zipObj:
    zipObj.extractall()

for file in os.listdir(rf"C:\Users\{getpass.getuser()}\Charonum\JS\JS_Startup-main"):
    shutil.move(rf"C:\Users\{getpass.getuser()}\Charonum\JS\JS_Startup-main\{file}", rf"C:\Users\{getpass.getuser()}\Charonum\JS")

os.remove(rf"C:\Users\{getpass.getuser()}\Charonum\JS\JS_Startup-main.zip")
os.remove(rf"C:\Users\{getpass.getuser()}\Charonum\JS\JS_Startup-main")

print("Installing PyAudio...")
user = getpass.getuser()
os.chdir(fr"C:\Users\{user}\Downloads\JS_Setup\Setup_Files")
os.system("install.py")
