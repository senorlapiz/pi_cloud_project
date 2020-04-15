from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os, glob
import csv
from datetime import datetime
import shutil
import schedule

g_login = GoogleAuth()
g_login.LocalWebserverAuth()
drive = GoogleDrive(g_login)

#Renames files with date and MAC address
def file_rename():
    i = 0
    for file in glob.glob('*.csv'):
        source = str(file)
        dest = str(i) + str(datetime.date(datetime.now())) + 'MAC.csv' #Put MAC address here
        os.rename(source, dest)
        print('success')
        i += 1

#Uploads files to google drive
def file_upload():
    for file in glob.glob('*.csv'):
        print(file)
        with open (file, 'r') as f:
            fn = os.path.basename(f.name)
            file_drive = drive.CreateFile({'title': fn})
            file_drive.SetContentString(f.read())
            file_drive.Upload()
            print("The file: " + fn + ' has been uploaded')

#Sends files to archive
def file_archive():
    for file in glob.glob('*.csv'):
        orginal = str(file)
        final = 'archive/' + str(file)
        shutil.move(orginal, final)

# schedule.every().day.at('05:00').do(file_rename)
# schedule.every().day.at('05:02').do(file_upload)
# schedule.every().day.at('05:04').do(file_archive)

file_rename()
file_upload()
file_archive()

print('all files have been updated')
