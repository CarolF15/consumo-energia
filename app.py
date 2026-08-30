"""
Calculadora de Consumo Elétrico Inteligente
Arquivo: app.py
Pasta: projetos/consumo-energia
"""

# Entrada de dados
nome_aparelho = input("Digite o nome do aparelho (ex.: Geladeira): ")
potencia = float(input("Digite a potência do aparelho em watts (W): "))
horas_dia = float(input("Digite o tempo médio de uso diário em horas: "))

# Validação com estrutura de decisão
if potencia <= 0 or horas_dia <= 0:
    print("\nA potência e as horas devem ser maiores que zero.")
elif horas_dia > 24:
    print("\nO tempo de uso diário não pode exceder 24 horas.")
else:
    # Processamento (Fórmula da atividade)
    consumo_mensal = (potencia * horas_dia * 30) / 1000
    custo_estimado = consumo_mensal * 0.75

    print("\n-----------------------------------")
    print(f"Aparelho: {nome_aparelho}")
    print(f"Consumo estimado: {consumo_mensal:.2f} kWh/mês")
    print(f"Custo estimado: R$ {custo_estimado:.2f}/mês")
    print("-----------------------------------")