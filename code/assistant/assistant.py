import speech_recognition as sr
import os
from datetime import datetime
import time
from gtts import gTTS
from chatterbot.trainers import ChatterBotCorpusTrainer
import chatterbot
import threading
from mutagen.mp3 import MP3

NOTE_FILE_PATH = './NOTE/'
LANGUAGE = 'en'
OUTPUT_PATH = './audio/speechOutput.mp3'

def produce_voice_notification(notificationText):
	global canListen;
	canListen=False
	print('Making announcement')
	speechObject = gTTS(text=notificationText, lang=LANGUAGE, slow=False)
	speechObject.save(OUTPUT_PATH)
	os.system('mpg123 '+ OUTPUT_PATH)
	time.sleep(notificationTime)
	notificationTime = float(MP3(OUTPUT_PATH).info.length)
	print(notificationTime)
	print(notificationText)
	canListen = True

def voice_to_text():
	global recordingList
	while True:
		if len(recordingList) > 0:
			print('There are currently ', len(recordingList), ' queued recordings.')
			recording = recordingList.pop(0)
			try:
				recognizedText = r.recognize_google(recording)
				print(recognizedText)
			except sr.UnknownValueError:
				print('Unable to decode speech! Please try to speak more clearly.')
				produce_voice_notification("I could not understand you lol.")

def capture_voice(recognizerObject, microphone):
	global recordingList
	global canListen

	while True:
		with microphone as source:
			if canListen:
				print('Listening...')
				r.adjust_for_ambient_noise(source) 
				recording = r.listen(source)
				recordingList.append(recording)
				print('Appended a new recording!')
			else:
				print('Cant listen!')



if __name__ == "__main__":

	#create a new recognizer
	r = sr.Recognizer()
	micList = sr.Microphone.list_microphone_names()
	#select an input device for the Microphone object to use
	DEVICE_INDEX = 7
	mic = sr.Microphone(device_index = DEVICE_INDEX)

	recordingList = []
	canListen = True
	listener = threading.Thread(target= capture_voice, args=(r, mic), daemon=True)
	voiceToTextConvertor = threading.Thread(target=voice_to_text, daemon=True)
	listener.start()
	voiceToTextConvertor.start()
	
	while True:
		pass
	

