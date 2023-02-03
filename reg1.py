import streamlit as st
import pandas as pd

# Title of the form
st.title('REGISTRATION FORM')

# Take user registration information
first, last = st.columns(2)
first_name = first.text_input('First Name')
last_name = last.text_input('Last Name')


email, mobile = st.columns([3,1])
email_id = email.text_input('Email Id')
mobile_no = mobile.text_input('Mobile No')

username, pw1, pw2 = st.columns(3)
username = username.text_input('Pick your Userane')
password = pw1.text_input('Pick your Password', type = 'password')
pw_confirm = pw2.text_input('Confirm your Password', type = 'password')

cb, submit = st.columns([6,1])
agree = cb.checkbox('I Agree to Terms & Conditions')
if submit.button('Submit'):
    add_data = {'First Name': [first_name], 'Last Name': [last_name], 'Email Id': [email_id], 'Mobile No': [mobile_no], 'Username': [username], 'Password': [password]}
    add_data = pd.DataFrame(add_data)
    add_data.to_csv('registration_data.csv', mode='a', header = False, index = False)
    st.success('Thank you for Restration')
    
