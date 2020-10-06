from flask import Flask
import os
import sys

pagefile = open("music.html", "r")
htmlpage = pagefile.read()
pagefile.close()

G_page = 1
G_mid = "001"

app = Flask(__name__)

def get_music_list(root):
	path = sys.path[0]
	file = os.listdir(path + '/' + root)
	file.sort()
	music_text = htmlpage
	for f in file:
		if f.endswith('.txt'):
			f_content = open(path + '/' + root + '/' + f)
			music_text = music_text + "\n\t\t\t\t<p><a href = 'page=" + G_page + \
			    "&mid=" + f[:-4] + "'>" + f[:-4] + f_content.readline()[5:] + "</a></p>"
			f_content.close()
	return music_text + "\n\t\t\t</div>"


@app.route('/music/page=<page>&mid=<mid>')
def hello_world(page, mid):
	global G_page
	global G_mid
	if(page):
		G_page = page
	if(mid):
		G_mid = mid
	root = "static/data/music_" + "%02d" % int(G_page)
	page_content = get_music_list(root)
	page_content = page_content + "\n\t\t\t<div class = 'music-player'>"
	page_content = page_content + "\n\t\t\t\t<img src = '../" + root + '/' + G_mid + ".png' width = 256px height = 256px/>"
	f_file = open(sys.path[0] + '/' + root + '/' + G_mid + ".txt")
	f_content = f_file.readlines()
	for f in f_content:
		if(f):
			page_content = page_content + "\n\t\t\t\t<div>" + f + "</div>"
	page_content = page_content + "\n\t\t\t\t<audio src = '../" + root + '/' + G_mid + ".mp3' controls = 'controls'>Your Browser Does Not Support Audio</audio>"
	page_content + page_content + "\n\t\t\t</div>\n\t\t</div>\n\t</body>\n</html>"
	return page_content

if __name__ == '__main__':
	app.run(host='0.0.0.0')
