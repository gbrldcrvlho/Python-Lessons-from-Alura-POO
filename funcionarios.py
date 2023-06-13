class Funcionario:
    def horas_registradas(self, horas):
        print('Horas Registradas...')

    def mostrar_tarefas(self):
        print('Fez muita coisa...')

class Caelum(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Caelumer')

    def buscar_cursos_do_mes(self, mes=None):
        print(f'Mostrando Cursos - {mes}' if mes else 'Mostrando cursos desse mes')

class Alura(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Alurete')

    def buscar_perguntas_sem_resposta(self):
        print('Mostrando perguntas nao respondidas do forum')

class Junior(Alura):
    pass

class Pleno(Alura, Caelum):
    pass

jose = Junior()
jose.buscar_perguntas_sem_resposta()

luan = Pleno()
luan.buscar_cursos_do_mes()
luan.buscar_perguntas_sem_resposta()

luan.mostrar_tarefas()

