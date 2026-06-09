# 03. Decomposição de Tempo (Automação Industrial): Um sensor de esteira
# conta o tempo de operação em segundos. Receba um valor inteiro de segundos
# (ex: 10.000) e decomponha-o em Horas, Minutos e Segundos restantes.
# ● Exemplo: 3661 segundos = 1 Hora, 1 Minuto e 1 Segundo.
# ● Use ferramentas dadas em aulas até aqui. Não use funções prontas.

segundos_total = int(input("Digite o tempo em segundos: "))
 
horas = segundos_total // 3600
minutos_restantes = segundos_total % 3600
minutos = minutos_restantes // 60
segundos = minutos_restantes % 60

print("\n" + "-" * 25)
print(f"Resultado: Horas: {horas} | Minutos: {minutos} | Segundos: {segundos}")
print("-" *25 + "\n")
