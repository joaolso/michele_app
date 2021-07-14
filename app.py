from multiapp import MultiApp
from pages import load, shap_process, exploratory  # import your app modules here
from function import *
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import streamlit as st

st.set_page_config(
    page_title="App",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded",
)

PAGES = {
    "Inserção de Dados": load,
    "SHAP": shap_process,
    # "Exploratory": exploratory,
}


def main():

    st.sidebar.markdown("## Menu")
    selection = st.sidebar.radio("", list(PAGES.keys()))

    page = PAGES[selection]
    page.app()

    st.sidebar.markdown("## Release")
    st.sidebar.info(
        "Aplicação para identificação de atributos relevantes em dados educacionais"
    )
    st.sidebar.markdown("## Versão 1.0.0")
    st.sidebar.info(
        """ This app is maintained by """
    )


if __name__ == "__main__":
    main()
