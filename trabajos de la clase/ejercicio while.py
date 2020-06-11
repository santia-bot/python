print("*actividad while*")
numero = int(input("ingrese los numero que quiera sumar: \n "))
#variable = numero
total = 0
while numero >= 1:
	valor = int(input("ingrese un valor: \n "))
	total += valor
	numero = numero - 1
	print("el total es:", total)