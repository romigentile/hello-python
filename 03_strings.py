## Strings 

my_string_1 = "Hola mundo"
print(my_string_1)

my_string_2 = 'Hola mundoo'
print(my_string_2)

my_string_3 = """Hola mundooo"""
print(my_string_3)

my_string_4 = '''Hola mundoooo'''
print(my_string_4)

print(my_string_1 + " " + my_string_2)

my_new_line_string = "Hola mundo\ncon salto de linea"
print(my_new_line_string)

my_tab_string = "Hola mundo\n\tcon tabulador y salto de linea"
print(my_tab_string)

my_scape_string = "Hola mundo \\n con barra invertida"
print(my_scape_string)

# FORMATEO

name, surname, age = "Romi", "Gentile", 32

print("Mi nombre es %s %s y mi edad es %d" % (name, surname, age)) # %s para strings, %d para enteros

print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age)) # {} para strings, {} para enteros

print(f"Mi nombre es {name} {surname} y mi edad es {age}") # inferencia de datos

# Desempaquetado de caracteres

language = "Python"
a, b, c, d, e, f = language

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# Division

language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[:3]
print(language_slice)

language_slice = language[-2] # empieza desde el final
print(language_slice)

language_slice = language[0:6:2] # salta de 2 en 2, pero es muy rebuscado
print(language_slice)

# Reversión

reversed_language = language[::-1]
print(reversed_language)


