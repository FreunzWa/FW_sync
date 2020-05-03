import speech_recognition as sr
import os
import time
from gtts import gTTS
from chatterbot.trainers import ChatterBotCorpusTrainer
import chatterbot
from playsound import playsound



LANGUAGE = 'en-uk'
OUTPUT_PATH = './audioData/speechOutput.mp3'


def play_response(message):
	responseText = chatbot.get_response(message).text
	speechObject = gTTS(text=responseText, lang=LANGUAGE, slow=False)
	speechObject.save(OUTPUT_PATH)
	print('Echoing speech --> ')
	playsound(OUTPUT_PATH)


if __name__ == '__main__':

	#train the chatterbot
	chatbot = chatterbot.ChatBot('HAL 9001')
	trainer = chatterbot.trainers.ChatterBotCorpusTrainer(chatbot)
	trainer.train('chatterbot.corpus.english') 
	trainer.train('chatterbot.corpus.english.greetings') 
	trainer.train('chatterbot.corpus.english.conversations') 

	#create a recognizer object
	r = sr.Recognizer()

	#list available input devices
	micList = sr.Microphone.list_microphone_names()
	print('Available input devices: ', micList)

	#select an input device for the Microphone object to use
	DEVICE_INDEX = 5
	mic = sr.Microphone(device_index = DEVICE_INDEX)



	play_response('Hello!')


	while True:


		print('Speak for the recording --> ')	
		with mic as source:
			audio = r.listen(source)

		try:
			recognizedText = r.recognize_google(audio)	

			print('Heard: ', recognizedText)
			play_response(recognizedText)



		except:
			print('Unable to decode speech! Please try to speak more clearly.')

	

	if client.logout():
		print('Log out successful.')
	else:
		print('Log out was not successful.')