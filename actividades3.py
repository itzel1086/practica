print("\t Lista de tareas por materia.")
tareas = dict()
 
datonuevo= str(input("Registre nueva tarea \n\t"))
registronuevo=str(input("Materia\n\t"))
tareas.setdefault(registronuevo, datonuevo)
for registro_nuevo, datonuevo in tareas.items():#items devielve el conjunto de valores
    print("\n\t Las nuevas tareas son: \n")
    print("{0}-->{1}". format(registro_nuevo, datonuevo ))# para cada iteración imprimir clave=valor
