from task_manager.repository import TaskRepository
from datetime import datetime, timedelta
from task_manager.task import Task, Priority, Status

def test_save_atribui_id(mocker):
    mock_storage = mocker.Mock()
    repo = TaskRepository(mock_storage)

    prazo = datetime.now() + timedelta(days=1)
    task = Task(None, "Estudar", "Python", Priority.ALTA, prazo, Status.EM_PROGRESSO)

    resultado = repo.save(task)

    assert resultado.id == 1
    mock_storage.add.assert_called_once()

def test_save_chama_storage_add(mocker):
    mock_storage = mocker.Mock()
    repo = TaskRepository(mock_storage)

    prazo = datetime.now() + timedelta(days=1)
    task = Task(None, "Teste", "Desc", Priority.BAIXA, prazo, Status.CONCLUIDA)

    repo.save(task)

    mock_storage.add.assert_called_once_with(task.id, task)

def test_find_by_id_chama_storage_get(mocker):
    mock_storage = mocker.Mock()
    repo = TaskRepository(mock_storage)

    repo.find_by_id(5)

    mock_storage.get.assert_called_once_with(5)

def test_find_all_retorna_lista(mocker):
    mock_storage = mocker.Mock()
    mock_storage.get_all.return_value = ["t1", "t2"]

    repo = TaskRepository(mock_storage)
    resultado = repo.find_all()

    assert resultado == ["t1", "t2"]
    mock_storage.get_all.assert_called_once()