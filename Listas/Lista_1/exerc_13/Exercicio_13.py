# 13. Detector de Pico de Pressão: Um sensor envia um dado. O sistema deve
# exibir "PERIGO" se o valor for estritamente maior que 100, e "OK" caso contrário.
# Proibido usar if.
# ● A tarefa: O sensor às vezes envia o valor como string e às vezes como float.
# O sistema deve saber lidar com ambos.
# ● Além disso, se o dado vier vazio (""), o sistema deve exibir "ERRO DE
# SENSOR" em vez de quebrar.
# ● O Desafio: Resolva usando só expressões lógicas que tratem o valor vazio
# antes de tentar converter para número (para evitar que o programa trave).
# ● Imprima (no final) algo como “Status do Sistema:” + o status devido.

dado = input("Digite o dado no sensor: ")

status = (dado == "" and "ERRO DE SENSOR") or (float(dado) > 100 and "PERIGO") or "OK"

print("\n")
print("_" *30)
input(f"Status do sistema: {status}")
print("_" *30)