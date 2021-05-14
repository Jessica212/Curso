#Palindromo
palabraalreves=""
print("Introduce una palabra  ")
palabra=input("")
for i in range (len(palabra),-1,-1):
    palabraalreves=palabraalreves+palabra[i:i+1]
if palabraalreves==palabra:
    print("Es un palíndromo")
else: 
    print("No es un palíndromo")
