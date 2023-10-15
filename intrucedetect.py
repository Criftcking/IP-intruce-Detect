import subprocess
import re
import colorama
import os
from colorama import Fore
rs = Fore.RESET
colorama.init()


import os

def limpiar():
    sistema = os.name  # Obtener el nombre del sistema operativo

    if sistema == 'posix':  # Si es un sistema basado en Unix/Linux
        os.system('clear')
    elif sistema == 'nt':  # Si es un sistema Windows
        os.system('cls')
    else:
        print("No se puede determinar el sistema operativo.")



limpiar()




def obtener():
    result = subprocess.run(["arp", "-a"], stdout=subprocess.PIPE, text=True)
    resp = (result.stdout)
    print(Fore.RED+"Las Ip actuales son: \n" + resp+Fore.RESET)
    
    cond = input(Fore.YELLOW+"Quieres guardarlas en get.txt ? (si | no)---> "+Fore.RESET)
    
    
    if cond == 'si' or "SI" or "Si":
            result = subprocess.run(["arp", "-a"], stdout=subprocess.PIPE, text=True)
            resp = (result.stdout)


            ip_addresses = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', resp)
            with open("get.txt", "w") as file:
                for ip in ip_addresses:
                    file.write(ip + "\n")
                    
    elif cond == "no" or "NO" or "No":
        pass
    print("\n")
    input("Presiona 'Enter Para Continuar..'")

    
    initi()
    




def ipconf():
    archivo = 'ip_de_confianza.txt'
    with open(archivo, "r") as file:
        direcciones_ip = file.read().splitlines()
        print(Fore.LIGHTBLUE_EX+"Las IP de confianzas son: \n"+Fore.RESET)
        for ip in direcciones_ip:
            print(ip)
            
            
    print("\n")
    input("Presiona 'Enter Para Continuar..'")
    initi()





def detect():
    input(Fore.YELLOW+"Coloca las ip de confianzas en ip_de_confianza.txt\n\nPresiona 'ENTER' para continuar.."+ rs)
    
    result = subprocess.run(["arp", "-a"], stdout=subprocess.PIPE, text=True)
    #resp = (result.stdout)


  
    archivo_actual = "get.txt"
    archivo_anterior = "ip_de_confianza.txt"


    def leer_direcciones_ip(archivo):
        with open(archivo, "r") as file:
            direcciones_ip = file.read().splitlines()
        return set(direcciones_ip)


    direcciones_ip_actuales = leer_direcciones_ip(archivo_actual)


    direcciones_ip_anteriores = leer_direcciones_ip(archivo_anterior)

 
    nuevas_direcciones_ip = direcciones_ip_actuales - direcciones_ip_anteriores

    if nuevas_direcciones_ip:
        print("Se han detectado direcciones IP nuevas:")
        
        with open("NuevasIP.txt", "w") as file:
            for ip in nuevas_direcciones_ip:
                file.write(ip + "\n")
                
        for ip in nuevas_direcciones_ip:
            print(ip)
            
        print("\n")
        input("Presiona 'Enter Para Continuar..'")
        initi()  
    
    else:
        print("No se han detectado direcciones IP nuevas.")
    initi()
        





def initi():
    limpiar()
    print(Fore.LIGHTYELLOW_EX+"Bienvenido a mi Programa IP INTRUSO DETECT\n"+Fore.RESET)
    print(Fore.BLUE+"Elige Una Opcion\n1-Ver IP Actuales conectadas a mi red\n2-Ver Las IP de confianza\n3-Detectar las IP Intruso en mi PC\n4-SALIR"+Fore.RESET)
    print()
    resp = int(input("Elige tu opcion---> "))


    if resp == 1:
        limpiar()
        obtener()
        
    elif resp == 2:
        limpiar()
        ipconf()
        
    elif resp == 3:
        limpiar()
        detect()
       
    elif resp == 4:
        print()
        
    else:
        input("Opcion incorrecta. Press 'ENTER To Continue..'")
        
        
initi()