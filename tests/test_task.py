import pytest
from datetime import datetime, timedelta
from task_manager.task import Task, Priority, Status

def test_task_valida():
    prazo = datetime.now() + timedelta(days=1)
    task = Task(None, "Estudar", "Python", Priority.ALTA, prazo, Status.EM_PROGRESSO)
    assert task.titulo == "Estudar"

def test_titulo_curto_invalido():
    prazo = datetime.now() + timedelta(days=1)
    with pytest.raises(ValueError):
        task = Task(None, "AB", "Python", Priority.ALTA, prazo, Status.PENDENTE)

def test_prazo_passado_invalido():
    prazo = datetime.now() - timedelta(days=1)
    with pytest.raises(ValueError):
        task = Task(None, "Estudar", "PHP", Priority.MEDIA, prazo, Status.CONCLUIDA)