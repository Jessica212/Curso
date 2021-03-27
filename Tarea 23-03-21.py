print("\tCalcula el área de las siguientes figuras, Ingresa el número que indica la figura que deseas calcular\n")
print("1.Triángulo\n2.Cuadrado\n3.Rectángulo\n4.Círculo\n5.Rombo\n")

opción=int(input("Ingresa el número de la figura deseada: "))
if(opción==1):
    base=float(input("Ingresa la base: "))
    altura=float(input("Ingresa la altura: "))
    res=(base*altura)/2
    print("El área del triángulo es: ",res)
elif(opción==2):
    lado =float(input("Ingresa el valor del lado: "))
    res=(lado**2)
    print("El área del cuadrado  es: ",res)
elif(opción==3):
    base =float(input("Ingresa la base: "))
    altura=float(input("Ingresa la altura: "))
    res=(base*altura)
    print("El área del rectángulo es: ",res)
elif(opción==4):
    pi=3.14
    radio=float(input("Ingresa el valor del radio: "))
    res=(pi*(radio**2))
    print("El área del círculo es: ",res)
elif(opción==5):
    dmenor=float(input("Ingresa la diagonal menor: "))
    dmayor=float(input("Ingresa la diagonal mayor: "))
    res=(dmenor*dmayor)/2
    print("El área del rombo es: ",res)
else:
    print("Opción no válida")
print("Hasta luego")