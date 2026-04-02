"""Funcionalidad de nuestra app"""

import json


class Task:
    def __init__(self, id, description, completada = False):
        self.id = id
        self.description = description
        self.completada = completada
    
    def __str__(self): 
        status = "✓" if self.completada else "✗" 
        return f"[{status}] #{self.id}: {self.description}"
    
class TaskManager:
    
    FILENAME = "task.json" #para guardar datos de forma persistente creamos una constante, en Python se escribe todo en mayuscula, donde vamos a guardar un archivo json que servirá para guardar las tareas.
    
    def __init__(self):
        """Definimos las variable que vamos a necesitar para iniciar una tarea"""
        self.tasks = []  
        self.next_id = 1
        self.load_tasks()
    
    def add_task(self, description):
        """Para añadir tareas, crearemos una variable task que llamará a la clase Task()"""
        task = Task(self.next_id, description)
        """Añadiremos la tarea"""
        self.tasks.append(task)
        """Incrementamos el id"""
        self.next_id += 1
        print(f"Tarea añadida, {description}" )
        self.save_tasks()
    def list_task(self):
        """Condición si no hay tareas"""
        if not self.tasks:
            print("No hay tareas pendientes")
        else:
            """Pero si hay tareas, se recorren y se muestran."""
            for task in self.tasks:
                print(task)
    
    def complete_task(self, id):
        for task in self.tasks:
            if task.id == id:
                task.completada = True
                print(f"Tarea completada: {task}")
                self.save_tasks()
                return
            print(f"Tarea no encontrada: #{id}")
    
    def delete_task(self, id):
        for task in self.tasks:
            if task.id == id:
                self.tasks.remove(task)
                print(f"Tarea eliminada: #{id}")
                self.save_tasks()
                return
            print(f"Tarea no encontrada: #{id}")
        
    def load_tasks(self): #Cargamos las tareas, este lo tendremos que poner al iniciar el progrmaa en el __init__
        try:
            with open(self.FILENAME, "r", encoding="utf-8") as file: #primero comprobamos que exista con with open(nombre fichero, carga solo lectura) y lo abrimos con un archivo.
            #ahora controlamos el error que puede salir si no existe el archivo con un try except
                content = file.read().strip() #lee contenido y lo devuelve limpio
                if not content: #si no hay contenido lo deja vacío
                    self.tasks = []
                    self.next_id = 1
                    return

                data = json.loads(content)# cargamos el contenido como un json
                self.tasks = [Task(item["id"], item["description"], item["completada"]) for item in data] #recorremos la tarea para imprimir sus valores.
                if self.tasks:# comprobamos si hay tareas, cogemos la ultima y le sumamo uno al id
                    self.next_id = self.tasks[-1].id + 1
                else: 
                    self.next_id = 1
        #Controlar el error de json vacio
        except json.JSONDecodeError:
            self.tasks = []
            self.next_id = 1
        #controlar si no encuentra el file.
        except FileNotFoundError:
            self.tasks = []
            self.next_id = 1
        
        
    def save_tasks(self): #para salvar los datos, lo pondremos en sitios de actualización, al crear, al completar o al eliminar tareas
        with open(self.FILENAME, "w") as file:
            json.dump( [{"id" : task.id, "description": task.description, "completada": task.completada}  for task in self.tasks], file, indent=4)