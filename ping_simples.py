import os #Importa o módulo os (integra os programas e recursos do S.O)

ip_ou_host = input("Digite o IP ou HOST a ser verificado: ")

os.system(f'ping -n 6 {ip_ou_host}') #-n = número de pacotes.