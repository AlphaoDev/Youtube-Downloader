# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import youtube_dl
from pathlib import Path
import hashlib
import time

# List of tags corresponding to the directories in the songs folder
tags = ["old"]

# Main function to download Youtube video(s)
def download():
    # Open links file
    with open("links.txt","r") as link_file:
        lines = link_file.readlines()
        # For each links line in file
        for line in lines:
            # For each tag in tags list
            for tag in tags:
                data = line.split()
                # If first string in links file equals current tag
                if data[0] == tag:
                    link = str(data[1])
                    # Create md5sum for each link to check if file is already downloaded
                    hash_obj = hashlib.md5(link.encode())
                    md5 = hash_obj.hexdigest()
                    # Open md5 file
                    with open("md5.txt","r+") as md5_file:
                        lines = md5_file.readlines()
                        # Check if md5 is in file
                        for line in lines:
                            if str(md5) in line:
                                print("File already here, md5sum : {}.".format(md5))
                                break
                        else:
                            # Options to download Youtube file
                            ydl_opts = {
                                'outtmpl': 'songs/{}/%(title)s.%(ext)s'.format(tag),
                                'quiet': True,
                                'format': 'bestaudio/best',
                                'postprocessors': [{
                                    'key': 'FFmpegExtractAudio',
                                    'preferredcodec': 'mp3',
                                    'preferredquality': '320',
                                }],
                            }
                            # Try to download video
                            try:
                                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                                    ydl.cache.remove()
                                    infos = ydl.extract_info(link, download=False)
                                    title = infos.get('title', None)
                                    ydl.download([link])
                                    print("File downloaded, title : {}.".format(title))
                                    # Write md5 if it isn't here
                                    md5_file.write(str(md5) + "\n")
                            except Exception:
                                print("Link {} is not downloadable".format(link))

if __name__ == "__main__":
    # Set timer
    timer_start = time.time()
    # Launch download function
    download()
    # Get final timer
    timer_end = time.time()
    timer_result = round(timer_end  - timer_start,3)
    # Print timer
    print("\nThe process lasted : {} s.".format(timer_result))