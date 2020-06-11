#manipulacion  de archivos txt
#archivo = open("pilio.txt", "x")
#archivo.write("hola curso pyhon \n lnea2")
archivo = open("pilio.txt", "w") #abrir un archivo para escribir
archivo.write("hola papito como estas") #el texto agregado
archivo.close() #se cierra el archivo

archivo = open("pilio.txt","a") #se agrega otro texto si ya existe otroç
archvo.close()
archivo = open("pilio.txt","r")
for linea in open("hola.txt"):
    print(linea)