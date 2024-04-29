import streamlit as st
import openai

# Set your OpenAI API key here
openai.api_key = 'your-api-key'

def get_response(prompt):
    response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=prompt,
      max_tokens=150
    )
    return response.choices[0].text.strip()

def main():
    st.title('Interview Bot')

    user_input = st.text_input("Enter your question:")
    
    if st.button('Submit'):
        response = get_response(user_input)
        st.text_area("Answer:", value=response, height=200)

if __name__ == '__main__':
    main()
