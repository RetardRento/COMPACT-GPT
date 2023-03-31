import openai
import streamlit as st

# Set OpenAI API key
openai.api_key = "YOUR_API_KEY"

# Create Streamlit app
st.title("AI ASKER")
user_input = st.text_input("Enter your query here:")

language = st.selectbox("Select a programming language", ["Python", "Java", "C++"])

if user_input:
    response = openai.Completion.create(engine="text-davinci-003", prompt=user_input, max_tokens=200, stop=None)
    output = response.choices[0].text
    st.code(output, language=language.lower())
