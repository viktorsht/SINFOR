class LoteVacina:

    def __init__(self, nome, lote, fabricacao, validade, qtd):
        self._nome = nome
        self._lote = lote
        self._fabricacao = fabricacao
        self._validade = validade
        self._qtd = qtd

    def imprimir(self):
        print('\nNome: ', self._nome,
              ' | Lote: ', self._lote,
              '\nFabricação ', self._fabricacao,
              ' Validade ', self._validade,
              ' Quantidade ', self._qtd)
