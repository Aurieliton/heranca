# Classe pai
class Funcionario:
    def __init__(self, matricula, nome, salario):
        self.matricula = matricula
        self.nome = nome
        self.salario = salario
    def exibirDados(self):
        print("--- DADOS DO FUNCIONÁRIO ---")
        print(f"Matricula: {self.matricula}")
        print(f"Nome: {self.nome}")
        print(f"Salário: {self.salario}")

class Professor(Funcionario):
    pass
class Monitor(Funcionario):
    pass
class Coordenador(Funcionario):
    pass
p1 = Professor(1, "Luiz", 3500)
p1.exibirDados()