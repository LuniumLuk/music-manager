from flask import Flask, render_template, json, jsonify
import os
import sys
import math

app = Flask(__name__)

# 获取歌曲列表，即歌曲分区文件夹下的所有.txt的文件名
# 方便计算歌曲数量、读取歌曲信息等等
# 该函数目前并未调用
def get_list(root):
    path = sys.path[0]
    file = os.listdir(path + '/' + root)
    txt_files = []
    for f in file:
        if f.endswith('.txt'):
            txt_files.append(path + '/' + root + '/' + f)
    txt_files.sort()
    return txt_files

# 获取某种分区的所有歌曲信息
# 返回一个JSON对象
def get_songs(style):
    songs = []
    path = sys.path[0]
    files = os.listdir(path + '/static/data/' + style)
    files.sort()
    for f in files:
        if(f.endswith('.txt')):
            f_file = open(path + '/static/data/' + style + '/' + f, encoding='utf-8')
            f_content = f_file.readlines()
            songs.append({
                "id": int(f[:-4]),
                "title": f_content[0][5:-1],
                "duration": f_content[2][:-1],
                "album": f_content[4][:-1],
                "singer": f_content[6],
                "cover": '../../static/data/' + style + '/' + f[:-3] + 'png',
                "url": '../../static/data/' + style + '/' + f[:-3] + 'mp3'
            })
    return songs

all_songs = {
    "acg": get_songs('acg'),
    "man": get_songs('man'),
    "can": get_songs('can')
}

@app.route('/music')
def music(style='acg', page='1', cn='10'):
    page = int(page)
    cn = int(cn)
    songs = all_songs[style]
    max_page = math.ceil(len(songs) / cn)
    songs = songs[(page-1)*cn:page*cn]
    pages = []
    for p in range(0,max_page):
        pages.append({
            "id": p+1,
            "url": "page=" + str(p+1) + '&cn=' + str(cn)
        })
    return render_template('music_template.html', songs=songs, pages=pages, maxPage=max_page, page=page, style=style, cn=cn, href="")

@app.route('/music/<style>')
def music_style(style='acg', page='1', cn='10'):
    page = int(page)
    cn = int(cn)
    songs = all_songs[style]
    max_page = math.ceil(len(songs) / cn)
    songs = songs[(page-1)*cn:page*cn]
    pages = []
    for p in range(0,max_page):
        pages.append({
            "id": p+1,
            "url": "page=" + str(p+1) + '&cn=' + str(cn)
        })
    return render_template('music_template.html', songs=songs, pages=pages, maxPage=max_page, page=page, style=style, cn=cn, href="../")

@app.route('/music/<style>/page=<page>')
@app.route('/music/<style>/page=<page>&cn=<cn>')
def music_style_page(style='acg', page='1', cn='10'):
    page = int(page)
    cn = int(cn)
    songs = all_songs[style]
    max_page = math.ceil(len(songs) / cn)
    songs = songs[(page-1)*cn:page*cn]
    pages = []
    for p in range(0,max_page):
        pages.append({
            "id": p+1,
            "url": "page=" + str(p+1) + '&cn=' + str(cn)
        })
    return render_template('music_template.html', songs=songs, pages=pages, maxPage=max_page, page=page, style=style, cn=cn, href="../../")

# http:GET方法获取所有歌曲信息
# 需要改进，冗余较高
@app.route('/getSongs/<style>', methods=['GET'])
def get(style):
    return jsonify(all_songs[style])


if __name__ == '__main__':
    app.run(host='0.0.0.0')
