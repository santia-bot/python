suma = "suma"
valor_1 = "valor_1"
valor_2 = "valor_2"
resta = "resta"
division = "division"
multiplicacion = "multiplicacion"

print("hola usuario, ¿que quieres realizar el dia de hoy?: suma, resta, division, multiplicacion\n")


def calculadora():
    valor_1 = input("ingrese el primer valor:\n")
    valor_2 = input("ingrese el segundo valor:\n")
    op = input("ingres la operacion que quieras realizar:\n")
    valor_1 = int(valor_1)
    valor_2 = int(valor_2)
    operaciones(valor_1, valor_2, op)


def operaciones(valor_1, valor_2, op):
    if op == suma:
        resultado = (valor_1 + valor_2)
        print(resultado)
    elif op == resta:
        resultado = (valor_1 - valor_2)
        print(resultado)
    elif op == division:
        resultado = (valor_1 / valor_2)
        print(resultado)
    elif op == multiplicacion:
        resultado = (valor_1 * valor_2)
        print(resultado)
    else:
        print("solo se puede poner: suma, resta, division, multiplicacion")


calculadora()
