import streamlit as st

st.title("Hello Streamlit")

st.header("Header")

st.subheader("subheader")

st.text("This is my first attempt")

st.markdown("""
# h1 tag
## h2 tag
### h3 tag
:sunglasses:<br>
:moon: <br>
**bold** <br>
_italics_
""", True)

d = {"Name":"Mohit",
     "Lang":"Python",
     "Topic":"streamlit"}

st.latex(r''' a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)''')

st.write(d)

st.write("# Mohit", "Patil")