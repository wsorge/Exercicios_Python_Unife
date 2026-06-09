# 06. Calculadora de Frete: Receba o valor_venda e a regiao (1-Sul, 2-Norte,
# 3-Oeste).
# ● Se Região for 1: Frete Grátis se Venda > 100.
# ● Se Região for 2: Frete Grátis se Venda > 250.
# ● Se Região for 3: Sempre paga frete de 50 reais.
# Usar ferramentas aprendidas em aula (match-case é obrigatório aqui).

valor_venda = float(input("Digite o valor da venda: "))

print("_" * 35)
print("\n1 para Região Sul\n"
      "2 para Região Norte\n"
      "3 para Região Oeste")
print("_" * 35 + "\n")

regiao = int(input("Digite a região (1-Sul, 2-Norte, 3-Oeste): "))
 
match regiao:
    case 1:
        if valor_venda > 100:
            print("Frete Grátis!")
        else:
            print("Frete cobrado!")
    case 2:
        if valor_venda > 250:
            print("Frete Grátis!")
        else:
            print("Frete cobrado!")
    case 3:
        print("Frete: R$ 50,00")
    case _:
        print("Região inválida.")
