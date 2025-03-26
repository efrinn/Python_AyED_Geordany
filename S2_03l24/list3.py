# tipo de estructura de dato
# 1. Pilas

stack = []

def push (val):
    if len(stack) < 5:
        stack.append(val)
    else:
        print ("Stack Overflow")

def pop():
    if len(stack) > 0:
        return stack.pop
    else:
        print("Stack Ondeflow")

def menu():
    print("1. Push")
    print("2. Pop")
    print("3. Salir")
    return int(input("Elije una opcion: "))

while True:
    option = menu()
    if option ==1:
        push (int(input("Ingresa un numero")))
    elif option == 2:
        print(pop())
    elif option == 3:
        break
    else:
         print ("Opcion invalida")

print("Gracias por usar el programa")