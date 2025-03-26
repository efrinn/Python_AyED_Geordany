"""lista de cadena"""
lista = ["Hola","Mundo","Python","programacion","C#","Java","PHP","SQL"]

print(lista)

print(lista[0]) #cuando son numeros positivos a la hora de recorrer la lista se imprimira de izquierda a derecha
print(lista[1])

print(lista[-2])
print(lista[-3]) # cuando son positivos de derecha a izquierda
print(lista[2: -5])

lista.append("Ruby")
print(lista)

#insertar en posicion especifica

lista.insert(2,"JavaScript")
print(lista)