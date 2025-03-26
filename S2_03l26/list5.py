#leer un parrafo y contar cuantas oraciones tiene

parrafo_input = input("Escribe un parrafo:  ")


#borrar los espacios al inicio y al final

if parrafo_input[-1] == ".":
    parrafo = parrafo_input[0:len(parrafo_input)-1].strip()
else: parrafo = parrafo_input

oraciones = parrafo.split(".")
print(parrafo)

print(f"El parrafo tiene {len(oraciones)} oraciones")