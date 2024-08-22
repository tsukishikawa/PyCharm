class Cliente:
    def __init__(self, nome, telefone):
        self._nome = nome
        self._telefone = telefone

    # Metodo get
    @property
    def nome(self):
        return self._nome

    # Metodo set
    @nome.setter
    def nome(self, nome):
        self._nome = nome