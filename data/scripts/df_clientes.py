import pandas as pd
import numpy as np
import os
from datetime import datetime, timedelta

# Configuração para reprodutibilidade
np.random.seed(42)

n_clientes = 500

# Listas para simular dados brasileiros
nomes_base = ["Ana", "Bruno", "Carla", "Diego", "Elena", "Fabio", "Gisele", "Hugo", "Iara", "João"]
sobrenomes_base = ["Silva", "Santos", "Oliveira", "Souza", "Pereira", "Costa", "Ferreira", "Rodrigues"]
estados = ["SP", "RJ", "MG", "PR", "SC", "RS", "BA", "GO"]

clientes_data = []

for i in range(n_clientes):
    cliente_id = f"CUST-{1000 + i}"
    nome_completo = f"{np.random.choice(nomes_base)} {np.random.choice(sobrenomes_base)}"
    genero = np.random.choice(['F', 'M', 'Outro'], p=[0.48, 0.48, 0.04])
    
    # Data de nascimento (idades entre 18 e 70 anos)
    anos_atras = np.random.randint(18, 70)
    data_nasc = datetime(2026, 1, 1) - timedelta(days=anos_atras*365 + np.random.randint(0, 365))
    
    # Data de cadastro (entre 2023 e 2026)
    data_cadastro = datetime(2023, 1, 1) + timedelta(days=np.random.randint(0, 1000))
    
    estado = np.random.choice(estados)
    
    clientes_data.append([
        cliente_id, nome_completo, genero, 
        data_nasc.strftime('%Y-%m-%d'), 
        data_cadastro.strftime('%Y-%m-%d'), 
        estado
    ])

df_clientes = pd.DataFrame(clientes_data, columns=[
    'cliente_id', 'nome', 'genero', 'data_nascimento', 'data_cadastro', 'estado'
])

# Salva na pasta data
output_path = os.path.join('..', 'df_clientes.csv')
df_clientes.to_csv(output_path, index=False)

print(f"✅ Tabela de Clientes gerada em: {output_path}")
print(df_clientes.head())