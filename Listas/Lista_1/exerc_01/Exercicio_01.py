# 01. Gestão de Estoque Crítico: Uma importadora de hardware precisa de um
# sistema de reposição inteligente. Receba a categoria (string) e a quantidade (int).
# ● Se a categoria for "Acessórios": Repor se estoque estiver menor que 15.
# ● Se a categoria for "Periférico": Repor se estoque estiver menor que 25.
# ● O Desafio: Se a categoria for qualquer outra, o estoque mínimo de
# segurança é sempre 10.
# ● Saída: Exiba "REPOSIÇÃO SOLICITADA" apenas se o estoque estiver abaixo
# do limite para a categoria específica. Caso contrário, exiba "ESTOQUE
# INTEGRAL".

categoria = input("Digite a categoria (Acessórios / Periférico / outra): ")
quantidade = int(input("Digite a quantidade: "))
 
if categoria == "Acessórios":
    limite = 15
elif categoria == "Periférico":
    limite = 25
else:    
    limite = 10

if quantidade < limite:
    print(f"REPOSIÇÃO SOLICITADA '(Quantidade: {quantidade})'")
else:
    print(f"ESTOQUE INTEGRAL '(Quantidade: {quantidade})'")