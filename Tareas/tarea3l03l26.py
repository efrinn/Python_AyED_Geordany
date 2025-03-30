"""Ejercisio 3 de la tarea 1 de programacion / fecha: 03/26/2025"""

lista_cadenas = ["Esta es otra " , " lista de cadenas" , " para el ejercicio 3" , " de la tarea 1" , " de programacion"]

def Min_o_Mayus(lista):
    for i in range(len(lista)):
        if i % 2 == 0:
            lista[i] = lista[i].upper()
        else:
            lista[i] = lista[i].lower()
    return lista
print(Min_o_Mayus(lista_cadenas))