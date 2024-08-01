# Variables 

my_string_variable = "Hola mundo"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = True
print(my_bool_variable)

# Concatenacion de variables en un print

print(my_string_variable + ", como estas?, " + str(my_int_variable))

print(my_string_variable, my_int_variable, my_bool_variable)

print(type(print(my_string_variable, my_int_variable, my_bool_variable))) # None Type

# Funciones del sistema

# cuenta cuantos caracteres tiene la variable, contando espacios

print(len(my_string_variable)) 

# variables en una sola linea - no es buena practica

name, surname, alias, age = "Romina", "Gentile", "romigentile", 32 

print("Mi nombre es: ", name, surname, ". Mi alias es: ", alias, ". Mi edad es: ", age)

# Python no es un lenguaje fuertemente tipado.

address: str = "Calle 123" # Es solo para decir que queremos que sea un string, pero no e suna forma de forzar el tipado.
print(type(address))
address = 123 # Se cambia a numero
print(address)
print(type(address))