#!/usr/bin/env python3
#encoding: UTF-8

from logging import error
import os
import sys
import pytube
from termcolor import colored
from tkinter import Tk, filedialog

# before-hand error handling
if sys.version_info[0] < 3:
    exit("you need to run this script using python 3")
    
if (len(sys.argv) == 1):
    print('just type an instagram or a youtube url and it will detect and download it for you.')
    exit(colored("[?]   usage: python3 {0} URL [path]".format(sys.argv[0]), "yellow"))

def get_download_path():
        if os.name == 'nt':
            import winreg
            sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
            downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
                location = winreg.QueryValueEx(key, downloads_guid)[0]
            return location
        else:
            if (os.path.exists(os.path.expanduser("~") + '/Downloads')):
                return os.path.expanduser("~") + '/Downloads'
            else:
                return os.path.expanduser("~")

if (sys.argv[1].__contains__('youtube')):
    try:
        url = pytube.YouTube(sys.argv[1])
    except Exception as err:
        exit('invalid url.         aka. {0}'.format(err))
    video = url.streams

    print("starting download of: \n{0} from {1}".format(url.title, url.author, url.publish_date))
    print("published {0} with {1} views".format(url.publish_date, url.views))

    if (len(sys.argv) <= 2):
        root = Tk()
        root.withdraw()
        root.attributes('-topmost', True)
        open_file = filedialog.askdirectory()
        if (open_file == '' or open_file == 'undefined' or len(open_file) == 0):
            open_file = get_download_path()
        
        print("size: {0} MB.".format(str(video.get_highest_resolution().filesize / 1e+6)))
        video.get_highest_resolution().download(open_file, "download.mp4")

    else:
        video.get_highest_resolution().download(sys.argv[2], "download.mp4")
        
if (sys.argv[1].__contains__('instagram')):
    print('not working :(')
    
if (sys.argv[1].__contains__('twitter')):
    print('not working :(')