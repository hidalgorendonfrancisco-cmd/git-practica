
# Lista para almacenar las tareas
tareas = []

def agregar_tarea(nombre_tarea):
    """
    Agrega una tarea a la lista de tareas.
    """
    if nombre_tarea:
        tareas.append(nombre_tarea)
        print(f"Tarea '{nombre_tarea}' agregada exitosamente.")
    else:
        print("El nombre de la tarea no puede estar vacío.")

def listar_tareas():
    """
    Imprime todas las tareas en la lista.
    """
    if not tareas:
        print("No hay tareas en la lista.")
    else:
        print("\nLista de tareas:")
        for i, tarea in enumerate(tareas, 1):
            print(f"{i}. {tarea}")

# Bloque principal para probar las funciones
if __name__ == "__main__":
    while True:
        print("\n--- Gestor de Tareas ---")
        print("1. Agregar tarea")
        print("2. Listar tareas")
        print("3. Salir")
        
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            nombre = input("Ingresa el nombre de la tarea: ")
            agregar_tarea(nombre)
        elif opcion == "2":
            listar_tareas()
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida, intenta de nuevo.")
