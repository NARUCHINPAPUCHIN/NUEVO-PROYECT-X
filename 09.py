print("")
numero=int(input("Ingrese un numero de 4 cifras:"))

cifra_1=int(numero/1000)
cifra_2=int((numero%100)/100)
cifra_3=int(((numero%1000)%100)/10)
cifra_4=numero%10

print(cifra_1)
print(cifra_2)
print(cifra_3)
print(cifra_4)