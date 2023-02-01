# import streamlit as st
# # from transformers import pipeline

# # Load the summarization model
# summarization_model = pipeline("summarization")

# # Add a title and header
# st.title("Text Summarization")
# st.header("Summary of given text")

# # Add a text input widget
# text_input = st.text_input("Enter your text here")

# # Add a button that summarizes the text
# if st.button("Summarize"):
#     summary = summarization_model(text_input, max_length=100, min_length=30)[0].summary_text
#     st.write("Summary:", summary)

# # Add a footer with a link to the Hugging Face website
# st.markdown("Powered by [Hugging Face](https://huggingface.co)")


import streamlit as st

# Add a title and header
st.title("Cogent Info - NLP Solutions")
st.header("Summarize your text, simplify your life.")



# Add a text input widget
text_input = st.text_input("Enter your text here")

# Add a button that converts the text
if st.button("Convert"):
    converted_text = "Converted Text: " + text_input
    st.success(converted_text)

# Add a footer with a link
st.markdown("Powered by [Cogent Info](https://www.cogentinfo.com/)")

if st.button("Stop"):
    exit()
