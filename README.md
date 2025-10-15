# Sistema Task Manager

Sistema de Gerenciamento de Tarefas simples em Python.

## Como instalar

1. Clone o repositório:
```bash
git clone https://github.com/ttinonin/tasks.git
cd tasks
```

2. Crie um ambiente virtual:

```bash
python -m venv venv
./venv/Scripts/activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Como testar

Execute todos os testes com pytest:
```bash
pytest -v .\tests\
```

## Estrutura do projeto
```bash
task_manager/
├── __init__.py
├── task.py
├── repository.py
└── storage.py
└── service.py
tests/
├── __init__.py
├── test_task.py
└── test_repository.py
requirements.txt
README.md
```