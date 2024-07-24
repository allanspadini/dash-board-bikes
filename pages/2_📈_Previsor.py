import streamlit as st
import joblib
import os
from prophet import Prophet


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
      fig = model.plot(forecast)
      st.pyplot(fig)

if __name__ == "__main__":
      main()