# # Setup api keys for groq, OPENAI and tavily
# # Setup LLM tools 
# # Setup AI agent with search functionality


# # Setup api keys for groq, OPENAI and tavily
# from dotenv import load_dotenv
# import os 
# load_dotenv()
# GROQ_API_KEY = os.getenv("GROQ_API_KEY")
# TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


# # Setup LLM tools 
# from langchain_groq import ChatGroq
# from langchain_openai import ChatOpenAI
# from langchain_community.tools.tavily_search import TavilySearchResults

# openai_llm=ChatOpenAI(model="gpt-4o-mini")
# groq_llm=ChatGroq(model="llama-3.3-70b-versatile")

# search_tool = TavilySearchResults(max_resilts=2)



# # Setup AI agent with search functionality
# from langgraph.prebuilt import create_react_agent
# from langchain_core.messages.ai import AIMessage
# system_prompt="Act as an AI Agent who is smart and friendly"

# def get_response_from_ai_agent(llm_id, query, allow_search, system_prompt,provider):
    
#     if provider=="Groq":
#         llm=ChatGroq(model=llm_id)
#     elif provider=="OpenAI":
#         llm=ChatOpenAI(model=llm_id)
        
#     tools=[ TavilySearchResults(max_results=2)] if allow_search else []
#     agent=create_react_agent(
#     model=llm,
#     tools=tools,
#     state_modifier=system_prompt
#     )

#     state={"messages":query}
#     response=agent.invoke(state)
#     messages=response.get("messages")
#     ai_messages=[message.content for message in messages if isinstance(message, AIMessage)]
#     return ai_messages[-1]



# Setup API keys for Groq, OpenAI, and Tavily
from dotenv import load_dotenv
import os 
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


# Setup LLM tools
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults

# Corrected typo in max_results
search_tool = TavilySearchResults(max_results=2)


# Setup AI agent with search functionality
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

def get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider):
    # Dynamically select model based on provider
    if provider == "Groq":
        llm = ChatGroq(model=llm_id)
    elif provider == "OpenAI":
        llm = ChatOpenAI(model=llm_id)
    else:
        return "Invalid provider selected."

    # Add search tool if allowed
    tools = [search_tool] if allow_search else []

    # Create the agent
    agent = create_react_agent(
        model=llm,
        tools=tools
    )

    # Inject system prompt as initial message
    state = {
        "messages": [
            SystemMessage(content=system_prompt),
            HumanMessage(content=query)
        ]
    }

    # Call the agent
    try:
        response = agent.invoke(state)
        messages = response.get("messages", [])
        ai_messages = [msg.content for msg in messages if isinstance(msg, AIMessage)]
        return ai_messages[-1] if ai_messages else "Sorry, I couldn't find an answer."
    except Exception as e:
        return f"Error during agent response: {str(e)}"

