"""
INE5605 - Desenvolvimento de Sistemas Orientados a Objetos I
Trabalho 1 - Parte 1: Entidades (Model)

Aluno: Lucca Bolsanello Ciotti (25202568)
"""

from abc import ABC, abstractmethod
from datetime import date, time


# =============================================================================
# PESSOA (classe abstrata)
# =============================================================================

class Pessoa(ABC):
    """Classe abstrata base para Paciente e Profissional."""

    def __init__(self, nome: str, celular: str, cpf: str):
        self._nome = nome
        self._celular = celular
        self._cpf = cpf

    @property
    def nome(self): return self._nome

    @property
    def celular(self): return self._celular

    @property
    def cpf(self): return self._cpf

    @abstractmethod
    def descricao(self) -> str:
        pass

    def __str__(self):
        return f"{self._nome} (CPF: {self._cpf})"


# =============================================================================
# PACIENTE
# =============================================================================

class Paciente(Pessoa):
    """Paciente cadastrado no sistema."""

    def __init__(self, nome: str, celular: str, cpf: str, data_nascimento: date):
        super().__init__(nome, celular, cpf)
        self._data_nascimento = data_nascimento

    @property
    def data_nascimento(self): return self._data_nascimento

    @property
    def idade(self) -> int:
        hoje = date.today()
        anos = hoje.year - self._data_nascimento.year
        if (hoje.month, hoje.day) < (self._data_nascimento.month, self._data_nascimento.day):
            anos -= 1
        return anos

    def descricao(self) -> str:
        return f"Paciente: {self._nome}, {self.idade} anos"


# =============================================================================
# PROFISSIONAL
# =============================================================================

class Profissional(Pessoa):
    """Profissional de saúde cadastrado no sistema."""

    def __init__(self, nome: str, celular: str, cpf: str,
                 especialidade: str, registro_profissional: str):
        super().__init__(nome, celular, cpf)
        self._especialidade = especialidade
        self._registro_profissional = registro_profissional

    @property
    def especialidade(self): return self._especialidade

    @property
    def registro_profissional(self): return self._registro_profissional

    def descricao(self) -> str:
        return f"Profissional: {self._nome} | {self._especialidade}"


# =============================================================================
# CLINICA
# =============================================================================

class Clinica:
    """Clínica de saúde cadastrada no sistema."""

    def __init__(self, nome: str, cidade: str, descricao: str,
                 horario_abertura: time, horario_fechamento: time):
        self._nome = nome
        self._cidade = cidade
        self._descricao = descricao
        self._horario_abertura = horario_abertura
        self._horario_fechamento = horario_fechamento

    @property
    def nome(self): return self._nome

    @property
    def cidade(self): return self._cidade

    @property
    def descricao(self): return self._descricao

    @property
    def horario_abertura(self): return self._horario_abertura

    @property
    def horario_fechamento(self): return self._horario_fechamento

    def __str__(self):
        return f"Clínica: {self._nome} | {self._cidade}"


# =============================================================================
# TIPO DE ATENDIMENTO
# =============================================================================

class TipoAtendimento:
    """Tipo de atendimento disponível (consulta, exame, retorno, etc.)."""

    def __init__(self, descricao: str):
        self._descricao = descricao

    @property
    def descricao(self): return self._descricao

    def __str__(self):
        return self._descricao


# PROCEDIMENTO  [COMPOSIÇÃO com Atendimento]

class Procedimento:
    """
    Procedimento realizado durante um atendimento.
    Não existe independentemente do Atendimento (composição).
    """

    def __init__(self, descricao: str, custo: float, profissional: Profissional):
        self._descricao = descricao
        self._custo = custo
        self._profissional = profissional  # associação

    @property
    def descricao(self): return self._descricao

    @property
    def custo(self): return self._custo

    @property
    def profissional(self): return self._profissional

    def __str__(self):
        return f"{self._descricao} - R$ {self._custo:.2f}"


# ATENDIMENTO

class Atendimento:
    """
    Atendimento agendado entre paciente e profissional em uma clínica.
    - Agrega Clinica (agregação)
    - Possui Procedimentos (composição)
    """

    def __init__(self, clinica: Clinica, paciente: Paciente,
                 profissional: Profissional, data: date,
                 hora_inicio: time, hora_fim: time,
                 tipo: TipoAtendimento, valor: float):
        self._clinica = clinica            # agregação
        self._paciente = paciente          # associação
        self._profissional = profissional  # associação
        self._data = data
        self._hora_inicio = hora_inicio
        self._hora_fim = hora_fim
        self._tipo = tipo                  # associação
        self._valor = valor
        self._procedimentos: list[Procedimento] = []  # composição

    @property
    def clinica(self): return self._clinica

    @property
    def paciente(self): return self._paciente

    @property
    def profissional(self): return self._profissional

    @property
    def data(self): return self._data

    @property
    def hora_inicio(self): return self._hora_inicio

    @property
    def hora_fim(self): return self._hora_fim

    @property
    def tipo(self): return self._tipo

    @property
    def valor(self): return self._valor

    @property
    def procedimentos(self): return list(self._procedimentos)

    def adicionar_procedimento(self, p: Procedimento):
        self._procedimentos.append(p)

    def __str__(self):
        return (f"Atendimento: {self._paciente.nome} com {self._profissional.nome} "
                f"em {self._data} | {self._tipo}")



# PAGAMENTO (classe abstrata) 

class Pagamento(ABC):
    """
    Classe abstrata para pagamentos de atendimentos.
    Subclasses: PagamentoDinheiro, PagamentoPix, PagamentoCartao.
    """

    def __init__(self, data_pagamento: date, atendimento: Atendimento,
                 paciente: Paciente, valor_pago: float):
        self._data_pagamento = data_pagamento
        self._atendimento = atendimento  # agregação
        self._paciente = paciente        # associação
        self._valor_pago = valor_pago

    @property
    def data_pagamento(self): return self._data_pagamento

    @property
    def atendimento(self): return self._atendimento

    @property
    def paciente(self): return self._paciente

    @property
    def valor_pago(self): return self._valor_pago

    @property
    def valor_restante(self):
        return self._atendimento.valor - self._valor_pago

    @abstractmethod
    def modalidade(self) -> str:
        pass

    def __str__(self):
        return f"Pagamento [{self.modalidade()}] R$ {self._valor_pago:.2f}"


class PagamentoDinheiro(Pagamento):
    def modalidade(self): return "Dinheiro"


class PagamentoPix(Pagamento):
    def __init__(self, data_pagamento, atendimento, paciente, valor_pago, cpf_pagador: str):
        super().__init__(data_pagamento, atendimento, paciente, valor_pago)
        self._cpf_pagador = cpf_pagador

    @property
    def cpf_pagador(self): return self._cpf_pagador

    def modalidade(self): return "Pix"


class PagamentoCartao(Pagamento):
    def __init__(self, data_pagamento, atendimento, paciente, valor_pago,
                 numero_cartao: str, bandeira: str):
        super().__init__(data_pagamento, atendimento, paciente, valor_pago)
        self._numero_cartao = numero_cartao
        self._bandeira = bandeira

    @property
    def numero_cartao(self): return self._numero_cartao

    @property
    def bandeira(self): return self._bandeira

    def modalidade(self): return f"Cartão ({self._bandeira})"
