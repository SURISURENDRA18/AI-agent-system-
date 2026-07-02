

import os
from tavily import TavilyClient
from dotenv import load_dotenv

load_dotenv()

tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

def search_tool(query: str):
    res = tavily.search(query=query, max_results=5)
    return "\n\n".join([r["content"] for r in res["results"]])