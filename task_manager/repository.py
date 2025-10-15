from task_manager.storage import InMemoryStorage
from task_manager.task import Task

class TaskRepository:
    def __init__(self, storage: InMemoryStorage):
        self.storage = storage
        self._next_id = 1

    def save(self, task: Task):
        task.id = self._next_id
        self._next_id += 1
        self.storage.add(task.id, task)
        return task
    
    def find_by_id(self, id):
        task = self.storage.get(id)
        if task:
            return task
        
        return None
    
    def delete(self, id):
        self.storage.delete(id)
        self._next_id -= 1

    def find_all(self):
        return self.storage.get_all()