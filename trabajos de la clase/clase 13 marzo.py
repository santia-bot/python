print("clase de lista")
"""
nombre
telefono
correo
sintaxis: lista = []
sintanxis: tupla = ()
"""

#lista = ["guadalupe", 32, "55523456", "diazsantix@gmail.com", False ]
#print(lista)
#slicing // buscar
lista2 = ["python", "java", "c++", "PHP", "MySQL", "C#"]

print("llamar un elemento:", lista2[0])
print("numeros de elementos en lista", len(lista2))

sub = lista2[1::3]
#sub = lista2[:: -2] /brincos al reves
#sub = lista2[:: -1] #alreves
#sub = lista2[1::3] #brincos
#sub = lista2[::2]# 2 en 2 /buscar mas
#lista[:-1] #se imprimer el ultimo
print("\n sublista:", sub,)
lista2.append("POO")
print(lista)

"""
tuplas
"""
tupla = ("guadalupe", "antonio", "pilio", 32, "30076375609")
print("llamar un elemento:", tupla[0])
print("numeros de elementos",len(tupla))

print( "\n subtupla:",subt )
#print(tupla[-2])
#tupla.append("juan") no se puede agregar