"""Lupita Moran
Ejercicio 1 - Realizar un programa en el cual pida tres números al usuario, con el uso de funciones, 
uno debe indicar si es par o no y la otra función deberá regresar la multiplicación del valor por 10. 
Todo esto se debe imprimir en pantalla. (Opcional pueden usar While)
"""

def par(num1,num2=0,num3=0):
    if num1 % 2 == 0:
        print("el numero",num1,"es par")
    else:
        print("el numero",num1,"es impar")
def multiplicar(num1=0,num2=0,num3=0):
    multip = num1 * 10
    return multip
#main
num1 =int(input("ingrese un numero:"))
num2 =int(input("ingrese un numero:"))
num3 =int(input("ingrese un numero:"))

par(num1)
par(num2)
par(num3)
multiplicar(num1)
multiplicar(num2)
multiplicar(num3)
multip = multiplicar(num1)
multip = multiplicar(num2)
multip = multiplicar(num3)

print("el resultrado de la multiplicacion del numero",num1, "es:",multip)
print("el resultrado de la multiplicacion del numero",num2, "es:",multip)
print("el resultrado de la multiplicacion del numero",num3, "es:",multip)
