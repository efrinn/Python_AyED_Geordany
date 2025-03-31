"""Ejercisio 9 de la tarea 1 de programacion / fecha: 03/30/2025"""

lista_cadenas = ["Hola" , "Hello" , " " , "Goodbye", " ", "Bestia" , "Perro" , " "]
print(lista_cadenas)

# esta funcion recibe una lista de cadenas y devuelve una lista con las cadenas sin subcadenas vacias
lista_cadenas = [cadena for cadena in lista_cadenas if cadena.strip() ]
print("Lista sin subcadenas vacias: ",lista_cadenas)