# Comenzamos a trabajar con diccionarios -

my_dict = dict() # constructor
print(type(my_dict))

my_other_dict = {} # tambien es un dict
print(type(my_other_dict))

my_other_dict = {"Nombre": "Romina", "Apellido": "Gentile", "Edad": 32, 1: "Python"} # relacion clave-valor - lo mejor es definir de que tipo va a ser la clave y el valor, pq no es fuertemente tipado - en este caso estamos mezclando
print(my_other_dict) 

my_dict = {
    "Nombre": "Romina", 
    "Apellido": "Gentile", 
    "Edad": 32, 
    "Lenguajes": {"Python", "C", "Javascript"}, # como valor es un set
    1: 36763885
    }

print(my_dict)

print(len(my_other_dict))
print(len(my_dict)) # cuenta las claves


# Acceso a las claves - muestra los elementos que tenga en esa clave

print(my_dict["Nombre"])
print(my_dict["Lenguajes"])

my_dict["Nombre"] = "Gisela" # Actualizo la clave - lo cambia
print(my_dict["Nombre"])

print(my_dict[1])

my_dict["Ciudad"] = "CABA" # Se agrega nueva clave y valor al diccionario
print(my_dict)

# my_dict.clear() # vacia el diccionario
# print(my_dict)

del my_dict["Ciudad"] # elimina clave y valor
print(my_dict)

# my_dict.pop("Ciudad") # elimina clave y valor

print("Gentile" in my_dict) # siempre sera FALSE pq asi busco por clave no por valor
print("Apellido" in my_dict) # aca si dara TRUE pq existe esa clave

print(my_dict.items()) # retorna el diccionario - listado de cada uno de los items

print(my_dict.keys()) # retorna un listado de las claves

print(my_dict.values()) # retorna los valores que hay en las claves

my_new_dict = my_dict.fromkeys(("Nombre", 1, "Pais")) # genera claves sin valor
print(my_new_dict)

my_new_dict = my_dict.fromkeys(my_dict) # genera claves sin valor de un diccionario existente, genera una copia de lo que le paso
print(my_new_dict)

my_new_dict = my_dict.fromkeys(my_dict, ("romigentile", "developer")) # le pongo ese valor a todas las claves
print(my_new_dict)

my_new_dict = my_dict.fromkeys(my_dict,)
print(my_new_dict)

print(my_dict.values())
print(list(my_dict))
print(tuple(my_dict))
print(set(my_dict))