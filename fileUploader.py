from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os, glob
import csv
from datetime import datetime
import shutil

g_login = GoogleAuth()
g_login.LocalWebserverAuth()
drive = GoogleDrive(g_login)

for file in glob.glob('*.csv'):
    source = str(file)
    dest = str(datetime.date(datetime.now())) + 'wow.csv'
    os.rename(source, dest)
    print('success')

for file in glob.glob('*.csv'):
    print(file)
    with open (file, 'r') as f:
        fn = os.path.basename(f.name)
        file_drive = drive.CreateFile({'title': fn})
        file_drive.SetContentString(f.read())
        file_drive.Upload()
        print("The file: " + fn + ' has been uploaded')

for file in glob.glob('*.csv'):
    orginal = str(file)
    final = 'archive/' + str(file)
    shutil.move(orginal, final)

print('all files have been updated')
