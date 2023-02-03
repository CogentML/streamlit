import streamlit as st
import pandas as pd

# Title of the form
st.title('REGISTRATION FORM')

# Take user registration information

first, last = st.columns(2)

first_name = st.text_input('First Name')
last_name = last.text_input('Last Name')

email, mobile = st.columns([3,1])

email.text_input('Email Id')
mobile.text_input('Mobile No')

username, pw1, pw2 = st.columns(3)
username.text_input('Pick your Userane')
pw1.text_input('Pick your Password', type = 'password')
pw2.text_input('Confirm your Password', type = 'password')

cb, submit = st.columns([6,1])
cb.checkbox('I Agree to Terms & Conditions')
# submit.button('Submite')

# Apply condition to the cb == True then only submit otherwise show prompt 'Plese Check "I Agree to Terms & Conditions"'

# Saving above information in registrationform.csv
# if submit.button('Submit'):
#     data = {'First Name': [first], 'Last Name': [last], 'Email Id': [email], 'Mobile No': [mobile], 'Username': [username], 'Password': [pw1]}
#     df = pd.DataFrame(data)
#     print(df)
#     df.to_csv('registration_data.csv', index=False)
#     st.write('Data saved successfully!')

if st.button('Submite'):
        add_data = {'First Name': [first], 'Last Name': [last], 'Email Id': [email], 'Mobile No': [mobile], 'Username': [username], 'Password': [pw1]}
        # add_data = {'YearsofExperience':[exp], 'Salary':[sal]}
        add_data = pd.DataFrame(add_data)
        add_data.to_csv('registration_data.csv', mode='a', header = False, index = False)
        st.success('Thank you for Restration')
