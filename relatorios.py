class Relatorio:
    def gerar_relatorio(self):
        print('Relatorio Geral')

class relatorio_usuarios(Relatorio):
    def gerar_relatorio(self):
        print('Relatorio dos Usuarios')

class relatorio_custos(Relatorio):
    def gerar_relatorio(self):
        print('Relatorio de Custos')

relatorio1 = relatorio_usuarios()
relatorio2 = relatorio_custos()
relatorio3 = relatorio_usuarios()
relatorio4 = relatorio_usuarios()

relatorios = [relatorio1, relatorio2, relatorio3, relatorio4]
for rel in relatorios:
    rel.gerar_relatorio()