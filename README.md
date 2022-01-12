# music manager

a Flask Program designed for Digital Assets Management Course Assignement

### Deploy
1.this program can be depolyed via gunicorn:
```
gunicorn -b [url:port] main:app
or
./gunicorn.sh
```
2.or deployed by Flask
```
flask main.py
```

### Music Database
music data are required to run this program by adding .txt .mp3 and .png files
to ./static/data/music/<style> folder

named them by "001.mp3" "001.png" "001.txt" and so on

**for each song, all three types of file are required**

### Demo
This program has already been depolyed in Tencent Cloud Server

A Demo Webpage: <a href="http://49.233.128.64:5000/music" target="_blank">DAM Music Manager V1.0.0</a>

This program currently remains an **assignment work**

do not simply copy the code if you're a student facing same assignment

All Rights Reserved @ LuniumLuk_ZJU
