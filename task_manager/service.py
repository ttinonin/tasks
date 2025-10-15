from task_manager.repository import TaskRepository

class TaskService:
    def __init__(self, repository: TaskRepository):
        self.repository = repository

    def cria_tarefa(self):
        pass

    def listar_todas(self):
        pass

    def atualizar_status(self, id, status):
        pass