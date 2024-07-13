import random as r
import csv

Trabajadores = [
    {"nombre": 'Juan Pérez'},
    {"nombre": 'María García'},
    {"nombre": 'Carlos López'},
    {"nombre": 'Ana Martínez'},
    {"nombre": 'Pedro Rodríguez'},
    {"nombre": 'Laura Hernández'},
    {"nombre": 'Miguel Sánchez'},
    {"nombre": 'Isabel Gómez'},
    {"nombre": 'Francisco Díaz'},
    {"nombre": 'Elena Fernández'}]
Sueldos = []
total = 0
def sueldo_aletorio():
    global Sueldos
    i = 0
    while i < 10:
        Sueldos.append(r.randint(350000, 2500000))
        i = i + 1 
    print("Saldos generados")
    
def clasificar_Sueldos():
        print("sueldos menores a $800.000 total:", len([s for s in Sueldos if s < 800000]))
        for trabajador, sueldo in zip(Trabajadores, Sueldos):
            if sueldo < 800000:
                print(f"Nombre empleado: {trabajador['nombre']}  Sueldo: ${sueldo}")
        print("\sueldos entre $800.000 y $2.000.000 total:", len([s for s in Sueldos if 800000 <= s <= 2000000]))
        for trabajador, sueldo in zip(Trabajadores, Sueldos):
            if 800000 <= sueldo <= 2000000:
                print(f"Nombre empleado: {trabajador['nombre']}  Sueldo: ${sueldo}")
        print("\sueldos mayor a $2.000.000 total:", len([s for s in Sueldos if s > 2000000]))
        for trabajador, sueldo in zip(Trabajadores, Sueldos):
            if sueldo > 2000000:
                print(f"Nombre empleado: {trabajador['nombre']}  Sueldo: ${sueldo}")
        
        print("\n total sueldos:", sum(Sueldos))
        
def ver_estadisticas():
    global Sueldos
    print(f"Sueldo mas bajo: {min((Sueldos))}")
    print(f"Sueldo mas alto: {max(Sueldos)}")
    print(f"promedio de sueldos: {sum(Sueldos) / len(Sueldos)}")

def reporte_sueldo():
        with open('reporteSueldos.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Nombre empleado", "Sueldo Base", "Descuento Salud", "Descuento AFP", "Sueldo Líquido"])
            for trabajador, sueldo in zip(Trabajadores, Sueldos):
                descuento_salud = sueldo * 0.07
                descuento_afp = sueldo * 0.12
                sueldo_liquido = sueldo - descuento_salud - descuento_afp
                writer.writerow([trabajador["nombre"], sueldo, descuento_salud, descuento_afp, sueldo_liquido])
                print(f"Nombre empleado: {trabajador['nombre']} Sueldo Base: ${sueldo} Descuento Salud: ${descuento_salud:.2f} Descuento AFP: ${descuento_afp:.2f} Sueldo Líquido: ${sueldo_liquido:.2f}")

def menu():
    while True:
        print(" 1. Asignar sueldos aleatorios \n 2. Clasificar sueldos \n 3. Ver estadísticas. \n 4. Reporte de sueldos \n 5. Salir del programa")
        op = int(input("Eliga una opción: "))
        if op == 1:
            sueldo_aletorio()
        elif op == 2:
            clasificar_Sueldos()
        elif op == 3:
            ver_estadisticas()
        elif op == 4:
            reporte_sueldo()
        elif op == 5:
            print("Finalizando programa...")
            print("Desarrollado por: Carlos Alejandro Torrejon Villanueva")
            print("RUT: 25669882-K")
            break

        else:
            print("Opcion incorrecta, Vuelva a ingresar una opcion")   
            
menu()