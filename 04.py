pies=float(input("Pies:"))
pulgadas=float(input("Pulgadas:"))

estatura=(((pies*12)+pulgadas)*2.54)/100

print("La Estatura en metros es:",format(estatura,".2f"),"m")