## Sets: es un tipo de dato. # un set no es una estructura ordenada como las listas. No tiene orden. Por eso no se puede acceder a los elementos. No acepta repetidos # Si no coloco el constructos set() y lo defino con {} se crea como un diccionario, hasta que le pongo datos, donde ahi se vuelve set

my_set = set()
print(type(my_set))

my_other_set_1= {} # vacio es un diccionario
print(type(my_other_set_1))

my_other_set_1 = {"Gentile", "Romi", 32, 1.64}
print(type(my_other_set_1))

my_other_set_2 = set([1, 2, 3, 4, 5])
print(type(my_other_set_2))

print(len(my_other_set_1))

# print(my_other_set_1[0]) # TypeError: 'set' object is not subscriptable

my_other_set_1.add("CABA") # añade elementos al set
print(my_other_set_1)

print("CABA" in my_other_set_1) # existe en el set? TRUE or FALSE
print("Romii" in my_other_set_1)

my_other_set_1.remove("CABA") # lo remueve
print(my_other_set_1)

my_other_set_1.clear() # lo limpia, es propio de los sets, al contrario del del que es propio del sistema
print(len(my_other_set_1))


# Esto no se suele hacer es muy arriesgado pq no se conoce el orden de la lista
my_set = {"romi", 32, 1.64, "CABA"}
my_list = list(my_set)
print(my_list)
print(type(my_list))
print(my_list[0])

my_other_set_2 = {"JavaScript", "Python", "C"}

my_new_set_1 = my_set.union(my_other_set_2) # union de sets
print(my_new_set_1)

my_new_set_2 = my_set.union(my_other_set_2).union({"Gentile"})
print(my_new_set_2)

print(my_new_set_1.difference(my_set)) # imprime lo que tienen como diferencia

