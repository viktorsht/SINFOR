from pessoa import Pessoa
from idade import *

class Servidor(Pessoa):


    def __init__(self, nome, cpf, nasc, sus, ocupacao, alocacao, condicao = None):
        super().__init__(nome, cpf, nasc, sus)
        self._ocupacao = ocupacao
        self._alocacao = alocacao
        self._data1dose = None
        self._data2dose = None
        self._1dose = 0
        self._2dose = 0
        self._condicao = condicao
        self._vacina_tipo = None

    @property
    def ocupacao(self):
        return self._ocupacao

    @property
    def alocacao(self):
        return self._alocacao

    def imprimir(self):
        print('\n\tNome: ', self._nome, ' | CPF: ', self._cpf, ' | Nasc: ', self._nasc, ' | SUS: ', self._sus,
              ' | Ocupação: ', self._ocupacao, ' | Alocação: ', self._alocacao)
        if self._1dose == 1:
            print('1ª dose de ', self._vacina_tipo, ' aplicada em ', self._data1dose)
            if self._2dose == 1:
                print('e 2ª dose de ', self._vacina_tipo, ' aplicada em ', self._data2dose)
        else:
            print('Ainda não tomou nenhuma dose de vacina')

    def autoriza_vacina1(self, lista_condicoes):
        id = calcula_idade(self._nasc)
        if id >= 40:
            return True
        else:
            for c in lista_condicoes:
                if c == self._condicao or c == self._alocacao:
                    return True
        return False

    def autoriza_vacina2(self, data_min, data_max):
        if self._1dose == 1 and self._2dose == 0:
            dias = conta_dias(self._data1dose)
            if dias >= data_min or dias <= data_max:
                return True
            else:
                return False
