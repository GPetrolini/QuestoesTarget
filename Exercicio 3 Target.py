import json

# Supondo que os dados estejam em um arquivo JSON
with open('faturamento.json') as f:
    faturamento = json.load(f)

# Filtrando os dias com faturamento válido (não nulo)
faturamento_valido = [dia for dia in faturamento if dia > 0]

# Calculando o menor e maior faturamento
menor_faturamento = min(faturamento_valido)
maior_faturamento = max(faturamento_valido)

# Calculando a média mensal
media_mensal = sum(faturamento_valido) / len(faturamento_valido)

# Contando os dias com faturamento acima da média
dias_acima_da_media = sum(1 for dia in faturamento_valido if dia > media_mensal)

print(f"Menor faturamento: {menor_faturamento}")
print(f"Maior faturamento: {maior_faturamento}")
print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")