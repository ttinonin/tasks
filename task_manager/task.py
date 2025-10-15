from enum import IntEnum, Enum
from datetime import datetime

class Priority(IntEnum):
    BAIXA = 1
    MEDIA = 2
    ALTA = 3

class Status(Enum):
    PENDENTE = "pendente"
    EM_PROGRESSO = "em_progresso"
    CONCLUIDA = "concluida"

class Task:
    def __init__(self, id, titulo, descricao, prioridade, prazo, status):
        self.validar(titulo, prazo)

        self.id: int = id
        self.titulo: str = titulo
        self.descricao: str = descricao
        self.prioridade: Priority = prioridade
        self.prazo: datetime = prazo
        self.status: Status = status

    def validar(self, titulo: str, prazo: datetime):
        if len(titulo) < 3:
            raise ValueError("O título deve ter pelo menos 3 caracteres.")
        
        if prazo < datetime.now():
            raise ValueError("O prazo não pode ser no passado.")