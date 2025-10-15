from task_manager.repository import TaskRepository
from task_manager.task import Task

class TaskService:
    def __init__(self, repository: TaskRepository):
        self.repository = repository

    def cria_tarefa(self, titulo, descricao, prioridade, prazo, status):
        task = Task(None, titulo, descricao, prioridade, prazo, status)
        self.repository.save(task)
        return task

    def listar_todas(self):
        return self.repository.find_all()

    def atualizar_status(self, id, status):
        task: Task = self.repository.find_by_id(id)
        task.status = status
        return task