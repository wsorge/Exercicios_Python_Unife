# 04. Simulador de Investimento com Aporte: Um acionista quer prever seu saldo. 
# Receba o valor_inicial e a taxa_rendimento (EM %).
# ● Ex: Se a taxa de rendimento digitada for 5, isso equivale a 5% (converta no código para que funcione).
# ● Se o rendimento final (Valor * Taxa) for um número par na sua parte inteira,
# o banco cobra uma taxa de custódia de R$ 10,00.
# ● Se for ímpar, a taxa é de R$ 5,00.
# ● Saída: Exiba o lucro líquido (Rendimento - Taxa) usando o tipo adequado.

from decimal import Decimal

valor_inicial = Decimal(input("Digite o valor inicial: "))
taxa_rendimento = Decimal(input("Digite a taxa de rendimento (%): "))

taxa_decimal = taxa_rendimento / 100
rendimento_final = valor_inicial * taxa_decimal
parte_inteira = int(rendimento_final)


if parte_inteira % 2 == 0:
    taxa_custodia = Decimal("10.00")
else:
    taxa_custodia = Decimal("5.00")

lucro_liquido = rendimento_final - taxa_custodia

print("-" *35)
print(f"Rendimento bruto: R$ {rendimento_final:.2f}")
print(f"Parte Inteira: {parte_inteira:.2f}")
print("-" *35)
print(f"Taxa de custódia: R$ {taxa_custodia:.2f}")
print(f"Lucro líquido: R$ {lucro_liquido:.2f}")
print("-" *35)