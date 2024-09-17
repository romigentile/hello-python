## Sets: es un tipo de dato

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

my_other_set_1.add("CABA") # un set no es una estructura ordenada como las listas. No tiene orden.
print(my_other_set_1)
