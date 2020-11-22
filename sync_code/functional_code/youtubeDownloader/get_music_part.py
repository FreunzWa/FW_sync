import os



while True:
    outputPath = 'C:/Users/freunzwa/Music'
    URL = input('Enter YT video URL\n==> ')
    try:
    	new_url = os.popen('youtube-dl -g "{u}"'.format(u=URL)).read()
    	os.system('ffmpeg -ss 00:00:15.00 -i "{u}" -t 00:00:10.00 -c copy ./out.mp3'.format(u=new_url))
    except AttributeError:
        print('Download failed')
    


