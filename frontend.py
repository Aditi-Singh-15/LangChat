# #Step1: Setup UI with streamlit (model provider, model, system prompt, web_search, query)
# import streamlit as st

# st.set_page_config(page_title="LangGraph Agent UI", layout="centered")
# st.title("AI Chatbot Agents")
# st.write("Create and Interact with the AI Agents!")

# system_prompt=st.text_area("Define your AI Agent: ", height=70, placeholder="Type your system prompt here...")

# MODEL_NAMES_GROQ = ["llama-3.3-70b-versatile", "mixtral-8x7b-32768"]
# MODEL_NAMES_OPENAI = ["gpt-4o-mini"]

# provider=st.radio("Select Provider:", ("Groq", "OpenAI"))

# if provider == "Groq":
#     selected_model = st.selectbox("Select Groq Model:", MODEL_NAMES_GROQ)
# elif provider == "OpenAI":
#     selected_model = st.selectbox("Select OpenAI Model:", MODEL_NAMES_OPENAI)

# allow_web_search=st.checkbox("Allow Web Search")

# user_query=st.text_area("Enter your query: ", height=150, placeholder="Ask Anything!")

# API_URL=  "https://langchat-backend.onrender.com/chat"

# if st.button("Ask Agent!"):
#     if user_query.strip():
#         #Step2: Connect with backend via URL
#         import requests

#         payload={
#             "model_name": selected_model,
#             "model_provider": provider,
#             "system_prompt": system_prompt,
#             "messages": [user_query],
#             "allow_search": allow_web_search
#         }

#         response=requests.post(API_URL, json=payload)
#         if response.status_code == 200:
#             response_data = response.json()
#             if "error" in response_data:
#                 st.error(response_data["error"])
#             else:
#                 st.subheader("Agent Response")
#                 st.markdown(f"**Final Response:** {response_data}")


# Step 1: Setup UI with streamlit (model provider, model, system prompt, web_search, query)
import streamlit as st

st.set_page_config(page_title="LangGraph Agent UI", layout="centered")
st.title("🤖 LangChat")
st.write("Create and Interact with Custom AI Agents!")

system_prompt = st.text_area("🧠 Define your AI Agent", height=70, placeholder="Type your system prompt here...")

MODEL_NAMES_GROQ = ["llama-3.3-70b-versatile", "llama3-70b-8192", "llama3-8b-8192"]
MODEL_NAMES_OPENAI = ["gpt-4o-mini"]

provider = st.radio("🛠️ Select Provider", ("Groq", "OpenAI"))

if provider == "Groq":
    selected_model = st.selectbox("📌 Select Groq Model", MODEL_NAMES_GROQ)
elif provider == "OpenAI":
    selected_model = st.selectbox("📌 Select OpenAI Model", MODEL_NAMES_OPENAI)

allow_web_search = st.checkbox("🌐 Allow Web Search")

user_query = st.text_area("💬 Enter your query", height=150, placeholder="Ask Anything!")

API_URL =  "https://langchat-backend.onrender.com/chat" # 🔁 You can change this to your deployed URL

# Step 2: Connect with backend via URL
if st.button("🚀 Ask Agent!"):
    if user_query.strip():
        import requests

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
                    st.subheader("🤖 Agent Response")
                    st.success(response_data["response"])
            else:
                st.error(f"Backend returned status code {response.status_code}")
        except Exception as e:
            st.error(f"Request failed: {e}")
    else:
        st.warning("Please enter a valid query.")

