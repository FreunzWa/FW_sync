import os



while True:
    outputPath = 'C:/Users/Jack/Music/'
    URL = input('Enter YT video URL\n==> ')
    try:
        command = 'youtube-dl -o 	'.format(p=outputPath, u=URL)
        print(command)
        os.system(command)
    except:
        print('Download failed')
    
