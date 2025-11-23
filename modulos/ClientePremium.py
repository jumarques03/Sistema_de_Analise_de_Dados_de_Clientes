from .Cliente import Cliente

class ClientePremium(Cliente):
    def __init__(self, id:int , nome:str , saldo: float, limite_credito: float):
        """
        Construtor da classe ClientePremium, herda a classe Cliente

        Args:
            self: a própria instância
            id: id único do cliente (int)
            nome: nome do cliente (str)
            saldo: saldo bancário do cliente (float)
            limite_credito: limite do crédito bancário (float)
        """
        super().__init__(id, nome, saldo)
        self._limite_credito = limite_credito

    def __str__(self) -> str:
        """
        Exibe de forma amigável ao usuário os inputs dos dados

        Args:
            self: a própria instância
        """
        return super().__str__() + f" | Limite: {self._limite_credito}"