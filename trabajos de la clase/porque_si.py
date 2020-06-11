print("""
autobus: precio del boleto 100
barco: precio del boleto 150
tren: precio del boleto 90
avion: precio del boleto 200
"""  )
print("""
los descuentosson los siguientes:
niño: descuento del 50%
adulto: no hay descuento
adulto mayor: descuento del 50%
discapacitado: descuento del 50%
""")

metodo = input("¿Que forma de viajar quieres elegir?")
metodo = int(metodo)

dinero = input("cuantos boletos quieres comprar" )
dinero = int(dinero)

pasajero = input("""
si el pasajero es: 
niño: oprima 1
adulto: oprima 2
adulto mayor: oprima 3
discapacitado: oprima 4 
""")
pasajero= int(pasajero)
