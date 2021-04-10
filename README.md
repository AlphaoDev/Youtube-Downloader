# Youtube-Downloader
 Youtube video downloader script.



This script will allow you to automate the downloading of Youtube videos by classifying them by style that you will have defined yourself.



## Setting up



First, the program has been tested under Linux but should also work under Windows. You just need to import the Python module youtube-dl.

```bash
$ pip3 install youtube-dl
```



⚠️ If you are using ffmpeg package (here it's the case in the postprocessing), install it :

```bash
$ apt-get install ffmpeg
```



Now, add files in your chosen directory (where main.py is), create songs directory :

```bash
$ mkdir songs
```

In this folder will be found your different style directories of downloaded music like here (in this project) :

➜ songs

​			➜ old



Add in links.txt file the link of your video with first the tag like this :

```
old https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

Don't use youtube lists or others, just the direct link to the video.



Then, don't touch to md5.txt file, this is where the md5 sums will be recorded to check if the video has already been uploaded.



In main.py, you can change and adapt your tags that correspond to the subdirectories in the songs folder.

```python
tags = ["old"]
```



Finally, you can run your script with this command :

```bash
$ python3 main.py
```

The download information will be displayed on the terminal. If the video already exists in one of the directories then it will not be downloaded.