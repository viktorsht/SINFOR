import abc

class Pessoa(abc.ABC):

    def __init__(self, nome, cpf, nasc, sus):
        self._nome = nome
        self._cpf = cpf
        self._nasc = nasc
        self._sus = sus

    @property
    def nome(self):
        return self._nome

    @property
    def cpf(self):
        return self._cpf

    @property
    def nasc(self):
        return self._nasc

    @property
    def sus(self):
        return self._sus

    def imprimir(self):
        print('Nome: ', self._nome, ' | CPF: ', self._cpf, ' | Data de Nascimento: ', self._nasc, ' | SUS: ', self._sus)

