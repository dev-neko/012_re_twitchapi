import requests
import json
import csv

# 本来はもうAPIを使用してアーカイブのコメントは取得できないが、Twitch自身のclient_idを使用することで現在でも取得可能だがグレーな方法
# https://ja.stackoverflow.com/questions/83617/twitch-api-を用いてアーカイブ動画のコメントを取得したい
client_id = 'kimne78kx3ncx6brgo4mv6wki5h1ko'
video_id = '1246355359'

# 一回目のリクエスト
url = 'https://api.twitch.tv/v5/videos/' + video_id + '/comments?content_offset_seconds=0'
headers = {'client-id': client_id}
r = requests.get(url, headers=headers)
print(r)
row_data = r.json()
print(row_data)

with open('comments.csv', 'a',encoding='utf-8', errors='ignore') as f:
	writer = csv.writer(f)
	for comment in row_data['comments']:
		writer.writerow([
			comment['content_offset_seconds'],
			comment['message']['body']
		])

# 二回目以降のリクエスト
while '_next' in row_data:
	url = 'https://api.twitch.tv/v5/videos/' + video_id + '/comments?cursor=' + row_data['_next']
	headers = {'client-id': client_id}
	r = requests.get(url, headers=headers)
	row_data = r.json()

	with open('comments.csv', 'a',encoding='utf-8', errors='ignore') as f:
		writer = csv.writer(f)
		for comment in row_data['comments']:
			writer.writerow([
				comment['content_offset_seconds'],
				comment['message']['body']
			])


DATABASES = {
	'default':{
		'ENGINE':'django_cockroachdb',
		'NAME':'defaultdb',
		'USER':'test_user_001',
		'PASSWORD':'4tdFSRpN5_0wDmDKNotSqw',
		'HOST':'forge-warthog-3911.8nk.cockroachlabs.cloud',
		'PORT':'26257',
	},
}

DATABASES = {
	'default':{
		'ENGINE':'django_cockroachdb',
		'NAME':os.environ['NAME'],
		'USER':os.environ['USER'],
		'PASSWORD':os.environ['PASSWORD'],
		'HOST':os.environ['HOST'],
		'PORT':os.environ['PORT'],
	},
}