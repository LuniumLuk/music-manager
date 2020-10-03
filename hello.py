from flask import Flask
import os
import sys

vuefile = open("firstvue.html", "r")
logfile = open("gunicorn.log", "r")
musicfile = open("music.html", "r")
app = Flask(__name__)

vuecontent = vuefile.read()
logcontent = logfile.read()
musiccontent = musicfile.read()

vuefile.close()
logfile.close()
musicfile.close()

def get_music_text_content(root):
	path = sys.path[0]
	file = os.listdir(path + '/' + root)
	music_text = musiccontent
	for f in file:
		if f.endswith('.txt'):
			f_content = open(path + '/' + root+'/'+f)
			music_text = music_text + "\n<div class = 'music-card'>\n<p style = 'width: 40%'>" + f_content.read() + "</p>"
			music_text = music_text + "\n<img class = 'music-cover' height = 120px width = 120px src = '" + root + '/' + f[:-3] + "png' alt = '" + f[:-3] + "png' />"
			music_text = music_text + "\n<audio class = 'music-player' src = '" + root + '/' + f[:-3] + "mp3' controls = 'controls'>Your Browser does not support audio</audio>\n</div>"
			f_content.close()
	return music_text + "\n</body>\n</html>"

@app.route('/')
def hello_world():
	return vuecontent

@app.route('/log')
def log():
	return logcontent

@app.route('/music_01')
def music_01():
	return get_music_text_content('static/data/music_01')

@app.route('/music_02')
def music_02():
	return get_music_text_content('static/data/music_02')





if __name__ == '__main__':
	app.run(host='0.0.0.0')
