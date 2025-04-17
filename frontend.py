import streamlit as st
import requests

st.set_page_config(page_title="LangGraph Agent UI", layout="centered")
st.title("🤖 LangChat")
st.write("Create and Interact with Custom AI Agents!")

# Prompt input
system_prompt = st.text_area("🧠 Define your AI Agent", height=70, placeholder="Type your system prompt here...")

# Model options
MODEL_NAMES_GROQ = ["llama-3.3-70b-versatile", "llama3-70b-8192", "llama3-8b-8192"]
MODEL_NAMES_OPENAI = ["gpt-4o-mini"]

# Provider selection
provider = st.radio("🛠️ Select Provider", ("Groq", "OpenAI"))

# Model selection based on provider
if provider == "Groq":
    selected_model = st.selectbox("📌 Select Groq Model", MODEL_NAMES_GROQ)
elif provider == "OpenAI":
    selected_model = st.selectbox("📌 Select OpenAI Model", MODEL_NAMES_OPENAI)

# Web search option
allow_web_search = st.checkbox("🌐 Allow Web Search")

# User query input
user_query = st.text_area("💬 Enter your query", height=150, placeholder="Ask Anything!")

# Backend URL
API_URL = "https://langchat-backend.onrender.com/chat"  # change this if running locally

# Function to format the response
def format_ai_response(response_text):
    # Ensure only headings like "1.", "2.", "3." are bold
    formatted = response_text
    formatted = formatted.replace("1.", "**1.**")
    formatted = formatted.replace("2.", "**2.**")
    formatted = formatted.replace("3.", "**3.**")
    formatted = formatted.replace("4.", "**4.**")
    formatted = formatted.replace("5.", "**5.**")
    return formatted

# On button click
if st.button("🚀 Ask Agent!"):
    if user_query.strip():
        payload = {
            "model_name": selected_model,
            "model_provider": provider,
            "system_prompt": system_prompt,
            "messages": [user_query],
            "allow_search": allow_web_search
        }

        try:
            response = requests.post(API_URL, json=payload)

            if response.status_code == 200:
                response_data = response.json()
                if "error" in response_data:
                    st.error(response_data["error"])
                else:
                    # Format and display response
                    response_text = response_data["response"]
                    formatted_response = format_ai_response(response_text)

                    st.subheader("🤖 Agent Response")
                    st.markdown(formatted_response)

            else:
                st.error(f"Backend returned status code {response.status_code}")
        except Exception as e:
            st.error(f"Request failed: {e}")
    else:
        st.warning("Please enter a valid query.")

