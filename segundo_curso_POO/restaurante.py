from segundo_curso_POO.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f"{self._nome} | {self._categoria}"
    
    @classmethod
    def listar_restaurantes(cls):
        print("Listando restaurantes:")
        for i in cls.restaurantes:
            print(f"- {i._nome} | {i._categoria} | {i.media_avaliacoes()} | {i.ativo}")

    def alternar_estado(self):
        self._ativo = not self._ativo

    @property
    def ativo(self):
        return "Restaurante ativo" if self._ativo else "Restaurante desativado"
    
    def receber_avaliacao(self, cliente, nota):
        if 0 <= nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    def media_avaliacoes(self):
        if not self._avaliacao:
            return "Sem avaliações"
        soma_avalicoes = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_avalicoes / quantidade_de_notas, 1)
        return media
    
