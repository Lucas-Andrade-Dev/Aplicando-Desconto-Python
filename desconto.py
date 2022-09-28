"""
Aplicando Desconto sobre o preço do produto

"""

print("Aplicando Desconto no produto")

valor = input("Valor do produto: R$ ")
porcentagem = input("Qual a porcentagem de desconto desejada? ")

desconto = (float(valor) * int(porcentagem)) / 100

preco = float(valor) - float(desconto)

print(
    f'Valor de R${float(valor):,.2f} teve um desconto de {porcentagem}% ficando R${desconto:,.2f}')

print(f'valor atual é de R${preco:,.2f}')
