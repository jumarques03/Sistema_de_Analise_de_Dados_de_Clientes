from .Cliente import Cliente

class ClientePremium(Cliente):
    def __init__(self, id:int , nome:str , saldo: float, limite_credito: float):
        super().__init__(id, nome, saldo)
        self._limite_credito = limite_credito

    def __str__(self) -> str:
        return super().__str__() + f" | Limite: {self._limite_credito}"