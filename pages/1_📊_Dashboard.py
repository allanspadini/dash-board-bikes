import streamlit as st
import pandas as pd

def main():
    st.set_page_config(
        page_title="EcoBike",
        page_icon="🚲",
        layout='wide'
    )

    df = pd.read_csv()

    # Criar colunas
    col1, col2, col3 = st.columns([0.33, 0.33, 0.33])

    with col1:
        
        st.image('assets/bike_neon.png', width=150)  # Ajuste o tamanho da imagem conforme necessário
        

    with col2:
        
        st.metric(label="Média de bicicletas por dia", value="2.5", delta="-1,2")

    with col3:
        st.markdown("## EcoBike")

if __name__ == "__main__":
    main()
