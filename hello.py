from flask import Flask
import os
import sys

vuefile = open("firstvue.html", "r")
logfile = open("gunicorn.log", "r")
app = Flask(__name__)

vuecontent = vuefile.read()
logcontent = logfile.read()

vuefile.close()
logfile.close()

def get_music_text_content(root):
	file = os.listdir(root)
	music_text = ''
	for f in file:
		if f.endswith('.txt'):
			f_content = open(root+'/'+f)
			music_text = music_text + "<p>" + f_content.read() + "</p>"
			music_text = music_text + "<img src = '" + root + "/" + f[:-3] + "png'/>"
			f_content.close()
	return music_text

@app.route('/')
def hello_world():
	return vuecontent

@app.route('/log')
def log():
	return logcontent

@app.route('/music_01')
def music_01():
	return get_music_text_content('/data/music_01')

@app.route('/music_02')
def music_02():
	return get_music_text_content('/data/music_02')





if __name__ == '__main__':
	app.run(host='0.0.0.0')
