# Write your code below this line 👇
print('''
    Welcome to the Band Name Generator | Bienvenido al Generador de Nombres de Bandas
    
    EN: Please select in your language, entering the corresponding number.   
    ES: Por favor selecciona en tu idioma, ingresando el numero correspondiente.
    
    1) English      2) Español
''')


while True:
    try:
        language = int(input('Language | Idioma : '))
    except ValueError:
        print("Error: You must enter a number | Debe ingresar un número ")
        continue
    else:
        if language == 1:
            city = input("Wath's name of the city you grew up in? ")
            pet = input('What is the name of your pet? ')
            print(f'Your band name could be: {city} {pet}\'s ')
        elif language == 2:
            city = input("¿Cuál es el nombre de la ciudad en la que creciste? ")
            pet = input('¿Cual es el nombre de tu mascota? ')
            print(f'El nombre de tu banda podría ser: {city} {pet}\'s ')
        else:
            print("Error: Invalid number try again | Número inválido inténtalo de nuevo ")
            continue
    break
