
"""
escribe un programa, usando estructuras de control selectivas (if, elif, else), que
pida ingresar cuatro numeros no consecutivos y debe imprimirlos en ordenn ascendente,
algunos ejemplos:
ingrese numero: 12
ingrese numero: 5
ingrese numero: 9
ingrese numero: 11
ordenado: 5 9 11 12
"""
print("Hola, bienvenido a mi programa")
num1 = int(input("ingrese el numero 1: \n "))
num2 = int(input("ingrese el numero 2: \n "))
num3 = int(input("ingrese el numero 3: \n "))
num4 = int(input("ingrese el numero 4: \n "))

if num1 < num2 and num1 < num3 and num1 < num3 and num1 < num4 and num2 < num4 and num2 < num3 and num3 < num4:
    print(num1, num2, num3, num4)
else:
    print("usted ingreso un dato ivalido")

