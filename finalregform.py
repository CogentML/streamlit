import streamlit as st
import pymysql
import re

# Connect to MySQL database
conn = pymysql.connect(
        host='localhost',
        user='root',
        password='mohit@cogent',
        db='mohitdb',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

# Title of the form
st.title('REGISTRATION FORM')

# Check if the submit button was pressed
if st.button('Submit'):
    
    # Take user registration information
    first_name = st.text_input('First Name')
    last_name = st.text_input('Last Name')
    email = st.text_input('Email Id')
    mobile = st.text_input('Mobile No')
    username = st.text_input('Pick your Userane')
    pw1 = st.text_input('Pick your Password', type = 'password')
    pw2 = st.text_input('Confirm your Password', type = 'password')
    terms_conditions = st.checkbox('I Agree to Terms & Conditions')
    
    # Check if all fields are filled
    if not all([first_name, last_name, email, mobile, username, pw1, pw2, terms_conditions]):
        st.error('Please fill all the fields')
        
    # Check if email is valid
    elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        st.error('Invalid email')
        
    # Check if password and password confirmation match
    elif pw1 != pw2:
        st.error('Password and confirmation password do not match')
        
    # Check if password has at least 8 characters with one Capital letter, one small letter, one digit, one symbol
    elif not re.match(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$', pw1):
        st.error('Password must have at least 8 characters with one Capital letter, one small letter, one digit, one symbol')
        
    # Check if mobile number is valid
    elif not re.match(r'^\d{10}$', mobile):
        st.error('Invalid mobile number')
        
    # Check if username is unique
    else:
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM users WHERE username='{username}'")
        if cur.fetchone():
            st.error('Username already exists')
        else:
            # Insert data into MySQL table
            cur.execute(f"INSERT INTO users (first_name, last_name, email, mobile, username, password) VALUES ('{first_name}', '{last_name}', '{email}', '{mobile}', '{username}', '{pw1}')")
