#Ejercicios de actividades de leo

actividad = 0
while actividad <=3:
    actividad = int(input("\n Hola, Este es el menú de actividades de Alex \n \n\t Actividades\n\n \t 1: Actividades en la casa\n \t 2: Actividades en la escuela\n \t 3: Actividades extras\n "))
    if actividad ==1:
        print("Las Actividades en la casa son:\n \t A) Barrer\n \t B) Escombrar\n \t C) Tender la cama\n")
    elif actividad ==2:
        print("Las actividades enla escuela son:\n \t1: Trabajar\n \t 2: Jugar")
    elif actividad==3:
        n_activ= input("Por favor ingrese numero de actividad\n")
        activ = input("Por favor ingrese la actividad\n")
        print ("\tEl numero de actividad es ", n_activ, " \ty la Actividad es: ", activ)
    else: 
        print("\n Lo sentimos, estamos actualizando más opciones")
