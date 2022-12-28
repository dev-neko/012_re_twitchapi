from pprint import pprint

import requests

def aaa():
	client_id = 'kimne78kx3ncx6brgo4mv6wki5h1ko'
	headers = {'client-id': client_id}

	ts_chat_url = 'https://api.twitch.tv/v5/videos/1678722379/comments?content_offset_seconds=0'
	r=requests.get(ts_chat_url,headers=headers)
	print(r)
	ts_chat_data=r.json()
	print(ts_chat_data)

	video_data_url = 'https://api.twitch.tv/v5/videos/1678722379'
	r = requests.get(video_data_url, headers=headers)
	print(r)
	video_data = r.json()
	print(video_data)
# aaa()

def bbb():
	headers={'client-id':'kimne78kx3ncx6brgo4mv6wki5h1ko'}
	ts_chat_url='https://gql.twitch.tv/gql'
	videoID="1560074296"
	body1=[
		{
			"operationName": "VideoCommentsByOffsetOrCursor",
			"variables": {
				"videoID":videoID,
				"contentOffsetSeconds": 0
			},
			"extensions": {
				"persistedQuery": {
					"version": 1,
					"sha256Hash": "b70a3591ff0f4e0313d126c6a1502d79a1c02baebb288227c582044aa76adf6a"
				}
			}
		}
	]


	body2=[
		{
			"operationName": "VideoCommentsByOffsetOrCursor",
			"variables": {
				"videoID":videoID,
				"cursor":"eyJpZCI6IlY3ajFCMHF5Q2hjY05RIiwiaGsiOiJ2aWRlbzoxNTYwMDc0Mjk2Iiwic2siOiJBQUFBVnhRakhBQVhDckpLQl9SWDVBIn0"
			},
			"extensions": {
				"persistedQuery": {
					"version": 1,
					"sha256Hash": "b70a3591ff0f4e0313d126c6a1502d79a1c02baebb288227c582044aa76adf6a"
				}
			}
		}
	]

	r=requests.post(ts_chat_url,headers=headers,json=body1)
	# print(r)
	ts_chat_data=r.json()
	# pprint(ts_chat_data)

	ts_chat_dist_new=[]
	for i in ts_chat_data[0]['data']['video']['comments']['edges']:
		ts=i['node']['contentOffsetSeconds']
		chat=''.join([d.get('text') for d in i['node']['message']['fragments']])
		# print(ts,chat)
		ts_chat_dist_new+=[{'ts':ts,'chat':chat}]
	pprint(ts_chat_dist_new)

	if not ts_chat_data[0]['data']['video']['comments']['pageInfo']['hasNextPage']:
		print('なし')
	else:
		cursor=ts_chat_data[0]['data']['video']['comments']['edges'][-1]['cursor']
		print(cursor)


		# pprint(i['node']['message']['fragments'].get('text'))
		# for j in i['node']['message']['fragments']:
		# 	bbb+=j['text']
		# print(bbb)

	print('------------------------------')

	# r=requests.post(ts_chat_url,headers=headers,json=body2)
	# # print(r)
	# ts_chat_data=r.json()
	# # pprint(ts_chat_data)
	#
	# aaa=ts_chat_data[0]['data']['video']['comments']['edges']
	# for i in aaa:
	# 	bbb=str(i['node']['contentOffsetSeconds'])+' '
	# 	for j in i['node']['message']['fragments']:
	# 		bbb+=j['text']
	# 	print(bbb)

bbb()

def ccc():
	import requests
	import re

	homepage = requests.get("https://www.twitch.tv").text
	client_id = re.search('"Client-ID" ?: ?"(.*?)"', homepage).group(1)
# ccc()