import os

from dotenv import load_dotenv

load_dotenv()

#pip show langchain
#pip show langchain-core
#pip show langchain-community
#pip show langchain-tavily
#pip show tavily-pythonpip lis

from tavily import TavilyClient
from langchain_core.tools import Tool

tavily_api_key = os.getenv("TAVILY_API_KEY")
if not tavily_api_key:
    raise ValueError("TAVILY_API_KEY not found in .env file")

client = TavilyClient(api_key=tavily_api_key)

def search_web(query: str):
    return client.search(query=query, max_results=3)

tavily_tool = Tool(
    name="Tavily Search",
    func=search_web,
    description="Search the web for current information."
)

print(tavily_tool.invoke("Who is leo messi?"))