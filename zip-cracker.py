import os
import zipfile
import argparse
import sys
from tqdm import tqdm
def banner():
	os.system("clear")
	os.system("cat banner")
def get_arguments():
	banner()
	parser = argparse.ArgumentParser()
	parser.add_argument("-z","--zipfile",dest="zip",help="Path of zipfile you want to crack")
	parser.add_argument("-w","--wordlist",dest="wordlist",help="Your world list file path")
	options = parser.parse_args()
	if not options.zip:
		print ("[!] pyyhon3 zip-cracker.py -h")
		print ("[!] Usage: python3 zip-cracker.py --zipfile filename.zip --wordlist worslist.txt")
		sys.exit()
	if not options.wordlist:
		print ("[!] pyyhon3 zip-cracker.py -h")
		print ("[!] Usage: python3 zip-cracker.py --zipfile filename.zip --wordlist worslist.txt")
		sys.exit()
	return options
def crack_zip():
	options = get_arguments()
	wordlist = options.wordlist
	zip = zipfile.ZipFile(options.zip)
	len_word = len(list(open(wordlist, "rb")))
	print (f"\n\n[+] Trying total passwors : {len_word}\n\n")
	with open(wordlist, "rb") as wordlist:
		for word in tqdm(wordlist,  total=len_word, unit="Passwords",desc="[+] Trying passwords"):
			try :
				zip.extractall(pwd=word.strip())
			except KeyboardInterrupt:
				sys.exit()
			except :
				continue
			else:
				global i
				i = word.decode().strip()
				break
	try:
		print (f"\n\n[+] Password found : {i}\f")
	except:
		print ("\n\n[!] Password not found try another wordlist.\f")
try :
	crack_zip()
except FileNotFoundError as e:
	print (f"{e}\n[!]Pleas specify an existing file")
except KeyboardInterrupt:
	sys.exit()
except Exception as x:
	print (x)
