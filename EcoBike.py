import streamlit as st


def main():
    
    st.set_page_config(
        page_title="EcoBike",
        page_icon="🚲",
        layout='wide'
    )

    st.markdown('''
                ## Dashboard EcoBike: Acompanhe e Planeje o Sucesso do Seu Negócio 🚴‍♀️🚴‍♂️

                Boas-vindas ao centro de controle da EcoBike! Aqui você encontra as ferramentas essenciais para impulsionar o seu serviço de aluguel de bicicletas. 🚲💨

                **Explore as opções:**

                * **Dashboard:** Mergulhe nos dados do seu negócio. 📊 Visualize o número de aluguéis, a receita gerada, os horários de pico e muito mais. Descubra insights valiosos para otimizar suas operações. 📈

                * **Previsão de Aluguéis:** Planeje o futuro com confiança. 🔮 Nossa ferramenta de previsão estima a demanda por bicicletas nos próximos dias, ajudando você a ajustar a disponibilidade da frota e maximizar seus lucros. 🚀

                **Importante:** Lembre-se que a precisão da previsão diminui à medida que aumenta o número de dias. 🗓️ Utilize as informações com sabedoria para tomar as melhores decisões para o seu negócio. 🤔

                **Pronto para começar?** Clique na opção desejada e explore o poder dos dados com a EcoBike! 💪
    ''')

if __name__ == "__main__":
    main()