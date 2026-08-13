class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self._notas = []

    def adicionar_nota(self, nota):
        self._notas.append(nota)

    def media(self):
        if not self._notas:
            return 0

        return sum(self._notas) / len(self._notas)
