# Importing required libraries
import streamlit as st
import pandas as pd 
from matplotlib import pyplot as plt
from plotly import graph_objs as go
from sklearn.linear_model import LinearRegression
import numpy as np
from PIL import Image

# Load ypur dataset
df = pd.read_csv('Salary_Data.csv')


# Linear regression model

x = np.array(df['YearsExperience']).reshape(-1,1)
lr_model = LinearRegression()
lr_model.fit(x,np.array(df['Salary']))


# To remove the matplotlib warnig
st.set_option('deprecation.showPyplotGlobalUse', False)


# Add title to your project
st.title('Salary Predictor')


# Add navigation bar
nav = st.sidebar.radio('',['Home','Predictor', 'Contribute'])


# Home Page 
if nav == 'Home':
    # Add header
    st.header('Home Page')

    # Add image
    sal_image = Image.open(r"C:\Users\Mohit Patil\Desktop\Conda_Files\Streamlit\sal.jpg")
    st.image(sal_image, width=700)

    # Add checkbox to show dataframe
    cb = st.checkbox('Show Data')
    if cb == True:
        st.table(df)
    
    # Add graphs
    graph = st.selectbox('What kind of Graph?',['Non-Interactive', 'Interactive'])
    if graph == 'Non-Interactive':
        plt.figure(figsize=(10,5))
        plt.scatter(df['YearsExperience'], df['Salary'])

        plt.xlabel('Years of Experience')
        plt.ylabel('Salary')

        plt.ylim(0)
        plt.tight_layout()
        st.pyplot()

    if graph == 'Interactive':
        layout = go.Layout(
            xaxis = dict(range=[0,12]),
            yaxis = dict(range=[0, 210000])
        )
        fig = go.Figure(data = go.Scatter(x = df['YearsExperience'], y = df['Salary'], mode = 'markers'),layout=layout)
        st.plotly_chart(fig)
        # pass

    
# Predictor Page
if nav == 'Predictor':

    st.header("Know your Salary")
    val = st.number_input("Enter you exp",0.00,20.00,step = 0.25)
    val = np.array(val).reshape(1,-1)
    pred = lr_model.predict(val)[0]

    if st.button("Predict"):
        st.success(f"Your predicted salary is {round(pred)}")


# Contribution Page
if nav == 'Contribute':
    st.header('Contribute to our dataset')

    exp = st.number_input('Entre your Experience', 0.0, 20.00, step = 0.5)
    sal = st.number_input('Entre your Salary', 0.0, 1000000.00, step = 10000.00)

    if st.button('Submite'):
        add_data = {'YearsofExperience':[exp], 'Salary':[sal]}
        add_data = pd.DataFrame(add_data)
        add_data.to_csv('Salary_Data.csv', mode='a', header = False, index = False)
        st.success('Thank you for your contribution')

