# 🤖 LangChat — Your AI Chat Companion  
*(Powered by LangGraph + FastAPI + Streamlit)*

Hey there! 👋  
Welcome to **LangChat**, where your chatbot isn't just smart—it’s smooth, structured, and seriously cool 😎.

This repo brings you a modular AI chatbot with **LangGraph agents**, a snappy **FastAPI** backend, and a clean **Streamlit** UI. Think of it as brains + beauty + speed = 💯

---

## 🧠 Architecture at a Glance

LangChat works in **3 neat phases**:

### 🔹 Phase 1 — Brain Power (LLM Core)
- Uses **LangGraph agents** to handle conversation logic.
- Works with **Groq**, **OpenAI**, **Tavily**, **Meta**, and more.
- Can switch tools/models based on context. Smart, huh?

### 🔹 Phase 2 — FastAPI Backend
- Handles incoming API requests and outgoing responses.
- Validates data with **Pydantic**.
- Runs on **Uvicorn** for that blazing-fast speed.

### 🔹 Phase 3 — Streamlit UI
- Clean, simple interface for user interaction.
- Super easy to use. Just type and talk!

---

## ⚙️ Tech Stack

| Layer       | Tools Used                              |
|-------------|------------------------------------------|
| 🧠 LLM Core | LangGraph, OpenAI, Groq, Tavily, Meta   |
| 🔌 Backend  | FastAPI, Pydantic, Uvicorn              |
| 🎨 Frontend | Streamlit                               |

---

## 🚀 How to Run This Locally

Here’s the 5-step magic spell to launch LangChat:

```bash
# 1. Clone the repo
git clone https://github.com/Aditi-Singh-15/LangChat.git

# 2. (Optional) Create a virtual environment
python -m venv env
source env/bin/activate  # For Windows: env\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Start the backend server
uvicorn backend.main:app --reload

# 5. Run the Streamlit frontend
streamlit run frontend.py

```
## 🌟 Features

- 🧠 **Dynamic model selection** (OpenAI / Groq)  
- 🤖 **LangGraph Agent + Tool chaining**  
- 🔌 **Modular FastAPI backend**  
- 🎨 **Beautiful Streamlit frontend**  
- 🛠️ **Tool support** (Tavily, Meta, etc.)

---

## 🧩 What’s Next?

- [ ] Add memory to retain chat context  
- [ ] Integrate vector store + RAG  
- [ ] Add voice interaction (because why not?)  
- [ ] Cloud deployment + CI/CD (Docker incoming!)

---

## 🙌 Want to Contribute?

Pull requests are welcome!  
Fork the repo, add your magic ✨, and send that PR. Let’s build together.

