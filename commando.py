import time
import os
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random

purple = '\x1b[38;5;165m'
blue = '\x1b[38;5;33m'
red = '\x1b[38;5;196m'
green = '\x1b[38;5;118m'
grey = '\x1b[38;5;0m'
pink = '\x1b[38;5;199m'

print(f'''{grey}
	                               ,▄▄▄▄▄╓,
                   ,,▄▄▄▄▓█████████████████████▓▓▄▄▄▄,,
                 ▀▀████████████████████████████████████████▓▄▄▄▄▄▄▄,
                ▄▄██████████████████████████████████████████████▌▄╓▄∩
             ▄██▀▀████████████████████████████████████████████████▄,     '
            `   ▄█████████{pink}▓{grey}████{pink}▓▓▓▓▓▓▓▓▓{grey}███████{pink}▓{grey}██████▄▄L,
              ▄██████████{pink}▓{grey}███{pink}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓{grey}████{pink}▓{grey}███████▀
             └▀╙ ▓██████{pink}▓{grey}██{pink}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓{grey}███{pink}▓▓▓{grey}████▀╙`
                ,███████{pink}▓{grey}██{pink}▓▓▓▓▓▓{grey}████{pink}▓▓▓▓▓▓▓▓▓{grey}██{pink}▓{grey}███
                ▓██████████{pink}▓▓▓▓▓▓{grey}█████{pink}▓▓▓▓▓▓▓▓{grey}██{pink}▓{grey}█████m
                ████████{pink}▓{grey}████{pink}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓{grey}████████████████████,
               J█████████{pink}▓{grey}████{pink}▓▓▓▓▓▓▓▓▓▓▓▓▓▓{grey}███{pink}▓{grey}██████▀╙
               ╟█████████████{pink}▓▓▓▓▓▓▓▓▓▓▓▓▓{grey}████{pink}▓{grey}████████████████▀
             {pink} ▄▓▓{grey}████████████{pink}▓▓▓{grey}█████████████████████████████████▀{pink}╨
             Φ▌▓▓▓{grey}███████████████████████████████████████{pink}▓▓▓▓▌Å"`
              ⌐'╫▓▓▓▓▓▓▓▓▓▓▓▓▓{grey}███████████████████████{pink}▓▓▓▓▓▓▓Ñ`
              `  "▌░╟╫╨╢║╣▀▓▓▓▀▀▀▓▓▓▓▓▓▓▓▓▓▓▓▓▓▌▀▀▀▀╣ÖÅ`╠░║▓:
             `    ▌ "╫. j  ▓▓▒" ``╟╫M` ```└```     ╙⌂║. "Ñ▓▌ Written By AuxGrep
                 ▐M `╨H ¿ "▓▓╫    ╣Ñ      j         ╣╬   ║▓    pew! pew!!
                 ╬   :Ñ"  ╫▓╣Ü    ╣░      j         ╙▌   ╣▌        2019
                 ''')

def encrypt(key, filename):
	chunksize = 64*1024
	outputFile = "(secured)"+filename
	filesize = str(os.path.getsize(filename)).zfill(16)
	IV = Random.new().read(16)

	system = AES.new(key, AES.MODE_CBC, IV)

	with open(filename, 'rb') as infile:
		with open(outputFile, 'wb') as outfile:
			outfile.write(filesize.encode('utf-8'))
			outfile.write(IV)
			
			while True:
				chunk = infile.read(chunksize)
				
				if len(chunk) == 0:
					break
				elif len(chunk) % 16 != 0:
					chunk += b' ' * (16 - (len(chunk) % 16))

				outfile.write(system.encrypt(chunk))


def decrypt(key, filename):
	chunksize = 64*1024
	outputFile = filename[11:]
	
	with open(filename, 'rb') as infile:
		filesize = int(infile.read(16))
		IV = infile.read(16)

		unlock = AES.new(key, AES.MODE_CBC, IV)

		with open(outputFile, 'wb') as outfile:
			while True:
				chunk = infile.read(chunksize)

				if len(chunk) == 0:
					break

				outfile.write(unlock.decrypt(chunk))
			outfile.truncate(filesize)


def getKey(password):
	hasher = SHA256.new(password.encode('utf-8'))
	return hasher.digest()
time.sleep(2)

def Main():
	choice = input("what can i help you (E)ncrypt or (D)ecrypt?: ")

	if choice == 'E':
		filename = input("Enter File to encrypt: ")
		password = input("Password: ")
		encrypt(getKey(password), filename)
		print("Okay Done.")
	elif choice == 'D':
		filename = input("Enter File to decrypt: ")
		password = input("Password: ")
		decrypt(getKey(password), filename)
		print("Okay Done.")
	else:
		print("GoodNight and fuck you!!!! use E or D for encryption and Decryption")

if __name__ == '__main__':
	Main()


