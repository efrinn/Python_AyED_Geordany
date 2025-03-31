"""Ejercisio 4 de la tarea 1 de programacion / fecha: 03/29/2025"""

lista_cadenas = ["Cadena", "String" , "Entero" , "Int", "booleano", "bool", "float", "flotantes" , "Cadena", "String" , "Entero" , "Int", "booleano", "bool", "float", "flotantes"]
print(lista_cadenas)

subcadena = input("Ingrese una subcadena de las 8 en la lista: ")

# esta funcion recibe una lista de cadenas y una subcadena y devuelve una lista con True o False segun si la subcadena se encuentra en la lista de cadenas

def subcadena_encontrar(lista_cadenas, subcadena):
    resultados = []
    for cadena in lista_cadenas:
        resultados.append(subcadena in cadena)
    return resultados

print(subcadena_encontrar(lista_cadenas, subcadena))