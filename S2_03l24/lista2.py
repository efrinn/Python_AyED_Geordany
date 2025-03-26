#Agregar los nombres de x cantidad de estudiantes 

list_students = list()

def add_student():
    student= input("Ingresa el nombre del estudiante: ")
    list_students.append(student)

def show_students():
    print("Lista de estudiantes: ")
    for student in list_students:
        print(student)

while True:
    add_student()
    show_students()
    if input("Desea agregar otro estudiante? :D? (s/n): ").lower() !="s":
        break

print("gracias por usar el programa")