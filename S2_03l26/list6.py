# Description: Ejemplo de uso de metodos de cadenas de texto

texto = "La uaM eS la uniVersidad mAs mierda de todas"
print(texto)

texto_Mayus = texto.upper()
print(texto_Mayus)

texto_Minus = texto.lower()
print(texto_Minus)

#primera letra en mayusculas

nombre = "geordany"
nombre = nombre.capitalize()
print(nombre)

#Remplazar texto 
texto2 = "Hola C# world"

texto2 = texto2.replace("C#", "python")
print(texto2)

#Eliminar espacios en blanco 
texto3 = "    Hola mundo    "
print(texto3)
print(texto3.strip())
print(texto3)

#Formato de numeros

numero = 1500
print(numero)
numero = "{:,.2f}".format(numero)
print(numero)