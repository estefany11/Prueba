#PUNTO 1
print("Este programa lee dos números y los imprime de manera ascendente.")
a=float(input("\nNúmero A: "))
b=float(input("Número B: "))

if a<b:
    print(a,b)
else:
    print(b,a)


#PUNTO 4
print("\nEste programa determina el total a pagar por una llamada")
llamada = int(input("\nNúmero de minutos: "))
valorllamada= 200

if llamada <= 3: 
    print(f"\nEl valor es: {valorllamada} pesos")

else:
    adicional = llamada-3 
    valorllamada=valorllamada + (adicional*100)
    print(f"\nEl valor es: {valorllamada} pesos")


#PUNTO 5
print("\nEste programa ayuda a monitorear el total de conejos en una granja.")

N=int(input("\nNúmero total de conejos: "))
C1=int(input("Conejos blancos: "))
C2=int(input("Conejos negros: "))

if C1+C2 != N:
    print(f"\nError: El número total de conejos no coincide con la cantidad de conejos blancos y negros totales. Hay {N} conejos en total y {C1+C2} de blancos más negros.")
    
else: 
    X=int(input("\nConejos negros vendidos: "))
    Y=int(input("Conejos blancos vendidos: "))
    
    if X > C2:
        print("Error: El número de conejos negros vendidos es mayor que el total de conejos negros disponibles")
        
    elif Y > C1:
        print("Error: El número de conejos blancos vendidos es mayor que el total de conejos blancos disponibles")
        
    elif X+Y > N:
        print("Error: El número de conejos vendidos es mayor que el total de conejos disponibles")
    else:

        ConejosVendidos = print(f"\nEl total de conejos vendidos es: {X+Y}")

        P1=float(input("\nPrecio de los conejos blancos: "))
        P2=float(input("Precio de los conejos negros: "))

        MontoVenta = print(f"\nEl monto total de la venta fue de {P1*Y+P2*X} pesos")

        if X>Y:
            print("\nSe vendieron más conejos negros.")
        else:
            print("\nSe vendieron más conejos blancos.")


#PUNTO 6
print("\nEste programa calcula la nota final de un estudiante.")

    #Nota PREVIOS
np1 = float(input("\nNota previo 1: "))
np2 = float(input("Nota previo 2: "))
np3 = float(input("Nota previo 3: "))

if np1<1 or np1>5:
    print("\nError: Nota de previo 1 no válida, debe ser entre 1 y 5")

elif np2<1 or np2>5:
    print("\nError: Nota de previo 2 no válida, debe ser entre 1 y 5")

elif np3<1 or np3>5:
    print("\nError: Nota de previo 3 no válida, debe ser entre 1 y 5")
  
else: 
    NotaPrevios = ((np1+np2+np3)/3)*0.6
    print(f"\nLa nota de previos es: {NotaPrevios}")

        #Nota TRABAJOS
    nt1 = float(input("\nNota trabajo 1: "))
    nt2 = float(input("Nota trabajo 2: "))

    if nt1<1 or nt1>5:
        print("\nError: Nota de trabajo 1 no válida, debe ser entre 1 y 5")

    elif nt2<1 or nt2>5:
        print("\nError: Nota de trabajo 2 no válida, debe ser entre 1 y 5")
    else: 
        NotaTrabajos= ((nt1+nt2)/2)*0.4
        print(f"\nLa nota de trabajos es: {NotaTrabajos}")
        
        print(f"\nLa NOTA FINAL será: {NotaPrevios+NotaTrabajos}")


#PUNTO 7
print("\nCálcula el descuento de un artículo.")
NombreArt=input("\nNombre del artículo: ")
Clave=int(input("Clave: "))

if Clave == 1 or Clave == 2:
    Precio=float(input("Precio:"))
    Cantidad=int(input("Cantidad: "))

    if Clave == 1:
        PrecioFinal = (Precio - (Precio*0.1))*Cantidad
        print(f"\nEl artículo {NombreArt} tiene un precio inicial de ${Precio} por unidad, al llevar {Cantidad} unidad(es), el precio final es: ${PrecioFinal}.\nSu ahorro fue de ${Precio*Cantidad-PrecioFinal}.")
    else:
        PrecioFinal = (Precio - (Precio*0.2))*Cantidad
        print(f"\nEl artículo {NombreArt} tiene un precio inicial de ${Precio} por unidad, al llevar {Cantidad} unidad(es), el precio final es: ${PrecioFinal}.\nSu ahorro fue de ${Precio*Cantidad-PrecioFinal}.")
else:
    print("\nError: Clave inválida.") 


#PUNTO 8
print("\nEste programa calcula el presupuesto para diferentes áreas de la medicina.")

PresupuestoAnual = float(input("\nPresupuesto Anual: "))
PorPsiquiatria = float(input("\nPorcentaje asignado a Psiquiatría: "))
PorPediatria = float(input("Porcentaje asignado a Pediatría: "))
PorTraumatologia = float(input("Porcentaje asignado a Traumatología: "))

if PorPsiquiatria+PorPediatria+PorTraumatologia != 100:
    print("La suma de los porcentajes no corresponde al 100%")

else:
    PrePsiquiatria= PresupuestoAnual*(PorPsiquiatria/100)
    PrePediatria = PresupuestoAnual*(PorPediatria/100)
    PreTraumatologia = PresupuestoAnual*(PorTraumatologia/100)

    print(f"\nPsiquiatría se le asigno el {PorPsiquiatria}% y tuvo un presupuesto de {PrePsiquiatria}. \nPediatría se le asigno el {PorPediatria}% y tuvo un presupuesto de {PrePediatria}. \nTraumatología se le asigno el {PorTraumatologia}% y tuvo un presupuesto de {PreTraumatologia}.")


#PUNTO 9
print("\nEste programa calcula el valor de un tiquete ida y vuelta.")
Distancia = float(input("\nDistancia recorrida en km: "))
Dias = int(input("Días de estancia: "))

Precio = Distancia*2.5

if Dias==7 and Distancia>800:
        Precio = Precio - (Precio*0.3)
        print(f"\nEl precio es {Precio} dolares")
else: 
    print(f"\nEl precio es {Precio} dolares")

    



