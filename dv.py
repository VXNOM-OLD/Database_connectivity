import pandas as pd
import streamlit as st
df =pd.Dataframe=(
{
    'Sr.no':[1,2,3,4,5],
    'Gender':['M','F','F','M','M'],
    'Weight':[50,55,60,70,75],
    'Height':[3.5,5.7,5.8,5.9,6.2],
    'BMI':[35,45,55,66,75]
})
st.table(df)
st.line_chart(df['Weight'])