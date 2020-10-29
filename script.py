#!/bin/python

import requests
import os
import json
import time
import pyperclip

WHITE = '\033[0m' 
RED = '\033[1;31m'
BLUE = '\033[94m'
BOLD = '\033[1m'
GREEN = '\033[32m'
OTRO = '\033[36m'
YELLOW = '\033[33m'
ENDC = '\033[0m'

logo = GREEN+r"""
                      _   _       ____  _ _ _ 
                     | | (_)     |___ \| | (_)
 _ __ ___   __ _ _ __| |_ _ _ __   __) | | |_ 
| '_ ` _ \ / _` | '__| __| | '_ \ |__ <| | | |
| | | | | | (_| | |  | |_| | | | |___) | | | |
|_| |_| |_|\__,_|_|   \__|_|_| |_|____/|_|_|_|
         @wh0001s <> greetz lowlife
"""+ENDC                                        

os.system("cls || clear")

print(logo)
arquivo = input("informe o nome ou diretório do arquivo: ")
server = 'https://apiv2.gofile.io/getServer'
s = requests.get(server)
resp = json.loads(s.text)
dados_servidor = resp.get('data')['server']
url = 'https://'+dados_servidor+'.gofile.io/uploadFile'

try:
   files = {'file': open(arquivo, 'rb')}
except:
  print(RED+"Esse arquivo não existe.")
  exit(0)

print("Uploading on "+dados_servidor+" server...")
try:
  
    r = requests.post(url, files=files)
    resposta = json.loads(r.text)
    dados_code = resposta.get('data')['code']
    dtamanho = resposta.get('data')['file']['size']
    dados_tamanho = str(dtamanho) 
    os.system("cls || clear")
    print(logo)
    print(BLUE+"Size: "+YELLOW+dados_tamanho+"bytes"+BLUE)
    print("Link: "+YELLOW+"https://gofile.io/d/"+dados_code+BLUE+"\nLink copied to your clipboard."+ENDC) 
    pyperclip.copy("https://gofile.io/d/"+dados_code)
    exit(0)

except(EnvironmentError):
    print(RED+"Ocorreu um erro no upload e não conseguimos enviar o arquivo.\n\n" + EnvironmentError)
