print("")
dinero_victor=float(input("Dinero de Victor: $"))
dinero_leo=float(input("Dinero de Leo: $"))
dinero_angelo=float(input("Dinero de Angelo: $"))

dolares_angelo=dinero_angelo/3
capital_total=dinero_victor+dinero_leo+dolares_angelo
porcentaje_victor=(dinero_victor*100)/capital_total
porcentaje_leo=(dinero_leo*100)/capital_total
porcentaje_angelo=(dolares_angelo*100)/capital_total

print("El capital total es: $",format(capital_total,".2f"),"%")
print("Victor dio el",format(porcentaje_victor,".2f"),"%")
print("Leo dio el",format(porcentaje_leo,".2f"),"%")
print("Angelo dio el",format(porcentaje_angelo,"2f"),"%")