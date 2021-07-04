import streamlit as st

st.set_page_config(
        page_title="App",
        page_icon="📚",
        layout="wide",
        initial_sidebar_state="expanded",
    )

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#import modules
from function import *
from multiapp import MultiApp
from pages import shap, lime, exploratory # import your app modules here


PAGES = {
    "SHAP": shap,
    "LIME": lime,
    "Exploratory": exploratory,
}

def main():

    st.sidebar.markdown("## Menu")
    selection = st.sidebar.radio("", list(PAGES.keys()))

    page = PAGES[selection]
    page.app()

    st.sidebar.markdown("## Release")
    st.sidebar.info(
        "Aplicação de Desenvolvimento para identificação de atributos relevantes"
        " em dados estudantis"
    )
    st.sidebar.markdown("## Versão 1.0.0")
    st.sidebar.info(
        """ This app is maintained by """
    )


if __name__ == "__main__":
    main()