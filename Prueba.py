nombre = input("¿Cómo te llamas? ")
edad_texto = input("¿Cuántos años tienes? ")

try:
    # INTENTAMOS convertir a número
    edad = int(edad_texto)
    print(f"Hola {nombre}, ¡el próximo año tendrás {edad + 1}!")
except ValueError:
    # SI FALLA, hacemos esto en lugar de mostrar el error rojo
    print(f"Oye {nombre}, '{edad_texto}' no es un número válido. ¡Escribe cifras (ej. 25)!")