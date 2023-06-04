import json
import requests


def t01():
	headers = {'client-id': 'kimne78kx3ncx6brgo4mv6wki5h1ko'}
	ts_chat_url='https://gql.twitch.tv/gql'
	# post_body=[
	# 	{
	# 		"operationName": "ChannelVideoLength",
	# 		"variables": {
	# 			"videoID":'1754480756',
	# 			"contentOffsetSeconds": 0
	# 		},
	# 		"extensions": {
	# 			"persistedQuery": {
	# 				"version": 1,
	# 				"sha256Hash": "b70a3591ff0f4e0313d126c6a1502d79a1c02baebb288227c582044aa76adf6a"
	# 			}
	# 		}
	# 	}
	# ]

	post_body={
		"query":"query{video(id:1754480756){title,lengthSeconds}}",
		"variables":{}
	}

	# "[{\"operationName\":\"VideoCommentsByOffsetOrCursor\",\"variables\":{\"videoID\":\"" + videoId + "\",\"contentOffsetSeconds\":" + videoStart + "},\"extensions\":{\"persistedQuery\":{\"version\":1,\"sha256Hash\":\"b70a3591ff0f4e0313d126c6a1502d79a1c02baebb288227c582044aa76adf6a\"}}}]"

	# "{\"query\":\"query{video(id:\\\"" + '1754480756' + "\\\"){title,thumbnailURLs(height:180,width:320),createdAt,lengthSeconds,owner{id,displayName}}}\",\"variables\":{}}"


	# video_data_url = 'https://api.twitch.tv/v5/videos/' + '1754480756'
	# r = requests.get(video_data_url, headers=headers)

	# video_data_url='https://api.twitch.tv/helix/videos?id='+'1754480756'
	# r=requests.get(video_data_url,headers=headers)

	# {
	# 	"error": "Not Found",
	# 	"status": 404,
	# 	"message": "This API does not exist"
	# }

	r=requests.post(ts_chat_url,headers=headers,json=post_body)

	video_data = r.json()
	print(json.dumps(video_data, indent=2))

def t02():
	headers={'client-id':'kimne78kx3ncx6brgo4mv6wki5h1ko'}
	ts_chat_url='https://gql.twitch.tv/gql'

	aaa='1757234573'

	post_body={"query":"query{video(id:"+str(aaa)+"){title,lengthSeconds}}"}
	r=requests.post(ts_chat_url,headers=headers,json=post_body)
	video_data=r.json()
	print(json.dumps(video_data,indent=2))






t02()