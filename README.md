# 🎯 Segmentação de Clientes com K-Means (Análise RFM)

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-lightgrey)
![Status](https://img.shields.io/badge/Status-Concluído-green)

## 1. O Problema de Negócio
No varejo competitivo, tratar todos os clientes da mesma forma é um desperdício de recursos de marketing. O objetivo deste projeto é identificar diferentes perfis de consumidores com base em seu histórico de compras, permitindo que o time de Marketing crie campanhas personalizadas e aumente o ROI (Retorno sobre Investimento).

**Pergunta respondida:** *Quem são os nossos clientes mais valiosos e quem está prestes a deixar de comprar conosco?*

## 2. A Solução (Abordagem Técnica)
Para resolver este problema, utilizei a metodologia **RFM** (Recência, Frequência e Valor Monetário) combinada com Aprendizado de Máquina Não Supervisionado:
* **Recência:** Quantos dias desde a última compra?
* **Frequência:** Quantas compras o cliente já fez?
* **Valor Monetário:** Quanto o cliente já gastou no total?

Após a engenharia de atributos, apliquei o algoritmo **K-Means** para encontrar agrupamentos matemáticos naturais na base de clientes.

## 3. Base de Dados
* **Origem:** Dados transacionais de e-commerce (ex: Kaggle - E-Commerce Retail Dataset).
* **Volume:** X.XXX registros de vendas cobrindo o período de [Mês/Ano] a [Mês/Ano].
* **Limpeza:** Remoção de valores nulos, tratamento de devoluções (valores negativos) e remoção de outliers extremos.

## 4. Resultados e Insights Gerados
O modelo identificou **4 clusters principais** de clientes. Abaixo, o perfil gerencial de cada um e a sugestão de ação:

| Cluster | Nome do Grupo | Características (RFM) | Estratégia de Negócio Recomendada |
| :---: | :--- | :--- | :--- |
| **0** | **Campeões (VIPs)** | Compram muito, gastam muito e compraram recentemente. | Oferecer acesso antecipado a novos produtos. Não dar descontos (eles já compram sem isso). |
| **1** | **Leais com Potencial** | Compram com boa frequência, mas ticket médio baixo. | Fazer campanhas de *Cross-sell* (oferecer produtos complementares). |
| **2** | **Atenção (Em Risco)** | Gastavam bem, mas não compram há muito tempo. | Enviar cupons de desconto agressivos para reativação. |
| **3** | **Dormentes/Perdidos** | Compraram uma vez há muito tempo e gastaram pouco. | Evitar gastos com marketing direto. Focar apenas em campanhas de massa. |

*(Adicione aqui uma imagem gerada pelo seu código, como um gráfico 3D dos clusters ou um Boxplot das variáveis RFM)*

## 5. Como Executar o Projeto
Instruções para clonar e rodar o projeto localmente.

```bash
# Clone o repositório
git clone https://github.com/Ricardo-Filgueiras/Segmentacao-Clientes-Clustering.git

# Entre no diretório
cd customer-segmentation-rfm

# Crie um ambiente virtual e instale as dependências
python -m venv venv
source venv/bin/activate  # Linux/Mac ou venv\Scripts\activate no Windows
pip install -r requirements.txt

# Execute o Jupyter Notebook
jupyter notebook
