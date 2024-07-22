import streamlit as st


def main():
    dashboard_page = st.Page("create.py", title="Create entry", icon=":material/add_circle:")
    previsao_page = st.Page("delete.py", title="Delete entry", icon=":material/delete:")

if __name__ == "__main__":
    main()