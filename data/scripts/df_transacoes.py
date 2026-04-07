import pandas as pd
import numpy as np
import os

# Configuração para reprodutibilidade
np.random.seed(42)

# Caminho dos arquivos dependentes (relativo ao script)
script_dir = os.path.dirname(os.path.abspath(__file__))
vendas_path = os.path.join(script_dir, '..', 'df_vendas.csv')
clientes_path = os.path.join(script_dir, '..', 'df_clientes.csv')
produtos_path = os.path.join(script_dir, '..', 'df_produtos.csv')

# Verifica se os arquivos base existem
if not os.path.exists(vendas_path) or not os.path.exists(clientes_path):
    print("❌ Erro: dfvendas.csv ou df_clientes.csv não encontrados. Execute df_vendas.py e df_clientes.py primeiro.")
    exit()

# Carrega dados base
df_vendas = pd.read_csv(vendas_path)
df_clientes = pd.read_csv(clientes_path)
df_produtos = pd.read_csv(produtos_path)

n_transacoes = 100
transacoes_list = []

for i in range(n_transacoes):
    id_transacao = f"T{1000 + i}"
    cliente_id = df_clientes.sample(1).iloc[0]['cliente_id']

    if np.random.random() < 0.7:
        pilot = df_produtos[df_produtos['produto_id'] == 101].iloc[0]
        refil = df_produtos[df_produtos['produto_id'] == 301].iloc[0]

        transacoes_list.append([id_transacao, cliente_id, pilot['produto_id'], pilot['nome']])
        transacoes_list.append([id_transacao, cliente_id, refil['produto_id'], refil['nome']])

df_transacoes = pd.DataFrame(
    transacoes_list,
    columns=['id_transacao', 'cliente_id', 'produto_id', 'nome']
)
# Salva na pasta data
output_path = os.path.join('data', 'df_transacoes.csv')
os.makedirs(os.path.dirname(output_path), exist_ok=True)
df_transacoes.to_csv(output_path, index=False)

print(f"✅ Tabela de Transações gerada em: {output_path}")
print(df_transacoes.head())