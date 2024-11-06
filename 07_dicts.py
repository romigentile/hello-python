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
    "Lenguajes": {"Python", "C", "Javascript"} # como valor es un set
    }

print(my_dict)
print(my_other_dict)