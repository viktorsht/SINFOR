from vacinalab import VacinaLab

# from vacinalab import VacinaLab
from comunitario import Comunitario
from servidor import Servidor
from loteVacina import LoteVacina
from datetime import date


class UBS:

    def __init__(self):
        self._servidor = {}
        self._comunitario = {'1': Comunitario(
            'wendel', '1', '27/10/1999', '0000')}
        self._vacina_lab = {}
        self._lote_vacina = {}
        self._vacinados_1dose = {}
        self._vacinados_2dose = {}
        self._lista_prioridade = []

    def add_comunitario(self, nome, cpf, nasc, sus, condicao=None):
        if cpf not in self._comunitario:
            self._comunitario[cpf] = Comunitario(
                nome, cpf, nasc, sus, condicao)
            print('Adicionado com sucesso!')

    def add_servidor(self, nome, cpf, nasc, sus, ocupacao, alocacao, condicao=None):
        if cpf not in self._servidor:
            self._servidor[cpf] = Servidor(
                nome, cpf, nasc, sus, ocupacao, alocacao, condicao)
            print('Adicionado com sucesso!')

    def add_vacina_lab(self, nome, lab, reforco=0, data_ref_min=0,  data_ref_max=0):
        try:
            if nome not in self._vacina_lab:
                self._vacina_lab[nome] = VacinaLab(
                    nome, lab, reforco, data_ref_min, data_ref_max)
                print('Adicionada com sucesso!')
        except:
            print('Esta vacina já consta em nossos dados!')

    def add_lote_vacina(self, nome, lote, fabricacao, validade, qtd):
        try:
            if qtd > 0:
                if nome in self._vacina_lab:
                    self._lote_vacina[lote] = LoteVacina(
                        nome, lote, fabricacao, validade, qtd)
                    self._vacina_lab[nome]._qtd += self._lote_vacina[lote]._qtd
                    print('Adicionado com sucesso!')

        except:
            print('Quantidade de vacinas precisa ser maior que zero!')

    def existe_servidor(self, cpf):
        if cpf in self._servidor.keys():
            return True
        else:
            return False

    def existe_comunitario(self, cpf):
        if cpf in self._comunitario.keys():
            return True
        else:
            return False

    def existe_vacina(self, vacina):
        if vacina in self._vacina_lab.keys():
            return True
        else:
            return False

    def existe_lote(self, lote):
        if lote in self._lote_vacina.keys():
            return True
        else:
            return False

    def vacinar_1dose(self, cpf, lote):
        hj = date.today()
        if self._comunitario[cpf]:
            if self._comunitario[cpf].autoriza_vacina1(self._lista_prioridade):
                self._comunitario[cpf]._1dose = 1
                self._comunitario[cpf]._data1dose = hj
                self._comunitario[cpf]._vacina_tipo = self._lote_vacina[lote]._nome
                self._lote_vacina[lote]._qtd -= 1
                self._vacinados_1dose[cpf] = self._comunitario[cpf]
                print('Vacinado adicionado com sucesso!')
            else:
                print('Pessoa não autorizada ... Verifique os dados e tente novamente!')
        elif self._servidor[cpf]:
            if self._comunitario[cpf].autoriza_vacina1(self._lista_prioridade):
                self._servidor[cpf]._1dose = 1
                self._servidor[cpf]._1dose = hj
                self._servidor[cpf]._vacina_tipo = self._lote_vacina[lote]._nome
                self._lote_vacina[lote]._qtd -= 1
                self._vacinados_1dose[cpf] = self._servidor[cpf]
                print('Vacinado adicionado com sucesso!')
            else:
                print('Pessoa não autorizada ... Verifique os dados e tente novamente!')

    def vacinar_2dose(self, cpf, lote):
        hj = date.today()
        if self._vacina_lab[self._lote_vacina[lote]._nome]._reforco == 1:
            min = self._vacina_lab[self._lote_vacina[lote]._nome]._data_ref_min
            max = self._vacina_lab[self._lote_vacina[lote]._nome]._data_ref_max
            if cpf in self._comunitario:
                if self._comunitario[cpf].autoriza_vacina2(min, max):
                    self._comunitario[cpf]._2dose = 1
                    self._comunitario[cpf]._2dose = hj
                    self._lote_vacina[lote]._qtd -= 1
                    self._vacinados_2dose[cpf] = self._comunitario[cpf]
                    print('Vacinado cadastrado com sucesso!')
                else:
                    print(
                        'Pessoa não autorizada ... Verifique os dados e tente novamente!')
            elif cpf in self._servidor:
                if self._servidor[cpf].autoriza_vacina2(min, max):
                    self._comunitario[cpf]._2dose = 1
                    self._comunitario[cpf]._2dose = hj
                    self._lote_vacina[lote]._qtd -= 1
                    self._vacinados_2dose[cpf] = self._comunitario[cpf]
                    print('Vacinado cadastrado com sucesso!')
                else:
                    print(
                        'Pessoa não autorizada ... Verifique os dados e tente novamente!')
        else:
            print('Vacina informada não necessita de reforço!')

    def imprimir_td_comunitario(self):
        for key, values in self._comunitario.items():
            self._comunitario[key].imprimir()

    def imprimir_td_servidor(self):
        for key, values in self._servidor.items():
            self._servidor[key].imprimir()

    def imprimir_td_vacina(self):
        for key, values in self._vacina_lab.items():
            self._vacina_lab[key].imprimir()

    def imprimir_td_lote(self):
        for key, values in self._lote_vacina.items():
            self._lote_vacina[key].imprimir()

    def imprimir_relatorio_1dose(self):
        hj = date.today()
        print('\tVacinados com a 1ª dose | data: ', hj)
        for key, values in self._vacinados_1dose.items():
            print('Nome: ', self._vacinados_1dose[key]._nome)
            print('CPF: ', self._vacinados_1dose[key]._cpf)

    def imprimir_relatorio_2dose(self):
        hj = date.today()
        print('\tVacinados com a 2ª dose | data: ', hj)
        for key, values in self._vacinados_2dose.items():
            print('Nome: ', self._vacinados_2dose[key]._nome)
            print('CPF: ', self._vacinados_2dose[key]._cpf)

    def imprimir_relatorio_vacina(self):
        hj = date.today()
        print('\tTotal de doses por vacina | data: ', hj)
        for key, values in self._vacina_lab.items():
            if values._qtd > 0:
                print('Nome da vacina: ', self._vacina_lab[key]._nome)
                print('Quantidade: ', self._vacina_lab[key]._qtd)

    def vacinados_tipo(self, vacina):
        qtd = 0
        for key, values in self._vacinados_1dose.items():
            if self._vacinados_1dose[key]._vacina_tipo == vacina:
                qtd += 1
        return qtd

    def qtd_tipo_vacina(self, vacina):
        qtd = 0
        for key, values in self._lote_vacina.items():
            if values._nome == vacina:
                qtd += values._qtd
        return qtd

    def total_vacinas(self):
        qtd = 0
        for key, values in self._lote_vacina.items():
            qtd += values._qtd
        return qtd

    def existe_condicao(self, condicao):
        for c in self._lista_prioridade:
            if c == condicao:
                return True
        return False

    def remover_lote(self, lote):
        if lote in self._lote_vacina:
            self._lote_vacina.pop(lote)
            print('Removido com sucesso!')
