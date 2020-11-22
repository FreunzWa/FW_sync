import os

PATH = './output/'

while True:

    outputPath = PATH
    if not os.path.exists('./output/'):
        os.system('mkdir output')

    URL = input('Enter YT video URL\n==> ')

    os.system('youtube-dl --extract-audio --audio-format mp3 -o "{p}%(title)s.%(ext)s" {u}'.format(p=outputPath, u=URL))

