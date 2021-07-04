import numpy as np
import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

#import modules
from function import *

# Globals
DATA_PATH = 'data/dados.csv'

st.title('Dados Discentes')

#Load Data
data = load_data(DATA_PATH)
st.markdown('### Raw Data')
st.dataframe(data.head().astype('object'))

data = transform_data(data)

data_train = data_train_generate(data)
st.markdown('### Transformed Data')
st.dataframe(data_train.head().astype('object'))

# Instantiating the SHAP explainer using our trained RFC model
st.markdown('### SHAP in Streamlit')
train_and_SHAP(data_train)