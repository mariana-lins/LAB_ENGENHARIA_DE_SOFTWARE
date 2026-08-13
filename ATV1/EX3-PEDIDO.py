class Pedido:
    def __init__(self, numero):
        self.numero = numero
        self._status = "Pendente"

    @property
    def status(self):
        return self._status

    def atualizar_status(self, novo_status):
        status_validos = [
            "Pendente",
            "Processando",
            "Enviado",
            "Entregue",
            "Cancelado"
        ]

        if novo_status in status_validos:
            self._status = novo_status
        else:
            raise ValueError("Status inválido")
