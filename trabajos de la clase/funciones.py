
def sumar():
    suma = 5 + 3
    print("suma:",suma)

def restar(num1,num2 = 0): # cuando es igual a 0 ayuda cuando no mandan un valor
    resta = num1 - num2
    num1 = 20
    print("resta:",resta)
    print("num1 en funcion:", num1)

def multiplicar(n1,n2): # funcion que recibe parametrosa y regresa un valor
    multi =n1*n2 #se pueden agregar los valores y se mostrara el resultado
    return multi

#main
sumar()  # llamar una funcion
num1 =10
num2 = 5
restar(num1,num2) #llamar funcion con parametros
#restar(num1)
#print("num1 en main", num1)
multip = multiplicar(num1,num2) #llamar un funcion con parametros y recibir parametro
print("multiplicacion:",multip)
#return sirve para el resultado de la funcion se pueda utilizar luego