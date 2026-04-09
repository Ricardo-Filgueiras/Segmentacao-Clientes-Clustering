# 🎯 Segmentação de Clientes: Do Registro Bruto à Inteligência de Personas

[![Python](https://img.shields.io/badge/Python-3.10-blue)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange)](https://scikit-learn.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-lightgrey)](https://pandas.pydata.org/)
[![Status](https://img.shields.io/badge/Status-Concluído-green)](#)

## 📖 A História do Projeto
No varejo moderno, dados são abundantes, mas o conhecimento é escasso. Tratar cada cliente como um número médio em uma planilha é um erro estratégico que corrói a margem de lucro e ignora o comportamento humano.

Este projeto não é apenas uma aplicação de algoritmos; é um **framework de descoberta**. Através de uma jornada em 4 capítulos (notebooks), transformamos registros anônimos de vendas em histórias de consumidores reais, permitindo que o time de marketing pare de "atirar para todos os lados" e passe a agir com precisão cirúrgica.

---

## 🚀 A Jornada Analítica (Storytelling)

### 🧱 Capítulo 1: O Alicerce (ETL & Engenharia)
Nesta fase, focamos em dar contexto aos dados. Unificamos tabelas isoladas de Produtos, Clientes e Vendas para criar um "Dataset Mestre". 
- **O que fizemos:** Criamos variáveis como *Idade do Cliente*, *Tempo de Casa (Tenure)* e *Sensibilidade Promocional*.
- **Insight:** Transformar IDs anônimos em perfis enriquecidos com localização e preferências de categoria.

### 📊 Capítulo 2: A Métrica de Ouro (RFM)
Aqui, traduzimos comportamento em números comparáveis através da metodologia **RFM**:
- **Recência (R):** Há quanto tempo ele não aparece?
- **Frequência (F):** Com que constância ele confia na marca?
- **Valor Monetário (M):** Qual o retorno financeiro total?
- **O que fizemos:** Tratamento agressivo de *Outliers* (removendo "baleias" que distorciam a média) e normalização de escalas via `StandardScaler`.

### 🧠 Capítulo 3: O Nascimento das Personas (Clustering)
Utilizando o algoritmo **K-Means** e o *Método do Cotovelo*, identificamos os agrupamentos naturais da base.
- **O que fizemos:** Definimos 3 grupos estratégicos (Campeões, Potenciais e Hibernando).
- **Insight:** Verificamos que os números contam uma história de engajamento que vai muito além do simples "gastou muito".

### 🧪 Capítulo 4: Além do Financeiro (Spinoff Experimental)
Expandimos a visão para incluir dados **Psicográficos**.
- **O que fizemos:** Adicionamos *Idade* e *Sensibilidade a Descontos* ao modelo.
- **Descoberta:** Identificamos o "VIP Sensível" — clientes que gastam muito, mas exigem mimos exclusivos para manter a fidelidade.

---

## 👥 Meet the Personas: Matriz de Ação

| Persona | Gatilho de Negócio | Ação Recomendada | Canal de Comunicação |
| :--- | :--- | :--- | :--- |
| **🥇 Campeões (VIPs)** | Valor Monetário Alto + Recência Baixa | Programa de Fidelidade e Acesso Antecipado. | WhatsApp VIP / Concierge |
| **🚀 Potenciais** | Frequência em crescimento + Recência Baixa | Cupom para 2ª/3ª compra e Cross-sell. | Notificação Push / E-mail |
| **💤 Hibernando** | Recência aumentando (>30 dias) | Campanha "Sentimos sua falta" com desconto agressivo. | E-mail Marketing / SMS |

---

## 🛠️ Stack Tecnológica

- **Linguagem:** Python 3.10
- **Análise de Dados:** Pandas, NumPy
- **Machine Learning:** Scikit-Learn (K-Means, StandardScaler)
- **Visualização:** Matplotlib, Seaborn, Plotly Express (Visualização 3D)

---

## ⚙️ Como Executar

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/Ricardo-Filgueiras/Segmentacao-Clientes-Clustering.git
   ```

2. **Prepare o ambiente:**
   ```bash
   python -m venv venv
   # No Windows:
   .\venv\Scripts\activate
   # No Linux/Mac:
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Siga a história:**
   Abra os notebooks na ordem numérica (`Notebook 01` ao `04`) para entender a evolução do raciocínio e da construção do modelo.

---
*Desenvolvido como um estudo de caso prático para Marketing Analytics e Data Science.*
