import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, roc_curve, auc
from sklearn.preprocessing import LabelEncoder

# Função para carregar dados
@st.cache_data
def carregar_dados():
    df = pd.read_excel(
        r"C:\Users\USER\Documents\Projetos_Churn\bra_telecom_dashboard\data\bra_telecom_churn_enriquecido_padronizado.xlsx"
    )
    return df

# Carregar dados
df = carregar_dados()

# Pré-processamento
df = df.dropna()  # Remove valores nulos
df['churn'] = df['churn'].astype(int)

# Codificação de variáveis categóricas
label_encoder = LabelEncoder()
df['Plano'] = label_encoder.fit_transform(df['Plano'])
df['Regiao'] = label_encoder.fit_transform(df['Regiao'])
df['tipo_contrato'] = label_encoder.fit_transform(df['tipo_contrato'])

# Seleção das variáveis independentes (features) e dependente (target)
X = df[['idade', 'Tempo_com_Operadora', 'Uso_de_Dados', 'Plano', 'Renda', 'Reclamacoes', 'Satisfacao', 'Ultimo_Contato_Suporte']]
y = df['churn']

# Divisão dos dados em treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Treinamento do modelo Random Forest
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

# Previsões
y_pred = rf.predict(X_test)

# Avaliação do modelo
classification_rep = classification_report(y_test, y_pred)
fpr, tpr, thresholds = roc_curve(y_test, rf.predict_proba(X_test)[:, 1])
roc_auc = auc(fpr, tpr)

# Exibindo as métricas no Streamlit
st.subheader("📈 Relatório de Desempenho do Modelo")
st.text(f"Relatório de Classificação:\n{classification_rep}")
st.text(f"AUC: {roc_auc:.2f}")

# Exibindo a Curva ROC
st.subheader("📊 Curva ROC")
fig, ax = plt.subplots()
ax.plot(fpr, tpr, color='blue', label=f'AUC = {roc_auc:.2f}')
ax.plot([0, 1], [0, 1], color='gray', linestyle='--')
ax.set_xlabel('Taxa de Falsos Positivos')
ax.set_ylabel('Taxa de Verdadeiros Positivos')
ax.set_title('Curva ROC')
ax.legend(loc='lower right')
st.pyplot(fig)

# Previsão para novos dados
st.subheader("📝 Previsão para Novo Cliente")
novo_cliente = {
    'idade': st.slider('Idade', 18, 100, 30),
    'Tempo_com_Operadora': st.slider('Tempo com Operadora (meses)', 1, 100, 24),
    'Uso_de_Dados': st.slider('Uso de Dados (MB)', 0, 10000, 500),
    'Plano': st.selectbox('Plano', label_encoder.classes_),
    'Renda': st.slider('Renda Mensal (R$)', 1000, 10000, 3000),
    'Reclamacoes': st.slider('Número de Reclamações', 0, 10, 0),
    'Satisfacao': st.slider('Satisfação (0-10)', 0, 10, 5),
    'Ultimo_Contato_Suporte': st.slider('Último Contato com Suporte (meses)', 0, 12, 6)
}

# Codificando as variáveis categóricas para o novo cliente
novo_cliente_df = pd.DataFrame([novo_cliente])

# Codificando o plano
novo_cliente_df['Plano'] = label_encoder.transform(novo_cliente_df['Plano'])

# Fazendo a previsão
churn_probabilidade = rf.predict_proba(novo_cliente_df)[:, 1]
churn_probabilidade = round(churn_probabilidade[0], 2)

# Exibindo a previsão de churn
st.write(f"A probabilidade de churn para este cliente é: {churn_probabilidade * 100}%")

# Exibindo a recomendação com base na previsão
if churn_probabilidade > 0.5:
    st.write("Recomendação: Este cliente tem uma alta probabilidade de churn. Considere ações para retenção, como descontos ou upgrades.")
else:
    st.write("Recomendação: Este cliente tem uma baixa probabilidade de churn. Mantenha o acompanhamento habitual.")
