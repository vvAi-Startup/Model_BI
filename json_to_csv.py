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
# Acessa diretamente o dicionário de métricas dentro de 'training_history'
df_history = pd.DataFrame(data['training_history'])
df_history.to_csv('tabela_historico_treinamento.csv', index=False, sep='|', decimal=',')

print("Gerado: tabela_historico_treinamento.csv")

# --- 2. Tabela: Metadados e Configuração do Modelo ---
# Achata os dicionários aninhados usando json_normalize
meta_data_combined = {**data['metadata'], **data['model_configuration']}
df_meta = pd.json_normalize(meta_data_combined)
df_meta.to_csv('tabela_metadata_modelo.csv', index=True, sep='|')

print("Gerado: tabela_metadata_modelo.csv")

# --- 3. Tabela: Informações do Dataset ---
# Achata o dicionário 'dataset_info'
df_dataset = pd.json_normalize(data['dataset_info'])
df_dataset.to_csv('tabela_dataset_info.csv', index=True, sep='|')

print("Gerado: tabela_dataset_info.csv")

# --- 4. Tabela: Configuração do Treinamento ---
# Usa json_normalize para achatar o dicionário 'training_configuration'
df_training_config = pd.json_normalize(data['training_configuration'])
df_training_config.to_csv('tabela_config_treinamento.csv', index=True, sep='|')

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
df_final_results.to_csv('tabela_resultados_finais.csv', index=True, sep='|', decimal=',')

print("Gerado: tabela_resultados_finais.csv")