import speech_recognition as sr
import os
import time
from gtts import gTTS
from chatterbot.trainers import ChatterBotCorpusTrainer
import chatterbot

LANGUAGE = 'en'
OUTPUT_PATH = './audioData/speechOutput.mp3'

if __name__ == '__main__':

	#train the chatterbot
	chatbot = chatterbot.ChatBot('HAL 9001')
	trainer = chatterbot.trainers.ChatterBotCorpusTrainer(chatbot)
	trainer.train('chatterbot.corpus.english', 
    "chatterbot.corpus.english.greetings",
    "chatterbot.corpus.english.conversations")

	#create a recognizer object
	r = sr.Recognizer()

	#list available input devices
	micList = sr.Microphone.list_microphone_names()
	print('Available input devices: ', micList)

	#select an input device for the Microphone object to use
	DEVICE_INDEX = 7
	mic = sr.Microphone(device_index = DEVICE_INDEX)

	while True:
		print('Speak for the recording --> ')	
		with mic as source:
			audio = r.listen(source)

		try:
			recognizedText = r.recognize_google(audio)	
			print('Heard: ', recognizedText)

			responseText = chatbot.get_response(recognizedText).text

			speechObject = gTTS(text=responseText, lang=LANGUAGE, slow=False)
			speechObject.save(OUTPUT_PATH)
			print('Echoing speech --> ')
			os.system('mpg123 '+ OUTPUT_PATH)


		except:
			print('Unable to decode speech! Please try to speak more clearly.')

		

	if client.logout():
		print('Log out successful.')
	else:
		print('Log out was not successful.')