for i in range(10):
	print(i)

a='ok'

aaa=f'''
set b_time={a}
set e_time=480

set video_name=video_%b_time%_%e_time%
set chat_name=chat_%b_time%_%e_time%

echo %vodid% %b_time%～%e_time% の処理を開始します

TwitchDownloaderCLI -m VideoDownload --id %vodid% --ffmpeg-path "ffmpeg.exe" -o %vodid%\%video_name%.mp4 -b %b_time% -e %e_time%
TwitchDownloaderCLI -m ChatDownload --id %vodid% -o %vodid%\%chat_name%.json -b %b_time% -e %e_time%
TwitchDownloaderCLI -m ChatRender -i %vodid%\%chat_name%.json -h 1080 -w 422 --framerate 30 --update-rate 0 --font-size 18 -o %vodid%\%chat_name%.mp4
'''

print(aaa)