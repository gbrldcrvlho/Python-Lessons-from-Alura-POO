class Carteira:

    def __init__(self, total, notas, moedas):
        self.total = total
        self.notas = notas
        self.moedas = moedas

    def mostrar(self, total, notas, moedas):
        return f"voce possui: voce possui {total} em notas e {total} em moedas."
