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