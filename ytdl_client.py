#!/usr/bin/python
import os
import youtube_dl
import subprocess
from mutagen.mp4 import MP4

youtube_dl.utils.bug_reports_message = lambda: ''

print()
print('\t*****************************')
print('\t*                           *')
print('\t*  roott youtube-dl client  *')
print('\t*                           *')
print('\t*****************************')
print()

url = input('|| enter url / query:\n|| ')
print()

print('|| you entered [' + url + '].')
confirm = input('|| confirm (y/n): ')

if (confirm == 'y'):
    titleName = input('|| please enter a file name: ')

    ytdl_format_options = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'm4a',
            'preferredquality': '192',
        }],
        'outtmpl': '/Users/roott/Documents/music/'+ titleName +'.%(ext)s',
        'restrictfilenames': True,
        'noplaylist': True,
        'nocheckcertificate': True,
        'ignoreerrors': False,
        'logtostderr': False,
        'quiet': True,
        'no_warnings': True,
        'default_search': 'auto',
        'source_address': '0.0.0.0'
    }

    ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

    try:
        print()
        print('|| attempting to download...')
        ytdl.download([url])
        print('|| file saved to directory.')
        print()

        editMD = input('|| edit metadata? (y/n): ')

        if (editMD == 'y'):
            print()
            audio = MP4("/Users/roott/Documents/music/" + titleName + ".m4a")
            artist = input('|| enter artist name: ')
            album = input('|| enter album name: ')
            audio["\xa9ART"] = artist
            audio["\xa9alb"] = album
            audio.save()
            print('metadata saved.')
        else:
            print()
            print('|| exited program.')
        print()
    except:
        print('|| there was an error when trying to download the file.')
        
else:
    print()
    print('|| exited program.')
