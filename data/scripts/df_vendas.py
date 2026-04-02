import pandas as pd
import numpy as np
import os
from datetime import datetime, timedelta

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

datas = [datetime(2026, 3, 1) + timedelta(days=x) for x in range(30)]
vendas_data = []

for data in datas:
    # Número aleatório de vendas por dia
    n_vendas_dia = np.random.randint(10, 50)
    
    for _ in range(n_vendas_dia):
        # Seleciona um cliente e um produto aleatório
        cliente = df_clientes.sample(1).iloc[0]
        produto = df_produtos.sample(1).iloc[0]
        
        # Lógica de preço com variação
        preco_base = produto['preco_base']
        preco_praticado = round(preco_base * np.random.uniform(0.9, 1.1), 2)
        
        # Simula contexto competitivo
        media_similares = round(preco_base * np.random.uniform(0.95, 1.05), 2)
        
        is_fds = 1 if data.weekday() >= 5 else 0
        qtd = np.random.randint(1, 5)
        
        # Simulação de estoque (entre 0 e 100)
        estoque = np.random.randint(0, 101)
        
        vendas_data.append([
            data.strftime('%Y-%m-%d'), 
            cliente['cliente_id'],
            produto['produto_id'], 
            qtd, 
            preco_praticado, 
            media_similares, 
            is_fds,
            estoque
        ])

df_vendas = pd.DataFrame(vendas_data, columns=[
    'data_venda', 'cliente_id', 'produto_id', 'qtd_vendida', 
    'preco_praticado', 'media_preco_similares', 'is_final_de_semana', 'estoque_disponivel'
])

# Salva na pasta data
output_path = os.path.join('..', 'df_vendas.csv')
df_vendas.to_csv(output_path, index=False)

print(f"✅ Tabela de Vendas e Estoque gerada em: {output_path}")
print(df_vendas.head())