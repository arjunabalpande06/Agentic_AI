import os
from dotenv import load_dotenv
from tavily import TavilyClient

# Load the API key from .env
load_dotenv()


class SearchAgent:
    """
    Search Agent
    Uses Tavily to search the web.
    """

    def __init__(self):
        api_key = os.getenv("TAVILY_API_KEY")

        if not api_key:
            raise ValueError("TAVILY_API_KEY not found in .env file")

        self.client = TavilyClient(api_key=api_key)

    def search(self, query):
        print("\n[Search Agent]")
        print(f"Searching for: {query}")

        response = self.client.search(
            query=query,
            max_results=3,
        )

        return response
