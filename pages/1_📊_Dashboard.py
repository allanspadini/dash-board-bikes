import streamlit as st
import pandas as pd
import plotly.express as px

def main():
    st.set_page_config(
        page_title="EcoBike",
        page_icon="🚲",
        layout='wide'
    )

    df = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vQ5ZO92AUBmD4zNMEWanOlDoso-6xkehUdDh0Ntw1ce0if_oOoEs85RD9GtZ787y7z6n08Zjx8GhxXC/pub?output=csv')

    # Criar colunas
    col1, col2, col3, col4 = st.columns([0.25, 0.25, 0.25,0.25])

    with col1:
        
        st.image('assets/bike_neon.png', width=150)  # Ajuste o tamanho da imagem conforme necessário

        
        

    with col2:
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df['month'] = df['timestamp'].dt.month
        total_bicicletas_por_mes = df.groupby('month')['cnt'].sum()
        # Reset the index, rename the column and sort by month
        total_bicicletas_por_mes = total_bicicletas_por_mes.reset_index().rename(columns={'cnt': 'total_bicicletas'}).sort_values('month')

        # Extraia o ano da coluna timestamp e armazene em uma nova coluna chamada year
        df['year'] = df['timestamp'].dt.year

        # Obtenha o valor de month da última linha
        ultimo_mes = df['month'].iloc[-1]

        # Obtenha o valor de year da última linha
        ultimo_ano = df['year'].iloc[-1]

        # Filtre o dataframe para o último ano e último mês
        df_ultimo_mes_ano = df[(df['year'] == ultimo_ano) & (df['month'] == ultimo_mes)]

        # Calcule a soma da coluna cnt no dataframe filtrado
        total_bicicletas_ultimo_mes_ano = df_ultimo_mes_ano['cnt'].sum()

        # Filtre o dataframe para o último ano e último mês
        df_ultimo_mes_ano = df[(df['year'] == ultimo_ano) & (df['month'] == ultimo_mes)]

        # Calcule a soma da coluna cnt no dataframe filtrado
        total_bicicletas_ultimo_mes_ano = df_ultimo_mes_ano['cnt'].sum()
        delta=int(total_bicicletas_ultimo_mes_ano)-int(total_bicicletas_por_mes['total_bicicletas'].mean())
        st.metric(label="Média de bicicletas por mês", value=int(total_bicicletas_por_mes['total_bicicletas'].mean()),delta=delta)

    with col3:
        st.metric(label="Desvio padrão", value=int(df['cnt'].std()))
        
    with col4:
        st.metric(label="Maior número de bicicletas em um dia ", value=int(df['cnt'].max()))

    fig = px.bar(df, x='month', y='cnt',
             title='Bicicletas Alugadas por Mês',
             color_discrete_sequence=['#7CCD7C'])#labels={'is_holiday': 'Feriado', 'total_bicicletas': 'Total de Bicicletas'}
    st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    main()
