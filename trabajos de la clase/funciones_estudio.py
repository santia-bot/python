"""def factorial(numero):
    factorial = 1
    while numero > 0:
        factorial = factorial * numero
        numero -=1
    #print(factorial)
    return factorial

numero = int(input("ingrese un numero:"))
factorial(numero)
"""
def suma(valor_uno,valor_dos,valor_tres):
    return valor_uno + valor_dos + valor_tres
def division(valor_uno,valor_dos):
    return valor_uno/valor_dos
def multiplicacion(valor_uno,valor_dos):
    return valor_uno * valor_dos
def multiples_valores():
    return 'String', "1", True, 25.6

resultado = suma (10,20,30)
print(resultado)

resultado = division(100,10)
print(resultado)

resultado = multiplicacion(6,10)
print(resultado)

resultado =multiples_valores()
print(resultado)