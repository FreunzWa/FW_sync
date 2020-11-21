import speech_recognition as sr
import os
from datetime import datetime
import time
from gtts import gTTS
from chatterbot.trainers import ChatterBotCorpusTrainer
import chatterbot

NOTE_FILE_PATH = './NOTE/'
LANGUAGE = 'en'
OUTPUT_PATH = './audioData/speechOutput.mp3'

def produce_voice_notification(notificationText):
	speechObject = gTTS(text=notificationText, lang=LANGUAGE, slow=False)
	speechObject.save(OUTPUT_PATH)
	os.system('mpg123 '+ OUTPUT_PATH)
	print(notificationText)

	

if __name__ == "__main__":

	#create a new recognizer
	r = sr.Recognizer()
	micList = sr.Microphone.list_microphone_names()
	#select an input device for the Microphone object to use
	DEVICE_INDEX = 7
	mic = sr.Microphone(device_index = DEVICE_INDEX)

	
	noteList = []
	
	while True:
		print('Speak for the recording --> ')
		with mic as source:
			r.adjust_for_ambient_noise(source) 
			audio = r.listen(source)

		try:
			recognizedText = r.recognize_google(audio)
		except sr.UnknownValueError:
			print('Unable to decode speech! Please try to speak more clearly.')
			continue

		try:
			commandName = recognizedText.split(' ')[0].upper()
			modifierName = recognizedText.split(' ')[1].upper()
			argumentString = ' '.join(recognizedText.split(' ')[2:])

			noteAliases = ['NOTES', 'NOTE', 'NO']
			exitAliases = ['EXIT', 'STOP', 'TERMINATE', 'END', 'ESCAPE', 'KILL', 'ABORT', 'QUIT']


			if commandName in noteAliases:

				if modifierName == 'TO':
					argumentString = ' '.join(recognizedText.split(' ')[3:])
					toFile = recognizedText[2]
					toFile = toFile.replace('pad', 'PAD_')

					fileName = NOTE_FILE_PATH + argumentString.replace(' ', '')
					
					if os.path.exists
					with open( + '.txt', 'w+') as file:

					print('NOTE --> ', argumentString)
					noteList.append(argumentString)
				elif modifierName == 'CREATE':
					with open(NOTE_FILE_PATH + 'PAD_'+argumentString.replace(' ', '') + '.txt', 'w+') as file:
						produce_voice_notification('Created new file.')
			elif commandName in exitAliases:
				produce_voice_notification('Aborting program.')
				break
			else:
				produce_voice_notification('The command word ({command}) is unknown. Please use a supported command.'.format(command=commandName))
				continue
		except:
			produce_voice_notification('The command failed, haha you must be stupid.')
			print(recognizedText)


print(noteList)