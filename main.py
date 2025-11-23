from modulos.Cliente import Cliente
from modulos.ClientePremium import ClientePremium
from funcoes_puras import gerar_nomes_clientes

primeiro_cliente = Cliente(1,"Juliano Soares", 1550.40)

print(primeiro_cliente.validar_nome(primeiro_cliente._nome))

print(primeiro_cliente.simular_deposito(10))

print(primeiro_cliente)

cliente_premium = ClientePremium(1, "Francesco", 145000.00, 350000.00)

print(cliente_premium)

lista_clientes = [
    Cliente(1,"Juliano Soares", 1550.40),
    Cliente(2,"Bethania", 2550.40),
    Cliente(3,"Amanda", 3550.40)
]

for nome in gerar_nomes_clientes(lista_clientes):
    print(nome)
