
actividad_Alex = dict ()
actividad = 0
while actividad <=4:
    actividad = int(input("\n Hola, Este es el menú de actividades de Alex \n \n\t Actividades\n\n \t 1: Actividades en la casa\n \t 2: Actividades en la escuela\n \t 3: Actividades extras\n \t 4: Actividades de Alex \n"))
    if actividad ==1:
        print("Las Actividades en la casa son:\n \t A) Barrer\n \t B) Escombrar\n \t C) Tender la cama\n")
    elif actividad ==2:
        print("Las actividades enla escuela son:\n \t1: Trabajar\n \t 2: Jugar")
    elif actividad==3:
        n_activ= input("Por favor ingrese numero de actividad\n")
        activ = input("Por favor ingrese la actividad\n")
        print ("\tEl numero de actividad es ", n_activ, " \ty la Actividad es: ", activ)
    elif actividad ==4: 
        
        print("\n\t Se esta agregando nueva actividad para Alex:\n")
        print("\t ==> Agregar nueva actividad<==")
        nuevo_clave_actividad= input("Registre nuevo número de actividad\n")
        nueva_avtividad=input("Nueva actividad\n")
        actividad_Alex.setdefault(nuevo_clave_actividad,nueva_avtividad )
        print ("\n LISTA DE ACTIVIDADES PARA ALEX")
        for numero_actividad, nom_actividad in  actividad_Alex.items():
            print("{0}==>{1}".format(numero_actividad,nom_actividad))
    else: 
        print("\n Lo sentimos, estamos actualizando más opciones")
