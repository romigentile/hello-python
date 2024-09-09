## Listas

my_list = list() 

my_other_list = []

print(len(my_list))

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(my_list)
print(len(my_list))

my_other_list = [32, 1.64 , "Romi", "Gentile"]

print(my_other_list)

print(type(my_other_list))
print(my_other_list[2])
print(my_other_list[-2])
print(my_other_list[0:3])

# print(my_other_list[4]) INDEX ERROR

print(my_other_list.count("Romi")) # Sirve para contar los elementos iguales de la lista

age, height, name, surname = my_other_list # No es por el nombre, es por la posicion. Lo desempaqueto

print(name)

my_other_list.append("CABA") # Agrega elementos al final de la lista
print(my_other_list)


print(my_list + my_other_list)


my_other_list.insert(2, "Femenino") # Agrega elementos en una posicion especifica

print(my_other_list)

my_other_list.remove("Femenino") # Elimina elementos de la lista

print(my_other_list)