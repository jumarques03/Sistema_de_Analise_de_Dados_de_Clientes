from modulos.Cliente import Cliente
from modulos.ClientePremium import ClientePremium
def is_cliente_rico(objeto: Cliente) -> bool:
    """
    Verifica se o cliente é rico

    Args:
        objeto: uma instância do tipo Cliente
    
    Returns:
        True: Se o saldo do cliente for mair ou igual a 500.000
        False: Se o saldo do cliente for menor que 500.000
    """

    if objeto._saldo > 500000:
        return True
    
    return False