import speech_recognition as sr
import fbchat
import getpass
import os
import time

def specify_user_id():

	targetUserName = input('Select a user to send a message to: ')
	targetUserList = client.searchForUsers(targetUserName)
	print(targetUserList)
	targetUser = targetUserList[0]
	if not targetUser.is_friend:
		print('You have chosen a person that is not your friend! Try again.')
	else:
		uid = targetUser.uid

	return uid, targetUserName


if __name__ == '__main__':

	client = fbchat.Client('joshaughness@student.unimelb.edu.au', getpass.getpass(), max_tries=1)

	uid, name = specify_user_id()
	#create a recognizer object
	r = sr.Recognizer()

	#list available input devices
	micList = sr.Microphone.list_microphone_names()
	print('Available input devices: ', micList)

	#select an input device for the Microphone object to use
	DEVICE_INDEX = 7
	mic = sr.Microphone(device_index = DEVICE_INDEX)


	while True:

		os.system('clear')
		print('You are speaking to ', name)
		print('Speak for the recording --> ')
		with mic as source:
			audio = r.listen(source)

		try:
			text = r.recognize_google(audio)


			if text.split(' ')[0].lower() == 'message':
				validMessage = True
			else:
				validMessage = False

			#message commands
			if text == 'exit' or text=='log out' or text=='logout':
				break
			elif text == 'switch':
				uid, name = specify_user_id()
			elif validMessage:
				message = ' '.join(text.split(' ')[1:])
				output = client.send(fbchat.Message(text=message), thread_id=uid, thread_type=fbchat.ThreadType.USER)
				print('Sent message: ', message, ' to ', targetUserName)
			else:
				print('The message format is invalid. You need to specify that this is a message by beginning with the "message" keyword.')

		except:
			print('Unable to decode speech! Please try to speak more clearly.')


	if client.logout():
		print('Log out successful.')
	else:
		print('Log out was not successful.')