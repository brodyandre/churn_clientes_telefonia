# Previsão de Churn com Random Forest - BRA TeleCOM

Este projeto utiliza técnicas de Machine Learning para prever a probabilidade de churn de clientes da BRA TeleCOM. O modelo foi treinado com dados históricos de clientes e é baseado no algoritmo Random Forest. Através de uma interface interativa com **Streamlit**, é possível visualizar os resultados do modelo e fazer previsões para novos clientes.

## Objetivo

O objetivo principal deste projeto é prever se um cliente vai deixar a operadora (churn) com base em suas características e comportamento. O modelo utiliza o algoritmo **Random Forest** para fazer essas previsões. A interface é criada com **Streamlit**, permitindo uma interação simples e rápida.

## Funcionalidades

- **Relatório de Desempenho do Modelo**: Exibe as métricas de desempenho do modelo, como o **Relatório de Classificação** e o **AUC**.
- **Curva ROC**: Mostra a performance do modelo ao longo de diferentes limiares de classificação.
- **Previsão de Churn para Novo Cliente**: Permite que o usuário insira informações sobre um novo cliente e receba a probabilidade de churn.

## Tecnologias Utilizadas

- **Streamlit**: Framework para criação de aplicações web interativas
- **Scikit-learn**: Biblioteca de Machine Learning
- **Pandas**: Manipulação de dados
- **Matplotlib**: Visualização de gráficos

## 🚀 Ambiente Virtual

Crie um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv venv
```

### Ative o ambiente:

**No Windows:**
```bash
.\venv\Scripts\activate
```

**No Linux/macOS:**
```bash
source venv/bin/activate
```

## 📆 Instale as dependências

```bash
pip install -r requirements.txt
```

Se o arquivo `requirements.txt` não estiver disponível, instale manualmente:

```bash
pip install pandas streamlit scikit-learn matplotlib
```

## ▶️ Como Rodar

Execute a aplicação com Streamlit:

```bash
streamlit run dashboard/app.py
```

A aplicação abrirá automaticamente no navegador em:  
📍 [http://localhost:8501](http://localhost:8501)

## 📂 Estrutura do Projeto

```text
bra-telecom-churn/
│
├── dashboard/                        
│   └── app.py                  # Código principal do Streamlit
│
├── data/                             
│   └── bra_telecom_churn_enriquecido_padronizado.xlsx
│
├── requirements.txt            # Lista de dependências do projeto
└── README.md                   # Documentação
```

## 🧠 Detalhes do Modelo

O modelo de Machine Learning foi construído com o algoritmo **Random Forest**. Antes do treinamento, o conjunto de dados foi limpo e pré-processado, com codificação de variáveis categóricas e tratamento de valores nulos.

## 🔍 Variáveis Utilizadas

- **Idade**: Idade do cliente  
- **Tempo com a Operadora**: Meses desde o início do contrato  
- **Uso de Dados**: MB utilizados mensalmente  
- **Plano**: Tipo de plano contratado  
- **Renda**: Renda mensal do cliente (em R$)  
- **Reclamações**: Total de reclamações registradas  
- **Satisfação**: Nível de satisfação (0 a 10)  
- **Último Contato com Suporte**: Tempo desde o último atendimento  

## 🤝 Como Contribuir

1. Faça um fork deste repositório  
2. Crie uma branch para sua feature:
```bash
git checkout -b feature/nova-feature
```
3. Faça commit das suas alterações:
```bash
git commit -m "Adicionando nova feature"
```
4. Envie para o seu repositório:
```bash
git push origin feature/nova-feature
```
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença **MIT License**.

## 👤 Autor

**Luiz André**  
Abril 2025  
[LinkedIn](https://www.linkedin.com/) · [GitHub](https://github.com/brodyandre)

