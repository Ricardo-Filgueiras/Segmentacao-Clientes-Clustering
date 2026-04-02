import pandas as pd
import numpy as np
import os

# Configuração para reprodutibilidade
np.random.seed(42)

# Mock de dados para simular uma papelaria técnica/escritório
produtos_data = [
    [101, "Caneta Gel Pilot G2 Preta", "Escrita", "Caneta Gel", "Pilot", "Ponta 0.7mm, escrita macia, recarregável", 15.90],
    [102, "Caneta Gel Uni-ball Signo", "Escrita", "Caneta Gel", "Uni-ball", "Ponta 0.5mm, secagem rápida, azul", 14.50],
    [103, "Caneta Esferográfica Bic Cristal", "Escrita", "Caneta Esferográfica", "Bic", "Ponta média, clássica, azul", 2.50],
    [201, "Caderno Moleskine Classic", "Papelaria", "Cadernos", "Moleskine", "Capa dura, 192 páginas, pautado", 120.00],
    [202, "Caderno Cícero Pontado", "Papelaria", "Cadernos", "Cícero", "Capa flexível, papel pólen, 160 páginas", 89.00],
    [301, "Refil Caneta Gel Pilot", "Escrita", "Refil", "Pilot", "Carga para G2, preta", 9.00]
]

df_produtos = pd.DataFrame(produtos_data, columns=[
    'produto_id', 'nome', 'categoria', 'subcategoria', 'marca', 'caracteristicas', 'custor'
])

# Salva na pasta data
output_path = os.path.join('..', 'df_produtos.csv')
df_produtos.to_csv(output_path, index=False)

print(f"✅ Tabela de Produtos gerada em: {output_path}")
print(df_produtos.head())