from pessoa import Pessoa
from idade import *


class Comunitario(Pessoa):
    def __init__(self, nome, cpf, sus, nasc, dose1=0, data1dose=None, vacina1=None, lote1=0, dose2=0, data2dose=None, vacina2=None, lote2=0, condicao=None):
        super().__init__(nome, cpf, nasc, sus)
        self._dose1 = dose1
        self._dose2 = dose2
        self._vacina1 = vacina1
        self._vacina2 = vacina2
        self._lote1 = lote1
        self._lote2 = lote2
        self._data1dose = data1dose
        self._data2dose = data2dose
        self._condicao = condicao
        self._senha = '1'
        self._vacina_tipo = None

    def imprimir(self):
        print('\n\tNome: ', self._nome, ' | CPF: ', self._cpf,
              ' | Nasc: ', self._nasc, ' | SUS: ', self._sus)
        if self._1dose == 1:
            print('1ª dose de ', self._vacina_tipo,
                  ' aplicada em ', self._data1dose)
            if self._2dose == 1:
                print('e 2ª dose de ', self._vacina_tipo,
                      ' aplicada em ', self._data2dose)
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
