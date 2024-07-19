import random
import csv
import cowsay
import math

"""
pip install cowsay
recomiendo la extension "rainbow csv", para una mejor lectura
"""

trabajadores = ["juan perez", 
                "maria garcia", 
                "carlos lopez", 
                "ana martinez", 
                "pedro rodriguez", 
                "laura hernandez", 
                "miguel sanchez", 
                "isabel gomez", 
                "francisco diaz", 
                "elena fernandez"]

def asignar_sueldos_aleatorios(trabajadores):
    sueldos = {}
    for trabajador in trabajadores:
        sueldos[trabajador] = random.randint(300000, 2500000)
    print("sueldos asignados aleatoriamente:")
    for trabajador in sueldos:
        print(trabajador, ":", sueldos[trabajador])
    return sueldos

def clasificar_sueldos(sueldos):
    clasificacion = {"abajo de 800000": [], "entre 800000 y 2000000": [], "arriba de 2000000": []}
    
    for trabajador in sueldos:
        sueldo = sueldos[trabajador]
        if sueldo < 800000:
            clasificacion["abajo de 800000"].append((trabajador, sueldo))
        elif sueldo < 2000000:
            clasificacion["entre 800000 y 2000000"].append((trabajador, sueldo))
        else:
            clasificacion["arriba de 2000000"].append((trabajador, sueldo))
    
    print("clasificacion de sueldos:")
    for categoria in clasificacion:
        print(categoria, ":", len(clasificacion[categoria]))
        for empleado in clasificacion[categoria]:
            print(empleado[0],":", empleado[1])
        print()
    
    total_sueldos = sum(sueldos.values())
    print("total sueldos:", total_sueldos)

def ver_estadisticas(sueldos):
    sueldo_mas_alto = max(sueldos.values())
    print("sueldo mas alto:", sueldo_mas_alto)

    sueldo_mas_bajo = min(sueldos.values())
    print("sueldo mas bajo:", sueldo_mas_bajo)

    total_sueldos = sum(sueldos.values())
    promedio_sueldos = total_sueldos / len(sueldos)
    print("promedio de sueldos:", promedio_sueldos)

    producto_sueldos = 1
    for sueldo in sueldos.values():
        producto_sueldos *= sueldo
    media_geometrica = math.pow(producto_sueldos, 1.0 / len(sueldos))
    print("media geometrica:", round(media_geometrica, 2)) 

def reporte_sueldos(sueldos):
    with open('sueldos.csv', 'w', newline='') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv, delimiter=";")
        escritor_csv.writerow(['nombre empleado', 'sueldo base', 'descuento salud', 'descuento afp', 'sueldo liquido'])
        
        for trabajador in sueldos:
            sueldo = sueldos[trabajador]
            salud = sueldo * 0.07
            afp = sueldo * 0.12
            sueldo_liquido = sueldo - salud - afp
            escritor_csv.writerow([trabajador, sueldo, salud, afp, sueldo_liquido])

def menu():
    sueldos = {}

    while True:
        print("1. asignar sueldos aleatorios \n2. clasificar sueldos \n3. ver estadisticas \n4. reporte de sueldos (exportar a csv) \n5. salir del programa")

        opcion = input("-ingrese una opcion: ")

        if opcion == "1":
            sueldos = asignar_sueldos_aleatorios(trabajadores)
        elif opcion == "2":
            if sueldos: 
                clasificar_sueldos(sueldos)
            else:
                print("debe escoger la primera opcion primero, para asi asignarles sueldos")
        elif opcion == "3":
            if sueldos: 
                ver_estadisticas(sueldos)
            else:
                print("debe escoger la primera opcion primero, para asi asignarles sueldos")
        elif opcion == "4":
            if sueldos: 
                reporte_sueldos(sueldos)
            else:
                print("debe escoger la primera opcion primero, para asi asignarles sueldos")
        elif opcion == "5":
            print("saliendo del programa... \ndesarrollado por benjamin salas \nrut 21679600-4")
            cowsay.daemon("see u space cowboy..")
            break
        else:
            print("opcion invalida. intente nuevamente.")

menu()
