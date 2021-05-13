import sys
import subprocess
import os
import getpass
import zipfile
import shutil

try:
    os.mkdir(rf"C:\Users\{getpass.getuser()}\Charonum\JS")
except:


subprocess.call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
subprocess.call([sys.executable, "-m", "pip", "install", "requests"])
subprocess.call([sys.executable, "-m", "pip", "install", "wget"])

import wget

url = "https://github.com/Charonum/JS_Startup/archive/refs/heads/main.zip"
wget.download(url, rf"C:\Users\{getpass.getuser()}\Charonum\JS")

with zipfile.ZipFile(rf"C:\Users\{getpass.getuser()}\Charonum\JS\JS_Startup-main.zip", 'r') as zipObj:
    zipObj.extractall(rf"C:\Users\{getpass.getuser()}\Charonum\JS")

for file in os.listdir(rf"C:\Users\{getpass.getuser()}\Charonum\JS\JS_Startup-main"):
    shutil.move(rf"C:\Users\{getpass.getuser()}\Charonum\JS\JS_Startup-main\{file}", rf"C:\Users\{getpass.getuser()}\Charonum\JS")

os.remove(rf"C:\Users\{getpass.getuser()}\Charonum\JS\JS_Startup-main.zip")
os.remove(rf"C:\Users\{getpass.getuser()}\Charonum\JS\JS_Startup-main")
os.remove(rf"C:\Users\{getpass.getuser()}\Charonum\JS\README.md")

print("Installing PyAudio...")
user = getpass.getuser()
os.chdir(fr"C:\Users\{user}\Downloads\Charon_Chat_Setup_main\Setup_Files")
os.system("install.py")
