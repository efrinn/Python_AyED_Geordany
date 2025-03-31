lista_cadenas = [" Hola profesor , como le va " , " A mi , me esta iendo bien "," esta cadena , rompe la 4ta pared "]
print(lista_cadenas)

lista_modificada = [cadena.split(",") for cadena in lista_cadenas]
print(lista_modificada)