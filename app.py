import streamlit as st
from openai import OpenAI

# 1. Page Configuration (Must be at the very top)
st.set_page_config(page_title="Risha AI Bot", page_icon="🤖")
st.title("🤖 Risha AI Chatbot")

# 2. Initialize the OpenAI Client
# This safely loads the key from your .streamlit/secrets.toml file
try:
    api_key = st.secrets["OPENROUTER_API_KEY"]
except Exception:
    st.error("API Key not found. Please ensure it is set in .streamlit/secrets.toml")
    st.stop()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
    default_headers={
        "HTTP-Referer": "http://localhost:8501",
        "X-Title": "Risha Project Chatbot",
    }
)

# 3. Maintain Conversation History
if "messages" not in st.session_state:
    st.session_state.messages = []

# 4. Display Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 5. Handle User Input and Stream Response
if prompt := st.chat_input("Ask me anything..."):
    # Display and Save User Message
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Generate and Stream Assistant Response
    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model="meta-llama/llama-3.1-8b-instruct",
            messages=st.session_state.messages,
            stream=True,
        )
        response = st.write_stream(stream)
    
    # Save Assistant Response
    st.session_state.messages.append({"role": "assistant", "content": response})