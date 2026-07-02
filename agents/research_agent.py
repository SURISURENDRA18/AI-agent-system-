

from tools.llm import call_llm
from tools.search_tool import search_tool

def research_agent(state):
    query = state["query"]

    data = search_tool(query)

    prompt = f"""
    You are a research agent.

    Use real-time data below:
    {data}

    Task:
    - Extract ONLY important facts and trends
    - Avoid repetition
    - Include stats ONLY if confident
    - Focus on recent insights (2024–2026)

    Output:
    - Bullet points
    - No explanation
    """

    return {"research": call_llm(prompt)}