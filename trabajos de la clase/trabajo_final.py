
print("""
Tipo de café                            Chico Grande
1 Espresso / Expresso / Exprés o solo.   15     25
2 Capuchino.                             20     35
3 Americano.                             18     33
4 Caffe Latte/Café con leche.            22     38
5 Café au Lait.                          25     45
6 Café Moca (Mokaccino)                  24     43
7 Caramelo Macchiato.                    27     48
"""
)
#diccionarios de los tiposde cafes y sus respectivos precios
cafe_chico = {"Expresso": 15,"Capuchino": 20,"Americano": 18,"Cafe con leche": 22,"Cafe au lait": 25,"Cafe moca":24,"Caramelo macchiato": 27}
cafe_grande ={"Expresso": 25,"Capuchino": 35,"Americano": 33,"Cafe con leche": 38,"Cafe au lait": 45,"Cafe moca": 43,"Caramelo macchiato": 48}


def descuentos_total(total_pagar,tipo_cafe,tamaño_cafe):
    if total_pagar < 40:
        ingrese_nombre = input("***usted va a participar en un concuerso***\n ingrese su nombre:")
        longitud_nombre = len(ingrese_nombre)
        print(longitud_nombre)
        if longitud_nombre % 2 == 0:
            total_pagar = total_a_pagar * 0.10
            print("usted ha ganado un descuendo del 10%, su valor a pagar es {}".fomart(total_a_pagar))
        else:
            total_a_pagar = total_a_pagar * 0.05
            print("usted ha ganado un descuento del 5%, su valor a  pagar es {}".format(total_a_pagar))

def compra_total(tipo_cafe,tamaño_cafe,pedido_cantidad):
    total_pagar = tipo_cafe + tipo_cafe
    return total_pagar
    descuentos_total(total_pagar,tipo_cafe,tamaño_cafe)

def descuento_tamaño(tipo_cafe,tamaño_cafe):

    if tamaño_cafe == "chico":
        tipo_cafe = cafe_chico.get(tipo_cafe)
        tipo_cafe = tipo_cafe - tipo_cafe * 0.05
        print("cafe con descuento",tipo_cafe) 
    elif tamaño_cafe == "grande":
        tipo_cafe = cafe_grande.get(tipo_cafe)
        tipo_cafe = tipo_cafe - tipo_cafe * 0.10
        print("cafe con descuento",tipo_cafe)
    else:
        print("dato invalido")
    compra_total(tipo_cafe,tamaño_cafe,pedido_cantidad)

def main(tamaño_cafe,tipo_cafe):

    if tamaño_cafe == "grande":
        print("cafe sin el descuento",cafe_grande.get(tipo_cafe))
    elif tamaño_cafe == "chico":
        print("cafe sin el descuento",cafe_chico.get(tipo_cafe)) 
    else:
        print("Dato invalido")
    descuento_tamaño(tipo_cafe,tamaño_cafe)

#se piden los cuantos cafes quiere comprar
pedido_cantidad = int(input("¿Cuantos cafés desea pedir?: \n"))
for pedido in range(pedido_cantidad):
    tipo_cafe = input("que tipo de cafe desea llevar: \n ").capitalize()
    tamaño_cafe = input("que tamaño de cafe desea llevar: \n")
    main(tipo_cafe=tipo_cafe,tamaño_cafe=tamaño_cafe)

