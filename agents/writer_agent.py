

from tools.llm import call_llm

def writer_agent(state):
    prompt = f"""
    You are a senior business analyst writing for executives.

    Convert this analysis into a HIGH-QUALITY report:

    {state['analysis']}

    STRICT RULES:
    - Be concise and sharp
    - Avoid generic statements
    - Focus on insights, not description

    Structure:

    Title

    Executive Summary (3-4 lines, powerful)

    Top Insights (ranked, clear and impactful)

    Key Risk (1, clearly explained)

    Key Opportunity (1, clearly explained)

    Final Takeaway (strong, non-obvious insight)

    Tone:
    - Professional
    - Insightful (like McKinsey/Bain report)
    """

    return {"draft": call_llm(prompt)}