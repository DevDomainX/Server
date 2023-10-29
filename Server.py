
import os
from time import sleep
from colorama import init, Fore, Style
init()

title =Fore.GREEN+Style.BRIGHT+ """ 
>>> Created by: Hans Saldias <<<<

>> by: 1 LugarParaProgramar <<

= > Servidor de archivos 

=>  activa el servidor en la carpeta de los 

=>  archivos que deseas compartir 

=> y con la ip que arroja y el puerto 

 => ingresalo en chrome o google
 
  => y listo.  """
for i in title:
    print(i, end="", flush=True)
    sleep(0.1)
p = input("Deseas iniciar el servidor: ").lower()
while not p.isalpha():
    p = input("Deseas iniciar el servidor (si/no): ").lower()
if p == "si":
    port = input("Ingresa el puerto eje 8080: ")
    os.system("pkg install python")
    os.system("pkg install python2")
    os.system("pkg install python3")
    os.system("ifconfig")
    os.system("python3 -m http.server "+port)
else:
    print("\nGracias por usar mi Script\nCreated by: Hans Saldias")
    