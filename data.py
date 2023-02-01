import streamlit as st
import pandas as pd
import numpy as np
import time

a = [i for i in range(10)]
# print(a)
st.dataframe(a)
st.table(a)
st.write(a)

arr1 = np.array(a)
# print(arr1)
st.dataframe(arr1)
st.table(arr1)
st.write(arr1)

arr2 = arr1.reshape((2,5))
# print(arr2)
st.dataframe(arr2)
st.table(arr2)
st.write(arr2)

d = {'Name':['Mohit','Patil'],
     'Age': [26,26],
     'City':['Dhule', 'India']}

st.dataframe(d)
st.table(d)
st.json(d)
st.write(d)

df = pd.read_csv('Salary_Data.csv')

# print(df)
st.dataframe(df, width=500, height=1000)
st.table(df)
st.write(df)

# cache in streamlit


# everytime we refresh the page the whole script gets executed from top to bottom
# if we have large amount of dataset or heavy computation program which need to be loaded everytime 
# them it will take more time to load
# this problem can be sloved using cache

# @st.cache

# def ret_time(a):
#     time.sleep(5)
#     return time.time()

# if st.checkbox('1'):
#     st.write(ret_time(1))

# if st.checkbox('2'):
#     st.write(ret_time(2))

@st.cache
def ret_time(a):
    time.sleep(5)
    return time.time()

if st.checkbox("1"):
    st.write(ret_time(1))

if st.checkbox("2"):
    st.write(ret_time(2))