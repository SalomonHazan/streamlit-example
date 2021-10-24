import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import matplotlib as pl

st.title('Machine Learning... The Streamlit Way')

st.write("""
# Explorer différents Classifier
Quel est le meilleur modèle ?
""")

st.selectbox("Selectionner un Dataset",("Iris", "Breast Cancer", "Wine dataset")
	     
