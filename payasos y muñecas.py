#jugueteria
payasos=int(input("Cantidad de payasos  "))
muñecas=int(input("Cantidad de muñecas  "))
pesodepayasos=(payasos*0.112)
pesodemuñecas=(muñecas*0.075)
pesototal=pesodepayasos+pesodemuñecas
print("Peso total en kilogramos es:",pesototal)
pesajeacobrar=(pesototal/55)
if pesajeacobrar<=1:
    print("El costo por el envio de los payasos y la muñeca  es $115")
else:
    print("El costo por el envio de los payasos y muñecas es $",round(pesajeacobrar)*115)



