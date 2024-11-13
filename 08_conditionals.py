## Condicionales - Establecen flujos de ejecucion del codigo - si se cumple una condicion ejecuto

my_condition = False

if my_condition: 
    print("Se ejecuta la condicion del if")

my_condition = 5*3

if my_condition == 10:
    print("Se ejecuta la condicion del segundo if")

if my_condition > 10 and my_condition < 20:
    print("Es mayor que 10 y menor a 20")
elif my_condition > 20:
    print("Es mayor a 20")
else:
    print("Es menor o igual que 10 o mayor o igual a 20")

print("La ejecucion continua")






