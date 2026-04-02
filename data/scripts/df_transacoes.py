import pandas as pd
import numpy as np
import os

# Configuração para reprodutibilidade
np.random.seed(42)

# Caminho dos arquivos dependentes
produtos_path = os.path.join('..', 'df_produtos.csv')
clientes_path = os.path.join('..', 'df_clientes.csv')

# Verifica se os arquivos base existem
if not os.path.exists(produtos_path) or not os.path.exists(clientes_path):
    print("❌ Erro: df_produtos.csv ou df_clientes.csv não encontrados. Execute df_products.py e df_clientes.py primeiro.")
    exit()

# Carrega dados base
df_produtos = pd.read_csv(produtos_path)
df_clientes = pd.read_csv(clientes_path)

transacoes_list = []
n_transacoes = 100

for i in range(n_transacoes):
    id_transacao = f"T{1000 + i}"
    cliente_id = df_clientes.sample(1).iloc[0]['cliente_id']
    
    # Simula comportamento de compra conjunta (Bundling)
    # Ex: Quem compra Caneta Pilot (101) tem 70% de chance de comprar Refil (301)
    if np.random.random() < 0.7:
        # Pega dados dos produtos específicos
        pilot = df_produtos[df_produtos['produto_id'] == 101].iloc[0]
        refil = df_produtos[df_produtos['produto_id'] == 301].iloc[0]
        
        transacoes_list.append([id_transacao, cliente_id, pilot['produto_id'], pilot['nome']])
        transacoes_list.append([id_transacao, cliente_id, refil['produto_id'], refil['nome']])
    else:
        # Compras aleatórias (1 a 3 itens)
        itens = df_produtos.sample(np.random.randint(1, 4))
        for _, item in itens.iterrows():
            transacoes_list.append([id_transacao, cliente_id, item['produto_id'], item['nome']])

df_transacoes = pd.DataFrame(transacoes_list, columns=['id_transacao', 'cliente_id', 'produto_id', 'nome_produto'])

# Salva na pasta data
output_path = os.path.join('..', 'df_transacoes.csv')
df_transacoes.to_csv(output_path, index=False)

print(f"✅ Tabela de Transações gerada em: {output_path}")
print(df_transacoes.head())