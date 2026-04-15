"""Menú de nuestra app"""
from taskManager import TaskManager
from ia_service import create_simple_tasks


def printMenu():
        print("\n --- Gestor de Tareas Inteligente---")
        print("1. Añadir tarea.")
        print("2. Añadir tarea compleja.(IA)")
        print("3. Listar tarea.")
        print("4. Completar tarea.")
        print("5. Borrar tarea.")
        print("6. Salir")


def main():
    
    manager = TaskManager() #inicializamos en una variable fuera del bucle (programación funcional)
    
    """Para crear una app que pregunte continuamente al usuario vamos a crear un bucle infinito hasta que el usuario pulse salir"""
    while True:
        
        printMenu()
        
        try:
            choice = int(input("Elige una opción: "))

            match choice:
                case 1:
                    description = input("Describa la tarea: ")
                    manager.add_task(description)
                case 2:
                    description = input("Descripción de la tarea compleja: ")
                    subtasks = create_simple_tasks(description)
                    #al añadir la tarea llamamos al manager y añadimos la tarea si no tenemos Error
                    for subtask in subtasks:
                        if not subtask.startswith("Error:"):
                            manager.add_task(subtask)
                        else:
                            print(subtask)
                            break # para no seguir realizando el for ya que si hay un error no tiene sentido buscar mas subtareas
                case 3:
                    manager.list_task()
            
                case 4:
                    id = int(input("ID de la tarea a completar: "))
                    manager.complete_task(id)
                case 5:
                    id = int(input ("ID de la tarea a eliminar: "))
                    manager.delete_task(id)
                case 6:
                    print("Saliendo")
                    break     
                case _: #en python este es igual que el default en js
                    print("Opción no válida. Selecciona otra.")
        except ValueError:
            print("Opción no válida. Selecciona otra.")

"""Esto hace que al iniciarse el archivo llamado main llame a la función main"""
if __name__ == "__main__":
    main()