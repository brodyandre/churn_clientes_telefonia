# Mas afinal o que é churn de clientes?

Churn é um termo em inglês que se refere à taxa de perda de clientes em uma empresa. Quando falamos de "churn de clientes", estamos nos referindo ao número de clientes que cancelam ou deixam de usar os serviços de uma empresa em um determinado período de tempo. Nesse projeto, desenvolvemos um dashboard dinamico com sliders, onde é possível configurarmos varios cenários. Cenários esses, em que o modelo consegue retornar uma probabilide de o churn acontecer para um determinado cliente que vc configurou movendo os sliders do dashboard...

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
- **Random Forest**: Previsão para o churn

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

## Na imagem abaixo podemos encontrar informações sobre a acurácia do modelo de previsão 
   ![Relatório de Desempenho do Modelo](https://github.com/brodyandre/churn_clientes_telefonia/blob/ea1ce08db50715cff63470be2832f5320bffeecf/Dashboard_churn_clientes/01_Relat%C3%B3rio%20de%20desempenho%20do%20modelo.png) 

## Na imagem abaixo podemos visualizar os sliders de configuração de valores para o modelo. Observe que o primeiro slider está configurado com a "Previsão para Novo Cliente Configurada em: 30 anos". E no rodapé da imagem o modelo exibe a previsão: "Probabilidade de churn para este cliente é de 19.0%"

Recomendação: Este cliente tem uma baixa probabilidade de chun. Mantenha o acompanhamento
   ![Relatório de Previsão para Novo CLiente](https://github.com/brodyandre/churn_clientes_telefonia/blob/d8a2a19a703dc73149ab1e1390eca2fc69d07750/Dashboard_churn_clientes/02_Dashboard_Previsao_para_novo_cliente_idade_30.png)


## Na imagem abaixo podemos visualizar os sliders de configuração de valores para o modelo. Observe que o primeiro slider agora foi movido para o valor "71" "Previsão para Novo Cliente Configurada em: 71 anos". E no rodapé da imagem o modelo exibe a previsão: "Probabilidade de churn para este cliente é de 39.0%"

Recomendação: Este cliente tem uma baixa probabilidade de chun. Mantenha o acompanhamento
   ![Relatório de Previsão para Novo CLiente](https://github.com/brodyandre/churn_clientes_telefonia/blob/f93267f49650167536ca017a98b28aaae7965f6e/Dashboard_churn_clientes/03_Dashboard_Previsao_para_novo_cliente_idade_71.png)


## Conclusões

Podemos mover os sliders e configurar infinitos cenários que o modelo de previsão exibirá uma probabilidade de churn. Facilitando a vida dos tomadores de decisão!!!


   

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

