# 07. Tentativas de login: Crie um programa com login_ativo = False. Use uma
# única linha de if com and. A primeira parte verifica login_ativo. A segunda parte
# deve ser uma operação que supostamente daria erro (10 / 0).
# O Desafio: Dentro de um print independente (abaixo do if), explique por que o
# programa não trava com execução da divisão por zero.

login_ativo = False

if login_ativo and (10 / 0):
    print("Login realizado!")


print("_" *50)
print("O programa não trava porque o operador 'and' utiliza avaliação de curto-circuito (short-circuit). Como 'login_ativo' é False, o Python já sabe que toda a condição será False e não precisa avaliar a segunda parte (10 / 0). Por isso, a divisão por zero nunca é executada.")
print("_" *50)