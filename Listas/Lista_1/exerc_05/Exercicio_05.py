# 05. Validador de Identidade: Receba dois inputs de texto idênticos, um após o
# outro (ex: o usuário digita "ADM" duas vezes).
# ● Armazene em user1 e user2.
# ● Crie uma lógica que imprima "Mesmo Valor" se o conteúdo das variáveis for
# igual, mas imprima "Objetos Diferentes no Heap " se as variáveis têm
# endereços distintos na memória.

user1 = input("Digite um valor1: ")
user2 = input("Digite um valor2: ")

if user1 == user2:
    print(f"Mesmo Valor (id1={id(user1)}, id2={id(user2)})")

if user1 is not user2:
    print(f"Objetos Diferentes no Heap (id1={id(user1)}, id2={id(user2)})")