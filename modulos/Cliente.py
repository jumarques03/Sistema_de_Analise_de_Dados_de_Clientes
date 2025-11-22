class Cliente:
    def __init__(self, id:int, nome:str, saldo:float):
        self.id = id
        self.nome = nome
        self.saldo = saldo

    def __str__(self):
        return f"ID: {self.id} | Nome: {self.nome} | Saldo: {self.saldo}"
    
    
