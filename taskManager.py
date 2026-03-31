"""Funcionalidad de nuestra app"""

class Task:
    def __init__(self, id, descripcion, completada = False):
        self.id = id
        self.descripcion = descripcion
        self.completada = completada
    
    def __str__(self): 
        status = "✓" if self.completada else "✗" 
        return f"[{status}] #{self.id}: {self.descripcion}"
    
class TaskManager:
    def __init__(self):
        """Definimos las variable que vamos a necesitar para iniciar una tarea"""
        self.tasks = []  
        self.next_id = 1
    
    def add_task(self, description):
        """Para añadir tareas, crearemos una variable task que llamará a la clase Task()"""
        task = Task(self.next_id, description)
        """Añadiremos la tarea"""
        self.tasks.append(task)
        """Incrementamos el id"""
        self.next_id += 1
        print(f"Tarea añadida, {description}" )
    
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
                task.complete = True
                print(f"Tarea completada: {task}")
                return
            print(f"Tarea no encontrada: #{id}")
    
    def delete_task(self, id):
        for task in self.tasks:
            if task.id == id:
                self.tasks.remove(task)
                print(f"Tarea eliminada: #{id}")
                return
            print(f"Tarea no encontrada: #{id}")