from modulos.Cliente import Cliente
from modulos.ClientePremium import ClientePremium

primeiro_cliente = Cliente(1,"Juliano Soares", 1550.40)

print(primeiro_cliente.validar_nome(primeiro_cliente._nome))

print(primeiro_cliente.simular_deposito(10))

print(primeiro_cliente)

cliente_premium = ClientePremium(1, "Francesco", 145000.00, 350000.00)

print(cliente_premium)

