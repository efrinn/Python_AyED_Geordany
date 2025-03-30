"""Ejercisio 1 de la tarea 1 de programacion / fecha: 03/26/2025"""

lista_cadenas = ["Este es un " ,"texto de prueba ", "para el ejercicio 1 ", "de la tarea 1", " de programacion"]

lista_Cadena_entera = f"{lista_cadenas[0]} {lista_cadenas[1]}{lista_cadenas[2]}{lista_cadenas[3]}{lista_cadenas[4]}"

print(lista_Cadena_entera)

#metodo menos tedioso

cadena_entera2 = " ".join(lista_cadenas)