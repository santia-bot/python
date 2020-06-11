dias_semana ={
	1:'LUN',
	2:'MAR',
	3:'MIE',
	4:'JUE',
	5:'VIE',
	6:'SAB',
	7:'DOM',
}

for llave in dias_semana:
	print(llave)

for valor in dias_semana.values():
	print(valor)

for llave,valor in dias_semana.items():
	print(llave, valor)
dic_prueba = {
'grupo1':{1:'LUN',2:'MAR'},
'grupo2':{3:'MIE',4:'JUE'},
'grupo3':{5:'VIE',6:'SAB',7:'DOM'}
}

print(dic_prueba)
"""
diccionario = { " a " : 55, "b" : "antonio", 5 : "geronimo" }
la claves deben ser inmutables
si existen dos llaves iguales se reemplaza
diccionario = {"a" = 55, "a" : "f"}
la salida sera f
diccionario["c"] = "nuevo_string"
asi se agregan datos a los diccionarios
modificar un valor
dicconario["a"] = false
si la llave se encuentra actualiza si no crea
obtener los datos de un diccionario
valor = diccionario ["a"]
si el elemneto no se encuentra regrese un mensaje
valor = diccionario.get("z" , "false")
eliminar valores
del dicconario [5]
un objeto iterable regresa las llaves
llaves = diccionarioi.keys()
para volverlo una lista
llaves = list(diccionario.keys())
obtener los valores de un diccionario
valores = list(diccionario.values())
tambien se  puede hacer con tuplas
agregar otro diccionario
diccionario_dos ) {"z":23,'w':88}
diccionario.update(diccionario_dos)