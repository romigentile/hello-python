## LOOPS - Pasamos por el mismo codigo varias veces

# WHILE

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 1 # si la condicion no cambia es un while infinito
else: 
    print("Mi condicion es > = 10") # cuando pasa el 10 se va al else, sale del bucle, permite mas control de la condicion

print("Sale del bucle")

while my_condition < 20:
    my_condition += 2
    if my_condition == 16:
        print("Mi condicion es = 16")
        break

    print(my_condition)