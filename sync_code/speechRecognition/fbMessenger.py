import fbchat
import getpass

client = fbchat.Client('joshaughness@student.unimelb.edu.au', getpass.getpass())

uid = client.searchForUsers('Cody Gu')[0].uid
client.send(fbchat.Message(text='Wow. very cool museum you have there. :) You need to start a bee exhibit.'), thread_id=uid, thread_type=fbchat.ThreadType.USER)