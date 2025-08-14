import json
import pandas as pd

# Carregar o arquivo JSON
try:
    with open('training_report.json', 'r') as f:
        data = json.load(f)
except FileNotFoundError:
    print("Erro: Arquivo 'training_report.json' não encontrado. Verifique o caminho.")
    exit()

# --- 1. Tabela: Histórico de Treinamento ---
# A única seção que é uma lista de listas precisa de um tratamento especial.
# 'json_normalize' não funciona diretamente neste formato. A abordagem é manual, mas confiável.
df_history = pd.DataFrame(data['training_history'])
df_history.to_csv('tabela_historico_treinamento.csv', index=False)

print("Gerado: tabela_historico_treinamento.csv")

# --- 2. Tabela: Metadados e Configuração do Modelo ---
# Achata os dicionários aninhados usando json_normalize
# As chaves aninhadas serão combinadas com um ponto (ex: "metadata.model_name")
# Isso é mais confiável do que a abordagem anterior.
meta_data_combined = {**data['metadata'], **data['model_configuration']}
df_meta = pd.json_normalize(meta_data_combined)
# Transpõe para o formato de tabela de duas colunas, se preferir
# df_meta = df_meta.T.rename(columns={0: 'Valor'})
# df_meta.index.name = 'Campo'
df_meta.to_csv('tabela_metadados_modelo.csv', index=True)

print("Gerado: tabela_metadados_modelo.csv")

# --- 3. Tabela: Informações do Conjunto de Dados ---
# Usa json_normalize para achatar o dicionário 'dataset_info'
df_dataset = pd.json_normalize(data['dataset_info'])
# Transpõe para o formato de tabela de duas colunas
# df_dataset = df_dataset.T.rename(columns={0: 'Valor'})
# df_dataset.index.name = 'Campo'
df_dataset.to_csv('tabela_dataset_info.csv', index=True)

print("Gerado: tabela_dataset_info.csv")

# --- 4. Tabela: Configuração do Treinamento ---
# Usa json_normalize para achatar o dicionário 'training_configuration'
df_training_config = pd.json_normalize(data['training_configuration'])
# Transpõe para o formato de tabela de duas colunas
# df_training_config = df_training_config.T.rename(columns={0: 'Valor'})
# df_training_config.index.name = 'Campo'
df_training_config.to_csv('tabela_config_treinamento.csv', index=True)

print("Gerado: tabela_config_treinamento.csv")


# --- 5. Tabela: Resultados Finais e Métricas de Teste ---
# Combina os dicionários aninhados e normaliza em uma única tabela
final_results_combined = {
    **data['final_results'],
    **data['final_results']['test_metrics'],
    **data['final_results']['improvement_summary']
}
final_results_combined.pop('test_metrics', None)
final_results_combined.pop('improvement_summary', None)
df_final_results = pd.json_normalize(final_results_combined)
# Transpõe para o formato de tabela de duas colunas
# df_final_results = df_final_results.T.rename(columns={0: 'Valor'})
# df_final_results.index.name = 'Campo'
df_final_results.to_csv('tabela_resultados_finais.csv', index=True)

print("Gerado: tabela_resultados_finais.csv")

print("\nConclusão: Todos os arquivos CSV foram gerados com sucesso. Agora você pode importá-los para o Power BI como 'Text/CSV'.")