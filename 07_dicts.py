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

