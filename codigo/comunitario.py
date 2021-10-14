from pessoa import Pessoa
from idade import *

class Comunitario(Pessoa):
    def __init__(self, nome, cpf, nasc, sus, condicao = None):
        super().__init__(nome, cpf, nasc, sus)
        self._1dose = 0
        self._2dose = 0
        self._data1dose = None
        self._data2dose = None
        self._condicao = condicao
        self._vacina_tipo = None

    def imprimir(self):
        print('\n\tNome: ',self._nome,' | CPF: ', self._cpf,' | Nasc: ', self._nasc, ' | SUS: ', self._sus)
        if self._1dose == 1:
            print('1ª dose de ', self._vacina_tipo, ' aplicada em ', self._data1dose)
            if self._2dose == 1:
                print('e 2ª dose de ', self._vacina_tipo, ' aplicada em ', self._data2dose)
        else:
            print('Ainda não tomou nenhuma dose de vacina')

    def autoriza_vacina1(self, lista_condicoes):
        if self._1dose == 0:
            resultado_idade = calcula_idade(self._nasc)
            if resultado_idade >= 30:
                return True
            else:
                for c in lista_condicoes:
                    if c == self._condicao:
                        return True
        return False

    def autoriza_vacina2(self, data_min, data_max):
        if self._1dose == 1 and self._2dose == 0:
            dias = conta_dias(self._data1dose)
            if dias >= data_min or dias <= data_max:
                return True
            else:
                return False