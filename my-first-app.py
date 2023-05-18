import streamlit as st
import pandas as pd
import numpy as np

st.title('my first app')

x = st.slider('Select a value')
st.write(x, 'squared is', x * x)
