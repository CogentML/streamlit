import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt
from PIL import Image

import warnings
warnings.filterwarnings('ignore')

data = pd.DataFrame(
    np.random.randn(100,3),
    columns=['a','b','c']
)

st.line_chart(data)

st.area_chart(data)

st.bar_chart(data)

# matplotlib scatter plot
plt.scatter(x=data['a'], y=data['b'])
plt.title('scatter')
st.pyplot()

# altair scatter plot

chart = alt.Chart(data).mark_circle().encode(
    x = 'a', y = 'b', tooltip = ['a', 'b']
)

st.altair_chart(chart, use_container_width=True)


# st.graphviz_chart("""
# digraph{
# watch -> like
# like -> share
# share -> subscribe
# share -> watch

# }

# """)


city = pd.DataFrame({
    'awesome cities' : ['Chicago', 'Minneapolis', 'Louisville', 'Topeka'],
    'lat' : [41.868171, 44.979840,  38.257972, 39.030575],
    'lon' : [-87.667458, -93.272474, -85.765187,  -95.702548]
})


st.map(city)

# st.image("C://Users//Mohit Patil//Desktop//Conda_Files//Streamlit//sal.jpg")

# st.altair_chart(chart,use_container_width =True)

# plt.scatter(data['a'],data['b'])
# plt.title("scatter")
# st.pyplot()

# st.line_chart(data)

# st.area_chart(data)

# st.bar_chart(data)

image1 = Image.open('sal.jpg')

st.image(image1)

# audio_file = open('data_demo.wav', 'rb')
# audio_bytes = audio_file.read()
# st.audio(audio_bytes, format='audio/ogg')

st.audio("data_demo.wav")

st.video("https://www.youtube.com/watch?v=jq0lKFb-P8k&list=PLuU3eVwK0I9PT48ZBYAHdKPFazhXg76h5&index=5")


# add flowchart

# st.graphviz_chart('''
# diagraph{ sap R/3 -> sas viya -> sas visual analysis}

# ''')

st.graphviz_chart("""
digraph{
SAP -> like
like -> share
share -> subscribe
share -> watch

}

""")

st.graphviz_chart("""
digraph{
SAP R/3 -> SAS Viya
SAS Viya -> SAS Visual Analysis
SAS Visual Analysis -> User 1
SAS Visual Analysis -> User 1
SAS Visual Analysis -> User 1

}

""")