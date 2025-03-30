lista_cadenas = ["Hola" , "Hello" , "Adios" , "Goodbye", "Beast", "Bestia" , "Perro" , "Dog"]
print(lista_cadenas)

#validar que solo sea un caracter a remplazar/ingresar

while True:
    caracter_a_remplazar = input("Ingrese el caracter a reemplazar/cambiar: ")
    if len(caracter_a_remplazar) == 1:
        break
    else:
        print("Porfavor ingrese solo un caracter :D")


while True:
    caracter_remplazo = input("Ingrese el caracter de reemplazo/sustituyente: ")
    if len(caracter_remplazo) == 1:
        break
    else:
        print("Porfavor ingrese solo un caracter :D")

#aqui se remplazara el caracter en cada cadena de la lista

lista_modificada = [cadena.replace(caracter_a_remplazar, caracter_remplazo) for cadena in lista_cadenas]
print(lista_modificada)