"""Ejercisio 3 de la tarea 1 de programacion / fecha: 03/26/2025"""

lista_cadenas = ["Esta es otra " , " lista de cadenas" , " para el ejercicio 3" , " de la tarea 1" , " de programacion"]

# esta funcion recibe una lista de cadenas y devuelve una lista con las cadenas en minusculas y mayusculas segun si son par o no
def Min_o_Mayus(lista):
    for i in range(len(lista)):
        if i % 2 == 0:
            lista[i] = lista[i].upper()
        else:
            lista[i] = lista[i].lower()
    return lista

print(Min_o_Mayus(lista_cadenas))