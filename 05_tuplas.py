# Tuplas! 
# La principal diferencia con las listas es que no tienen tantas operaciones como las listas.

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (32, 1.64 , "Romi", "Gentile")

print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple.count("Romi")) # Sirve para contar los elementos iguales de la lista
print(my_tuple.index("Gentile")) # Sirve para encontrar el indice de la lista
#print(my_tuple.index("Hola")) # INDEXERROR

#my_tuple[0] = 33 # INDEXERROR No se puede cambiar el valor de una tupla, son valores constantes, al contrario de una lista

