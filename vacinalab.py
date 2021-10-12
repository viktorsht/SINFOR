class VacinaLab:

    def __init__(self, nome, lab, reforco=0, data_ref_min=0,  data_ref_max=0):
        self._nome = nome
        self._lab = lab
        self._reforco = reforco
        self._data_ref_min = data_ref_min
        self._data_ref_max = data_ref_max
        self._qtd = 0

    def imprimir(self):
        print('\nNome: ', self._nome, ' | Laboratório Responsável: ', self._lab)
        if self._reforco:
            print('\tReforço de ', self._data_ref_min, ' até ', self._data_ref_max, ' dias')
        else:
            print('\t Dose única ')
