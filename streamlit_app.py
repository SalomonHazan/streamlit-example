import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import matplotlib as pl

st.title('Machine Learning... The Streamlit Way')

st.write("""
# Explorer différents modeles de classification
Quel est le meilleur modèle ?
""")

dataset_name=st.sidebar.selectbox("Selectionner un Dataset",("Iris", "Breast Cancer", "Wine dataset"))
st.write(dataset_name)

classifier=st.sidebar.selectbox("Selectionner un modèle de classification",("KNN", "SVM", "Random Forest"))



	     
