import numpy as np

characters = [
	'Mario',
	'DK',
	'Link',
	'Samus',
	'Yoshi',
	'Kirby',
	'Fox',
	'Pikachu',
	'Luigi',
	'Captain Falcon',
	'Ness',
	'Jigglypuff',

]


valueList = []
KOlist = []
useTimeList = []

if __name__ == "__main__":

	for character in characters:
		KOlist.append(float(input("Enter {char}'s KO --> ".format(char=character))))

	for character in characters:
		useTimeList.append(float(input("Enter {char}'s Use % --> ".format(char=character))))

	for count, KO in enumerate(KOlist):
		valueList.append(float(KOlist[count])/ useTimeList[count])


	print(valueList)

	orderedList = [x for _,x in sorted(zip(valueList,characters), reverse=True)]



	print('\n\n\n\n-- Official Rankings --')
	for count, character in enumerate(orderedList):
		if count % 3 == 0:
			print('\n'+['A','B','C','D'][count // 3] + '==========')
		print("{n}. {char} ----- ({score})".format(n=count+1, char=character, score=sorted(valueList, reverse=True)[count]))
