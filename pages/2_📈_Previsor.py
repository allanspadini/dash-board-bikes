import streamlit as st
import joblib
import os
from prophet import Prophet
from prophet.plot import plot_plotly


@st.cache_resource
def carrega_modelo():
      """
      A function that loads a serialized machine learning model from a file.

      Returns:
         The loaded machine learning model.

      """
      file_path = 'assets/modelo_prophet.pkl'
      if not os.path.exists(file_path):
            raise FileNotFoundError(f"Arquivo não encontrado: {file_path}")
      return joblib.load('assets/modelo_prophet.pkl')

def main():
      
      model = carrega_modelo()
      st.markdown('## Previsão de aluguéis')

      n_dias = st.number_input('Quantos dias deseja prever?', min_value=1, max_value=365, value=1, step=1)
      # Fazer previsões para datas futuras
      future = model.make_future_dataframe(periods=n_dias)
      forecast = model.predict(future)
      fig = plot_plotly(model,forecast)

      fig.update_layout({
        'plot_bgcolor': 'rgba(255, 255, 255, 1)',  # Define o fundo da área do gráfico como branco
        'paper_bgcolor': 'rgba(255, 255, 255, 1)', # Define o fundo externo ao gráfico como branco
        'title': {'text': "Quantidade", 'font': {'color': 'black'}},
        'xaxis': {'title': 'Data', 'title_font': {'color': 'black'}, 'tickfont': {'color': 'black'}},
        'yaxis': {'title': 'Bicicletas alugadas', 'title_font': {'color': 'black'}, 'tickfont': {'color': 'black'}}
      })
      st.plotly_chart(fig)

      tabela_previsao = forecast[['ds', 'yhat']].tail(n_dias)
      st.write('Tabela contendo as previsões de bicicletas alugadas para os próximos {} dias:'.format(n_dias))
      st.dataframe(tabela_previsao, height=300)

      # Permitindo o download da tabela
      csv = tabela_previsao.to_csv(index=False)
      st.download_button(label='Baixar tabela como csv', data=csv, file_name='previsao_ozonio.csv', mime='text/csv')

if __name__ == "__main__":
      main()