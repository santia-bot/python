#primer taller de diccionarios
"""
Crea un diccionario donde la clave sea el nombre del usuario y el valor sea 
el teléfono (no es necesario validar). Tendrás que ir pidiendo contactos 
hasta el usuario diga que no quiere insertar mas. No se podrán meter 
nombres repetidos.
"""

diccionario = {}
# bandera indicadora
encuesta_activa = True

while encuesta_activa:
    nombre = input("\n ingreser el nombre del usuario:").capitalize()
    if nombre in diccionario:
        print("el usuario",nombre,"ya se encuentra en el diccionario, para diferenciar pon el apellido")
    telefono = input("\n ingrese en telefono del usuario:")
#almacenar la respuesta en el diccionario
    diccionario[nombre] = telefono
    preguntar = input("¿quiertes ingresar a alguien mas? (Si/No)").capitalize() 
    if preguntar == "No":
        encuesta_activa = False
        print("\n este es el diccionario creado:",diccionario)
