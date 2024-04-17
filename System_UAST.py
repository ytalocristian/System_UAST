class Endereco:
    def __init__(self, rua, numero, bairro, cidade, estado):
        self.rua = rua
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado

    def __str__(self):
        return f"Endereço: {self.rua}, Numero: {self.numero} - {self.cidade}, {self.estado}"


class Curso:
    def __init__(self, nome, codigo, carga_horaria):
        self.nome = nome
        self.codigo = codigo
        self.carga_horaria = carga_horaria

    def __str__(self):
        return f"Curso: {self.nome}, Código do curso: ({self.codigo}) - Carga Horária: {self.carga_horaria}"


class Disciplina:
    def __init__(self, nome, codigo, carga_horaria):
        self.nome = nome
        self.codigo = codigo
        self.carga_horaria = carga_horaria

    def __str__(self):
        return f"Disciplina: {self.nome}, Código da disciplina: ({self.codigo}) - Carga Horária: {self.carga_horaria}"


class Professor:
    def __init__(self, nome, departamento):
        self.nome = nome
        self.departamento = departamento
        self.disciplinas = []

    def adicionar_disciplina(self, disciplina):
        self.disciplinas.append(disciplina)

    def __str__(self):
        disciplinas_str = "\n".join([f"  - {disciplina.nome} ({disciplina.codigo})" for disciplina in self.disciplinas])
        return f"Professor: {self.nome} ({self.departamento})\nDisciplinas ministradas:\n{disciplinas_str}"


class Aluno:
    def __init__(self, nome, matricula, curso, endereco):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
        self.endereco = endereco

    def __str__(self):
        return f"Aluno: {self.nome} ({self.matricula})\n{self.curso}\n{self.endereco}"


class Sala:
    def __init__(self, numero, capacidade, localizacao):
        self.numero = numero
        self.capacidade = capacidade
        self.localizacao = localizacao

    def __str__(self):
        return f"Sala: {self.numero} - Capacidade: {self.capacidade} pessoas\nLocalização: {self.localizacao}"


# instancia das classes
endereco_aluno = Endereco("Rua 1", 123, "Centro", "Cidade", "Estado")
curso_engenharia = Curso("Engenharia", "ENG", 4000)
aluno1 = Aluno("João", 123, curso_engenharia, endereco_aluno)
disciplina_fisica = Disciplina("Física", "FIS", 80)
disciplina_matematica = Disciplina("Matemática", "MAT", 80)
professor_fisica = Professor("Maria", "Física")
professor_matematica = Professor("José", "Matemática")
professor_matematica.adicionar_disciplina(disciplina_matematica)
professor_fisica.adicionar_disciplina(disciplina_fisica)
sala_aula = Sala(1, 50, "Bloco A")

# exibindo informações
print(aluno1)
print()
print(endereco_aluno)
print()
print(professor_fisica)
print()
print(professor_matematica)
print()
print(sala_aula)
print("\n")

#exibindo informações
print("Diagrama de classes:")
print("┌────────────────────┐")
print("│        Aluno       │")
print("└────────────────────┘")
print("| - nome: str        |")
print("| - matricula: int   |")
print("| - curso: Curso     |")
print("| - endereco: End.   |")
print("└────────────────────┘\n")

print("┌────────────────────┐")
print("│     Endereço       │")
print("└────────────────────┘")
print("| - rua: str         |")
print("| - numero: int      |")
print("| - bairro: str      |")
print("| - cidade: str      |")
print("| - estado: str      |")
print("└────────────────────┘\n")

print("┌────────────────────┐")
print("│      Curso         │")
print("└────────────────────┘")
print("| - nome: str        |")
print("| - codigo: str      |")
print("| - carga_horaria:int|")
print("└────────────────────┘\n")

print("┌────────────────────┐")
print("│    Disciplina      │")
print("└────────────────────┘")
print("| - nome: str        |")
print("| - codigo: str      |")
print("| - carga_horaria:int|")
print("└────────────────────┘\n")

print("┌────────────────────┐")
print("│    Professor       │")
print("└────────────────────┘")
print("| - nome: str        |")
print("| - departamento: str|")
print("| - disciplinas: list|")
print("└────────────────────┘\n")

print("┌────────────────────┐")
print("│       Sala         │")
print("└────────────────────┘")
print("| - numero: int      |")
print("| - capacidade: int  |")
print("| - localizacao: str |")
print("└────────────────────┘\n")
