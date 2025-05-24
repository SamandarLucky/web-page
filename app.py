import streamlit as st
from chatbot import generate_essay_response

# Title of the page
st.title("IELTS Essay")

# Display a simple message
st.write("Enter a writing prompt below to generate an essay:")

# Text input area for the user to enter the prompt
user_prompt = st.text_area("Essay Prompt")

# Display character count for the input
st.write(f"Character count: {len(user_prompt)}")

# Buttons for generating and resetting
col1, col2 = st.columns(2)

with col1:
    if st.button("Generate"):
        if user_prompt:
            with st.spinner("Generating essay..."):
                # Call the generate_essay_response function from chatbot.py
                essay = generate_essay_response(user_prompt)
                st.success("Essay generated successfully!")
                st.write(essay)
        else:
            st.error("Please enter a valid essay prompt to generate an essay.")

with col2:
    if st.button("Reset"):
        # Reset the text area by rerunning the app
        st.rerun()