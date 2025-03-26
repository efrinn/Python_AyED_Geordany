a = 3
b = ":-D"
c = 3.132
d = True
print(type(a))
print(type(b))
print(type(c))
print(type(d))

suma = 2+3
print(suma)

if suma == 5:
    print("Hola petes")
else: print("adios petes")

nombre = input("Ingresa tu nombre: ")

edad = int(input("Ingresa tu edad: "))

if edad >=0 and edad <=12:
    print("eres niño")
elif edad >=13 and edad <=17:
    print("Eres adolecente")
elif edad >=18 and edad <=29:
    print("Eres Joven")
elif edad >=30 and edad <=59:
    print("Eres adulto")
elif edad < 60:
    print("Eres adulto mayor")
else:
    print("que #@/*$ pusiste , esa edad no es validad") #este es un if anidado