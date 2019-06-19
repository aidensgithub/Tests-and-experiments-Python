#aiden
import requests
import json
import time
import os
import random
import sys

def Input(text):
	value = ''
	if sys.version_info.major > 2:
		value = input(text)
	else:
		value = raw_input(text)
	return str(value)

#главный класс
class Instasign():
	def __init__(self, username, passwordsFile='passw.txt'):
		self.username = username
		self.CurrentProxy = ''
		self.UsedProxys = []
		self.passwordsFile = passwordsFile
		
		#проверка1
		self.loadPasswords()
		#проверка логина
		self.IsUserExists()


		UsePorxy = Input('[*] Do you want to use proxy (y/n): ').upper()
		if (UsePorxy == 'Y' or UsePorxy == 'YES'):
			self.randomProxy()


	#проверка пароля
	def loadPasswords(self):
		if os.path.isfile(self.passwordsFile):
			with open(self.passwordsFile) as f:
				self.passwords = f.read().splitlines()
				passwordsNumber = len(self.passwords)
				if (passwordsNumber > 0):
					print ('[*] %s Passwords loaded successfully' % passwordsNumber)
				else:
					print('No passwords init, Please add passwords to it.')
					Input('[*] Press enter to exit')
					exit()
		else:
			print ('Please create passwords file named "%s"' % self.passwordsFile)
			Input('[*] Press enter to exit')
			exit()

	#случайные прокси
	def randomProxy(self):
		plist = open('proxies.txt').read().splitlines()
		proxy = random.choice(plist)

		if not proxy in self.UsedProxys:
			self.CurrentProxy = proxy
			self.UsedProxys.append(proxy)
		try:
			print('')
			print('[*] Check new ip...')
			print ('[*] Your public ip: %s' % requests.get('http://myexternalip.com/raw', proxies={ "http": proxy, "https": proxy },timeout=10.0).text)
		except Exception as e:
			print  ('[*] Can\'t reach proxy "%s"' % proxy)
		print('')


	#проверка логина 2
	def IsUserExists(self):
		r = requests.get('https://www.instagram.com/%s/?__a=1' % self.username) 
		if (r.status_code == 404):
			print ('[*] User named "%s" not found' % username)
			Input('[*] Press enter to exit')
			exit()
		elif (r.status_code == 200):
			return True

	#попытка входа
	def Login(self, password):
		sess = requests.Session()

		if len(self.CurrentProxy) > 0:
			sess.proxies = { "http": self.CurrentProxy, "https": self.CurrentProxy }
#unfinished-незаконченный проект

