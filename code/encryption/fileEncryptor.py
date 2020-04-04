from cryptography.fernet import Fernet
import os
import sys


def load_key(keyPath):
    """load an encryption key from keypath as specified"""
    return open(keyPath, "rb").read()

def encrypt_file(filePath, key):
    """encrypt the specified file with the key and save the file"""
    f = Fernet(key)

    if '.crypt' in filePath:
        print('It appears that ' + filePath + ' has already been encrypted.')
        print('Any file that contains ".crypt" will be flagged as already\
            having been encrypted.')
        return 0 
    elif '.key' in filePath:
        print('It appears ' + filePath + ' is a cryptographic key.')
        print('Skipping...')
        return 0

    #get the unencrypted file data
    with open(filePath, 'rb') as file:
        fileData = file.read()

    #generate the encrypted version of the data.
    encryptedData = f.encrypt(fileData)

    splitPath = filePath.split('/')
    if len(splitPath) > 1:
        encryptedName = f.encrypt(bytes(splitPath[-1], 'utf-8'))
    else:
        print('It seems that a file did not have the correct directory structure')
        return 0

    #write the encrypted data to the same file 
    #to overwrite it.
    with open(filePath, 'wb') as file:
        file.write(encryptedData)

    encryptedNameString = str(encryptedName, 'utf-8')
    #rename the file to show that it has been encrypted
    os.rename(filePath, '/'.join(splitPath[:-1]) + '/' + encryptedNameString + '.crypt')

    return 1



def decrypt_file(encryptedFilePath, key):
    """encrypt the specified file with the key and save the file"""
    f = Fernet(key)

    try:
        with open(encryptedFilePath, 'rb') as file:
            fileData = file.read()

        decryptedData = f.decrypt(fileData)
        #write the encrypted data to the same file 
        #to overwrite it.
        with open(encryptedFilePath, 'wb') as file:
            file.write(decryptedData)
    except:
        pass

    try:

        splitPath = filePath.split('/') 
        encryptedName = (splitPath[-1])
        encryptedNameBytes = bytes(encryptedName, 'utf-8')
        decryptedName = f.decrypt(encryptedNameBytes)

        if '.crypt' not in encryptedFilePath and 0:
            print('It appears that ' + encryptedFilePath + ' has not been encrypted.')
            print('Skipping...')
            return 0 
        if '.key' in encryptedFilePath:
            print('It appears ' + encryptedFilePath + ' is a cryptographic key.')
            print('Skipping...')
            return 0

        #get the unencrypted file data
        with open(encryptedFilePath, 'rb') as file:
            fileData = file.read()

        splitPath = filePath.split('/') 
        encryptedName = (splitPath[-1]).replace('.crypt', '')
        encryptedNameBytes = bytes(encryptedName, 'utf-8')

        if len(splitPath) > 1:
            decryptedName = str(f.decrypt(encryptedNameBytes), 'utf-8')
        else:
            print('It seems that a file did not have the correct directory structure')
            return 0

        #rename the file to show that it has been encrypted
        os.rename(filePath,('/'.join(splitPath[:-1]) + '/' + decryptedName))
        print('decrypted file ', decryptedName)
    except:
        pass

    return 1
    

  
if __name__ == '__main__':
    

    TARGET_BASE_PATH = sys.argv[1]  

    if not os.path.exists:
        print('Aborting because cannot find ' + TARGET_BASE_PATH)
        exit()
    if TARGET_BASE_PATH == '/':
        print('You entered "/" as the encryption path. It seems that you are trying to encrypt the entire memory.')
        exit()

    #path to the key file
    KEY_PATH = './encryptionKey.key'


    #load the key string from the key file
    key = load_key(KEY_PATH)


    if sys.argv[2] == 'encrypt-all':

        for directory in os.walk(TARGET_BASE_PATH):
            if directory == '/.git':
                print('Will not encrypt the .git directory')
                continue
            files = directory[2]
            for fileName in files:
                filePath = directory[0] + '/' + fileName

                encrypt_file(filePath, key)

    elif sys.argv[2] == 'decrypt-all':

        for directory in os.walk(TARGET_BASE_PATH):
            if directory == '/.git':
                print('Will skip the .git directory')
                continue
            files = directory[2]
            for fileName in files:
                filePath = directory[0] + '/' + fileName

                decrypt_file(filePath, key)
    else:
        print('Please enter a valid command: either encrypt-all or decrypt-all')
        print(sys.argv[1])

    print('Process complete.')

