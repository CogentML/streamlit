import streamlit as st
import pandas as pd 
from matplotlib import pyplot as plt
import time

# to remove the matplotlib warnig
st.set_option('deprecation.showPyplotGlobalUse', False)


# # adding a sidebar
# st.sidebar.selectbox('Pick a number', [_ for _ in range(10)])

# now using side bar we will plot graphs

plt.style.use("ggplot")

# lets make a dataframe
data = {
    "num":[x for x in range(1,11)],
    "square":[x**2 for x in range(1,11)],
    "twice":[x*2 for x in range(1,11)],
    "thrice":[x*3 for x in range(1,11)]
}

# df = pd.DataFrame(data=data)

#now we will ise sidebar to take input of x and y axis to plot the graph

# x = st.sidebar.selectbox('Select X-Axis', df.columns)
# y = st.sidebar.selectbox('Select Y-Axis', df.columns)

# plt.plot(df[x],df[y])
# st.pyplot()




# # let assume that I want multiple graphs then I will use multiselect
# y = st.sidebar.multiselect('Select the columns', df.columns)

# plt.plot(df['num'], df[y])
# st.pyplot()


# Adding navigation bar or also creating multiple page like enviorment

rad = st.sidebar.radio('Navigation',['Graphs', 'About Us'])

if rad == 'Graphs':
    
    df = pd.DataFrame(data=data)

    col = st.sidebar.multiselect('Entre the columns', df.columns)

    plt.plot(df['num'], df[col])

    st.pyplot()

# if rad == 'About Us':
#     st.write('You are our About Us Page')



# Adding animations-> Progress and status

# adding status messages to your web page


if rad == 'About Us':
    st.write('You are our About Us Page')

    progress = st.progress(0)
    for i in range(100):
        time.sleep(0.1)
        progress.progress(i+1)

    st.balloons()

    st.error('Error')
    st.success('Show Success')
    st.info('Information')
    st.exception(RuntimeError('This is an error'))
    st.warning('this is a warning')