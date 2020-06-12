import os



while True:
    outputPath = 'C:/Users/Jack/Music/'
    URL = input('Enter YT video URL\n==> ')
    try:
        os.system('youtube-dl --extract-audio --audio-format mp3 -o "{p}%(title)s.%(ext)s" {u}'.format(p=outputPath, u=URL))
    except:
        print('Download failed')
    
