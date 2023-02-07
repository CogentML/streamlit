import re
import pymysql
import streamlit as st
import pandas as pd


# Make a connection with mysql server with pymysql
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='mohit@cogent',
    db='mohitdb',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)


# Condition for secure password >> at least one capital letter, one small letter, one digit and one symbol
def password_check(password):
    pattern = re.compile(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,}$')
    return pattern.match(password)

# Condition for valid 10 digit mobile number
def is_valid_mobile_number(number):
    pattern = re.compile(r'^\d{10}$')
    return pattern.match(number)

# Condition for valid email id
def is_valid_email(email):
    pattern = re.compile(r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$')
    return pattern.match(email)


# Streamlit form 

st.title('REGISTRATION FORM')


first, last = st.columns(2)
first_name = first.text_input('First Name')
last_name = last.text_input('Last Name')


email, mobile = st.columns([3,1])
email_id = email.text_input('Email Id')
mobile_no = mobile.text_input('Mobile No')

# Check email input
if email_id:
    if not is_valid_email(email_id):
        st.error('Enter a valid email address')

# Check mobile number input
if mobile_no:
    if not is_valid_mobile_number(mobile_no):
        st.error('Enter a valid 10-digit mobile number')


username, pw1, pw2 = st.columns(3)
username = username.text_input('Pick your Username')
pw1 = pw1.text_input('Pick your Password', type = 'password')
pw2 = pw2.text_input('Confirm your Password', type = 'password')


# Check password input
if pw1:
    if len(pw1) < 8:
        st.error('Password must be at least 8 characters')
    elif not password_check(pw1):
        st.error('Password must contain one capital letter, one small letter, one digit, and one symbol')
    elif pw1 != pw2:
        st.error('Password and Confirm Password must match')

# Check if username already exist in the database or not
with conn.cursor() as cursor:
    sql = "SELECT * FROM registration WHERE username = %s"
    cursor.execute(sql, (username,))
    result = cursor.fetchone()
    if result:
        st.error("Username already exists")


cb, submit = st.columns([6,1])
cb.checkbox('I Agree to Terms & Conditions')


# Store user information in the database
if submit.button('Submit'):
    try:
        with conn.cursor() as cursor:
            sql = "INSERT INTO registration (first_name, last_name, email_id, mobile_no, username, password) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (first_name, last_name, email_id, mobile_no, username, pw1))
        conn.commit()
        st.write('Data saved successfully!')
    except Exception as e:
        st.write('Error saving data: ', e)
    finally:
        conn.close()