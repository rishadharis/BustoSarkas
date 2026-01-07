from langchain_community.tools.tavily_search import TavilySearchResults
# from dotenv import load_dotenv
# import os
from utils import get_config

tavily_api_key = get_config("TAVILY_API_KEY")
# print(tavily_api_key)

def get_url_profile_tavily(name: str):
    """Searches for LinkedIn Profile Page."""
    search = TavilySearchResults(tavily_api_key=tavily_api_key)
    res = search.run(f"{name}")

    return res
