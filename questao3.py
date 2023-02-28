import requests
import json

# faz o download do arquivo JSON
url = 'https://drive.google.com/u/0/uc?id=1qXvCPjEL4jerElN-hnScoKkEVmSQ8A2L&export=download'
response = requests.get(url)
data = response.json()

# cria uma lista com os valores de faturamento diário, desconsiderando os dias com valores iguais a 0.0
faturamento_diario = []
for item in data:
    valor = item['valor']
    if valor > 0.0:
        faturamento_diario.append(valor)

# calcula o menor valor de faturamento
menor_valor = min(faturamento_diario)

# calcula o maior valor de faturamento
maior_valor = max(faturamento_diario)

# calcula a média mensal de faturamento, desconsiderando os dias com valores iguais a 0.0
dias_validos = len(faturamento_diario)
media_mensal = sum(faturamento_diario) / dias_validos

# calcula o número de dias em que o valor de faturamento diário foi superior à média mensal
dias_acima_da_media = sum(
    1 for valor in faturamento_diario if valor > media_mensal)

# exibe os resultados
print(f"Menor valor de faturamento: R${menor_valor:.2f}")
print(f"Maior valor de faturamento: R${maior_valor:.2f}")
print(f"Número de dias acima da média mensal: {dias_acima_da_media}")
