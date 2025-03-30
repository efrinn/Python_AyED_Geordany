lista_cadenas = ["Cadena", "String" , "Entero" , "Int", "booleano", "bool", "float", "flotantes" , "Cadena", "String" , "Entero" , "Int", "booleano", "bool", "float", "flotantes"]
print(lista_cadenas)

subcadena = input("Ingrese una subcadena de las 8 en la lista: ")


def subcadena_encontrar(lista_cadenas, subcadena):
    resultados = []
    for cadena in lista_cadenas:
        resultados.append(subcadena in cadena)
    return resultados

print(subcadena_encontrar(lista_cadenas, subcadena))