

from tools.llm import call_llm

def analysis_agent(state):
    prompt = f"""
    You are a senior AI analyst.

    Analyze this research:

    {state['research']}

    STRICT RULES:
    - Do NOT repeat points
    - Remove weak or redundant insights
    - Be specific (no generic statements)

    Your tasks:
    1. Identify TOP 5 insights (ranked by importance)
    2. For each insight:
       - What is happening
       - Why it matters
       - Who is most affected
    3. Identify:
       - Biggest Risk (ONLY 1)
       - Biggest Opportunity (ONLY 1)
    4. Highlight contradictions if any

    Output format:

    Top Insights (Ranked):
    1. Insight:
       - Why it matters:
       - Who is affected:

    Biggest Risk:
    - ...

    Biggest Opportunity:
    - ...

    Contradictions (if any):
    - ...
    """

    return {"analysis": call_llm(prompt)}