import streamlit as st

# Title of the form
st.title('REGISTRATION FORM')

# Take user registration information

first, last = st.columns(2)

first.text_input('First Name')
last.text_input('Last Name')

email, mobile = st.columns([3,1])

email.text_input('Email Id')
mobile.text_input('Mobile No')

username, pw1, pw2 = st.columns(3)
username.text_input('Pick your Userane')
pw1.text_input('Pick your Password', type = 'password')
pw2.text_input('Confirm your Password', type = 'password')

checkbox, submit = st.columns([6,1])
checkbox.checkbox('I Agree to Terms & Conditions')
submit.button('Submite')