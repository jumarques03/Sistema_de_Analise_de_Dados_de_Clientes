from modulos.Cliente import Cliente
from typing import Iterable

def is_cliente_rico(objeto: Cliente) -> bool:
    """
    Verifica se o cliente é rico

    Args:
        objeto: uma instância do tipo Cliente (Cliente)
    
    Returns:
        True: Se o saldo do cliente for mair ou igual a 500.000
        False: Se o saldo do cliente for menor que 500.000
    """

    if objeto._saldo > 500000:
        return True
    
    return False

def calcular_media_saldos(objeto: Iterable[Cliente]) -> float:
    """
    Calcula a média dos saldos de todos os clientes presentes no iterável

    Args:
        objeto: uma lista de objetos tipo Cliente (Cliente)

    Returns:
        A média dos saldos de todos os clientes (float)
    """
    soma_saldos_clientes =  sum(cliente._saldo for cliente in objeto)
    return  soma_saldos_clientes / len(objeto)

def gerar_nomes_clientes(objeto: Iterable[Cliente]):
    """
    Exibe o atributo nome de cada cliente, um por um

    Args:
        objeto: uma lista de objetos tipo Cliente (Cliente)
    
    Returns:
        O nome de cada cliente, um por um utilizando yield

    """
    for cliente in objeto:
        yield cliente._nome

