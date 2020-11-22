from cryptography.fernet import Fernet

def create_key_file():
	"""write a key and save it to a file"""
	
	newKey = Fernet.generate_key()

	with open('./encryptionKey.key', 'wb') as keyFile:
		keyFile.write(newKey)

if __name__ == "__main__":
	#create or overwrite existing key file with a new key
	create_key_file()

	exit()