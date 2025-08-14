import json
import pandas as pd

# Carregar o arquivo JSON
# Altere 'training_report.json' se o nome do arquivo for diferente
with open('training_report.json', 'r') as f:
    data = json.load(f)

# --- Criação das Tabelas ---

# 1. Tabela: Metadados e Configuração do Modelo
# Juntar os dicionários 'metadata' e 'model_configuration'
meta_data = {**data['metadata'], **data['model_configuration']}
df_meta = pd.DataFrame([meta_data]).T.rename(columns={0: 'Valor'})
df_meta.index.name = 'Campo'
df_meta.to_csv('tabela_metadados_modelo.csv')

# 2. Tabela: Informações do Conjunto de Dados
df_dataset = pd.DataFrame([data['dataset_info']]).T.rename(columns={0: 'Valor'})
df_dataset.index.name = 'Campo'
df_dataset.to_csv('tabela_dataset_info.csv')

# 3. Tabela: Configuração do Treinamento
df_training_config = pd.DataFrame([data['training_configuration']]).T.rename(columns={0: 'Valor'})
df_training_config.index.name = 'Campo'
df_training_config.to_csv('tabela_config_treinamento.csv')

# 4. Tabela: Histórico de Treinamento
# Esta é a tabela mais importante, contendo os dados por época
df_history = pd.DataFrame(data['training_history'])
df_history.to_csv('tabela_historico_treinamento.csv', index=False)

# 5. Tabela: Resultados Finais e Métricas de Teste
# Juntar os dicionários 'final_results', 'test_metrics' e 'improvement_summary'
final_results_combined = {
    **data['final_results'],
    **data['final_results']['test_metrics'],
    **data['final_results']['improvement_summary']
}
# Remover as chaves de dicionários aninhados para evitar redundância
final_results_combined.pop('test_metrics', None)
final_results_combined.pop('improvement_summary', None)
df_final_results = pd.DataFrame([final_results_combined]).T.rename(columns={0: 'Valor'})
df_final_results.index.name = 'Campo'
df_final_results.to_csv('tabela_resultados_finais.csv')

print("Todos os arquivos CSV foram gerados com sucesso!")