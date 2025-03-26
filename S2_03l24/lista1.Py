#Almacenar 10 numeros enteros

list_Int = list()

def num_unpair():
    for i in range (10):
       num = int(input(f"{i+1} de 10 - Ingresa un numero: "))
       if num % 2 != 0 and num > 18:
        list_Int.append(num)
       else:
        print("(⸝⸝⸝O﹏O⸝⸝⸝) Parece que el numero que has ingresado es menor a 18 o es impar y no sera anadido a la lista")

num_unpair()
print(list_Int)
