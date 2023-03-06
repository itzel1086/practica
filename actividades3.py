print("\t Lista de tareas por materia.")
tareas = dict()
fecha = input("Por favor digite una fecha actual")
más_tareas ='S'
#Pedir datos para el diccionario 
   
while más_tareas.upper() !='N':
        
        datonuevo=(input("Registre nueva tarea \n\t"))
        registronuevo = input("Materia\n\t")
        más_tareas=input("\t ¿Desea agregar nueva actividad?  R= S/N")
        tareas.setdefault(datonuevo, registronuevo)
print("\n\t Las nuevas tareas son: \n")

      
for datonuevo, registronuevo in  tareas.items():
    print("{0}==>{1}".format(datonuevo,registronuevo))
print("\n \t A la Fecha", fecha)