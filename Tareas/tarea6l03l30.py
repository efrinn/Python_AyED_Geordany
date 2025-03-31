"""Ejercisio 6 de la tarea 1 de programacion / fecha: 03/30/2025"""

lista_cadenas = [" Hola profesor " , " A mi me esta iendo bien "," esta cadena es aburrida "]

print(lista_cadenas)

# esta funcion recibe una lista de cadenas y devuelve una lista con las cadenas sin espacios al principio y al final
lista_modificada = [cadena.strip() for cadena in lista_cadenas]
print(lista_modificada)