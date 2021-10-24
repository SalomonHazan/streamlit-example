import streamlit as st
import pandas as pd
pip install scikit-learn
pip install matplotlib

st.title('Machine Learning... The Streamlit Way')

st.write("""
# Explorer différents Classifier
""")

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/weather2019.csv"
df_weather = pd.read_csv(link)
df_weather
#st.dataframe(df_weather, 1000, 200)
st.line_chart(df_weather['MAX_TEMPERATURE_C'])

import seaborn as sns
viz_correlation = sns.heatmap(df_weather.corr(), center=0, cmap = sns.color_palette("vlag", as_cmap=True)
								)
st.pyplot(viz_correlation.figure)

name = st.text_input("Please give me your name :")
name_length = len(name)
st.write("Your name has ",name_length,"characters")

code = '''def hello():
   print("Hello, Streamlit!")'''
st.code(code, language='python')

st.dataframe(df_weather.style.highlight_max(axis=0))

st.metric(label="CA", value="23 K-Eur", delta="1.2 K-Eur")

col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")


st.json({    'foo': 'bar','baz': 'boz','stuff': [
         'stuff 1',
         'stuff 2',
         'stuff 3',
         'stuff 5',
     ],
 })


df2=df_weather.iloc[:,[1,2]]
st.line_chart(df2)
st.line_chart(df_weather.MAX_TEMPERATURE_C)

import numpy as np

df = pd.DataFrame(
     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
     columns=['lat', 'lon'])
df_weather	
st.map(df)


