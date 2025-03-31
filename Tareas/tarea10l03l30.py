"""Ejercisio 9 de la tarea 1 de programacion / fecha: 03/30/2025"""

lista_cadenas = ["Hola" , "Hello" , "Adios" , "Goodbye", "Beast", "Bestia" , "Perro" , "Dog"]
print(lista_cadenas)

caracter_a_buscar = input("Ingrese el caracter a buscar: ")

def contar_caracter(lista_cadenas, caracter_a_buscar):
    resultados = []
    for cadena in lista_cadenas:
        resultados.append(cadena.count(caracter_a_buscar)) # cuenta el numero de veces que aparece el caracter en la cadena y lo anade a resultados
    return resultados

print("Numero de veces que el caracter aparece en cada cadena: ",contar_caracter(lista_cadenas, caracter_a_buscar))