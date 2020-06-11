fecha = int(input("escriba 8 numero: \n"))

a = fecha % 10000
a = fecha // 10000
m= fecha % 100
m = fecha // 100
fecha = fecha // 100
d = fecha % 100



print("/", d, "/", m, "/", a, "/")
	