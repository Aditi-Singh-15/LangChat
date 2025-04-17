# #Step1: Setup Pydantic Model (Schema Validation)
# from pydantic import BaseModel
# from typing import List

# class RequestState(BaseModel):
#     model_name: str
#     model_provider: str
#     system_prompt: str
#     messages: List[str]
#     allow_search: bool

# #Step2: Setup AI Agent from FrontEnd Request
# from fastapi import FastAPI
# from ai_agent import get_response_from_ai_agent
# ALLOWED_MODEL_NAMES=["gpt-4o-mini", "llama-3.3-70b-versatile", "llama3-70b-8192","mistral-8x7b-32768"]

# app=FastAPI(title="Langgraph AI Agent")

# @app.post("/chat")
# def chat_endpoint(request: RequestState):
#     """
#     API endpoint to interact with the Chatbot using LangGraph and search tools.
#     It dynamically selects the model specified in the request.
    
#     """
    
#     if request.model_name not in ALLOWED_MODEL_NAMES:
#         return {"error": "Invalid model name. Kindly select a valid AI Model."}
    
#     llm_id=request.model_name
#     query=request.messages
#     allow_search=request.allow_search
#     system_prompt=request.system_prompt
#     provider=request.model_provider
    
#     #Create AI Agent and get response from it.
#     response=get_response_from_ai_agent(llm_id, query, allow_search, system_prompt,provider)
#     return response
    


# #Step3: Run app & Explore Swagger UI Docs

# if __name__=="__main__":
#     import uvicorn
#     uvicorn.run(app,host="127.0.0.1",port=9999)


# Step 1: Setup Pydantic Model (Schema Validation)
from pydantic import BaseModel
from typing import List

class RequestState(BaseModel):
    model_name: str
    model_provider: str
    system_prompt: str
    messages: List[str]
    allow_search: bool


# Step 2: Setup AI Agent from FrontEnd Request
from fastapi import FastAPI
from ai_agent import get_response_from_ai_agent

ALLOWED_MODEL_NAMES = [
    "gpt-4o-mini", 
    "llama-3.3-70b-versatile", 
    "llama3-70b-8192",
    "mistral-8x7b-32768"
]

app = FastAPI(title="LangGraph AI Agent")


@app.post("/chat")
def chat_endpoint(request: RequestState):
    """
    API endpoint to interact with the Chatbot using LangGraph and search tools.
    It dynamically selects the model specified in the request.
    """
    if request.model_name not in ALLOWED_MODEL_NAMES:
        return {"error": "Invalid model name. Kindly select a valid AI Model."}

    # Only send the latest message as the query
    query = request.messages[-1] if request.messages else ""

    # Create AI Agent and get response
    ai_response = get_response_from_ai_agent(
        llm_id=request.model_name,
        query=query,
        allow_search=request.allow_search,
        system_prompt=request.system_prompt,
        provider=request.model_provider
    )

    return {"response": ai_response}


# Step 3: Run app & Explore Swagger UI Docs
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=9999)

    
