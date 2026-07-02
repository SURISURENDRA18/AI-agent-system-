

from tools.llm import call_llm

def reviewer_agent(state):
    draft = state["draft"]

    prompt = f"""
    You are a strict reviewer.

    Check this report:

    {draft}

    Validate:
    - No repetition
    - Logical reasoning present
    - No unrealistic claims
    - Clear structure

    If PERFECT → return APPROVED  
    Else → return improved version ONLY
    """

    res = call_llm(prompt)

    if "APPROVED" in res:
        return {"final": draft}
    else:
        return {"draft": res}