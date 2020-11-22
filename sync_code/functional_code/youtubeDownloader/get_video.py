import os

PATH = './output/'

while True:
	if not os.path.exists('./output/'):
		os.system('mkdir output')
    outputPath = PATH
    URL = input('Enter YT video URL\n==> ')
    try:
        os.system('youtube-dl -f mp4/bestvideo+bestaudio -o "{p}%(title)s.%(ext)s" {u}'.format(p=outputPath, u=URL))
    except:
        print('Download failed')
    
