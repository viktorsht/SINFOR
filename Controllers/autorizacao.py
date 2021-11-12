import abc

class Autorizacao(abc.ABC):
    ''' Classe abstrata para classes de objetos
     que podem ser agendados para aplicação da vacina'''

    @abc.abstractmethod
    def autoriza_vacina1(self, lista_condicoes):
        ''' Metodo abstrato para realizar o agendamento para a vacina.
        Retorna True e permite o agendamento do objeto'''
        pass

    @abc.abstractmethod
    def autoriza_vacina2(self,data_min, data_max):
        ''' Metodo abstrato para realizar o agendamento para a vacina.
        Retorna True e permite o agendamento do objeto'''
        pass