import streamlit as st
import pandas as pd
from sklearn import datasets
import matplotlib as pl
import numpy as np

st.title('Machine Learning... The Streamlit Way')

st.write("""
# Explorer différents modeles de classification
Quel est le meilleur modèle ?
""")

dataset_name=st.sidebar.selectbox("Selectionner un Dataset",("Iris", "Breast Cancer", "Wine dataset"))
st.write(dataset_name)

classifier_name=st.sidebar.selectbox("Selectionner un modèle de classification",("KNN", "SVM", "Random Forest"))

def get_dataset(dataset_name):
	if dataset_name=="Iris":
		data=datasets.load_iris()
	elif dataset_name=="Breast Cancer":
		data=datasets.load_breast_cancer()
	else:
		data=datasets.load_wine()
	X=data.data
	y=data.target
	return X, y

X, y=get_dataset(dataset_name)
st.write("shape of dataset",X.shape)
st.write("Number of classes", len(np.unique(y)))

def add_parameter_ui(clf_name):
	params=dict()
	if clf_name=="KNN":
		K=st.sidebar.slider("K",1,15)
		params["K"]=K
	elif clf_name=="SVM":
		C=st.sidebar.slider("C",0.01,10.0)
		params["C"]=C
	else:
		max_depth=st.sidebar.slider("max_depth",2,15)
		n_estimators=st.sidebar.slider("n_estimators",1,100)
	return params

add_parameter_ui(classifier_name)
	     
