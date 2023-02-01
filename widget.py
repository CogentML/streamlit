import streamlit as st

st.title('WIDGET')

# how to add buttom and functionality to it

st.button('test button')

if st.button('Text Summarization'):

    st.write('Here is your text summary')


# how to get text input from user

# create a variable to store the input
name = st.text_input('Entre your name here')

# display the text input
st.write(name)

# if you want a bigger input window then use text_area
address = st.text_area('Entre your address here')

# date input
st.date_input('Entre your date of birth')

# time input
st.time_input('Entre your time availibility')

# similar to the name, we can save all of this inputs into variables to use them in functions



# adding checkbox to your app and add conditions to the same
if st.checkbox('Accept the terms & conditions', value=False):
    st.write('thank you')


# adding the radio box with & without default selection
st.radio('Location', ['Mumbai', 'Pune', 'Delhi'])

# by default index will be 0
st.radio('Language', ['Python','Java', 'R'], index=1)


# select box
# by default index will be 0
s1 = st.selectbox('Language', ['','Python','Java', 'R'], index=0)

# print the outpput of the selection
st.write(s1)

# multiselect
s2 = st.multiselect('Language', ['Python','Java', 'R'])
st.write('Your Selection', s2)


# add slider

# by default it ranges from 0 to 100
st.slider('Age')

# add min, max, dafault value and step size
st.slider('12th Percentage', min_value=40, max_value=100, value=60, step=5)

# add min, max, dafault value and step size >> type must be same either int or float
st.slider('Degree CGPA', min_value=0.0, max_value=10.0, value=4.0, step=0.5)

# number
st.number_input('number')

# number
st.number_input('number', min_value=10, max_value=100, value=50, step=10)


# # file upload to our web page
# st.file_uploader('Entre the file')

# file upload to our web page
img = st.file_uploader('Entre the your photo')

# from PIL import Image
# image1 = Image.open(img)
# st.image(image1)
st.image(img)