class Cliente:
    def __init__(self, id:int, nome:str, saldo:float):
        self._id = id
        self._nome = nome
        self._saldo = saldo

    def __str__(self) -> str:
        return f"ID: {self._id} | Nome: {self._nome} | Saldo: {self._saldo}"
    
    
    @staticmethod
    def validar_nome(nome: str) -> bool:
        """
        Valida a se o nome tem mais de 5 caracteres

        Args:
            nome: O nome do usuário (str)

        Returns:
            True: se o nome tiver mais de 5 caracteres (bool)
            False: se o nome não tiver mais de 5 caracteres (bool)
        """

        if len(nome) > 5:
            return True
        
        return False

    def simular_deposito(self, valor_a_depositar: float) -> float:
        """
        Simula um depósito bancário

        Args:
            self: a prória instância 
            valor_a_depositar: valor a ser depositado (float)

        Retuns:
            Novo saldo da conta do cliente

        Raises:
            ValueError: Se o valor a ser depositado for menor que 0.        
        """

        if valor_a_depositar < 0:
            raise ValueError(f"Depósitos negativos não são permitidos")
        
        return self._saldo + valor_a_depositar