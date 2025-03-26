nombre = "Haydee"
apellido = "Valverde"

nombre_completo = nombre + " " + apellido
print(nombre_completo)

nombre_completo2 = f"{nombre} {apellido}"
print(nombre_completo2)

nombre_completo3 = " ".join([nombre, apellido])

lista = []
lista.append(nombre)
lista.append(apellido)
nombre_completo4 = " ".join(lista)
print(nombre_completo4)