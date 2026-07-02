
from langgraph.graph import StateGraph, END
from typing import TypedDict
from agents.research_agent import research_agent
from agents.analysis_agent import analysis_agent
from agents.writer_agent import writer_agent
from agents.reviewer_agent import reviewer_agent


class State(TypedDict):
    query: str
    research: str
    analysis: str
    draft: str
    final: str


builder = StateGraph(State)

builder.add_node("research_node", research_agent)
builder.add_node("analysis_node", analysis_agent)
builder.add_node("writer_node", writer_agent)
builder.add_node("reviewer_node", reviewer_agent)


builder.set_entry_point("research_node")

builder.add_edge("research_node", "analysis_node")
builder.add_edge("analysis_node", "writer_node")
builder.add_edge("writer_node", "reviewer_node")


def route(state):
    if state.get("final"):
        return END
    return "writer_node"


builder.add_conditional_edges("reviewer_node", route)


graph = builder.compile()