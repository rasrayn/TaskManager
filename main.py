"""Menú de nuestra app"""
from taskManager import TaskManager


def printMenu():
        print("\n --- Gestor de Tareas Inteligente---")
        print("1. Añadir tarea.")
        print("2. Listar tarea.")
        print("3. Completar tarea.")
        print("4. Borrar tarea.")
        print("5. Salir")


def main():
    
    manager = TaskManager() #inicializamos en una variable fuera del bucle (programación funcional)
    
    """Para crear una app que pregunte continuamente al usuario vamos a crear un bucle infinito hasta que el usuario pulse salir"""
    while True:
        
        printMenu()
        choice = input("Elige una opción: ")

        match choice:
            case "1":
                description = input("Describa la tarea: ")
                manager.add_task(description)
            case "2":
                manager.list_task()
            case "3":
                id = input("ID de la tarea a completar: ")
                manager.complete_task(id)
            case "4":
                id = input ("ID de la tarea a eliminar: ")
                manager.delete_task(id)
            case "5":
                print("Saliendo")
                break     
            case _: #en python este es igual que el default en js
                print("Opción no válida. Selecciona otra.")
            

"""Esto hace que al iniciarse el archivo llamado main llame a la función main"""
if __name__ == "__main__":
    main()