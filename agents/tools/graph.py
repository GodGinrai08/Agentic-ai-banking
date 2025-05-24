from langgraph.graph import StateGraph, END
from langchain_core.runnables import RunnableLambda
from agents.tools.transaction_analyzer import analyze_transactions
from agents.tools.summarizer import summarize_insights
from agents.tools.data.load_transactions import load_transactions

from typing import TypedDict, List, Dict, Any

# Step 1: Define a state schema
class GraphState(TypedDict):
    transactions: List[Dict[str, Any]]
    insights: str

# Step 2: Build the graph
def build_graph():
    builder = StateGraph(GraphState)  # <-- pass schema here!

    # Nodes
    builder.add_node("load", RunnableLambda(load_transactions))
    builder.add_node("analyze", RunnableLambda(analyze_transactions))
    builder.add_node("summarize", RunnableLambda(summarize_insights))

    # Flow
    builder.set_entry_point("load")
    builder.add_edge("load", "analyze")
    builder.add_edge("analyze", "summarize")
    builder.set_finish_point("summarize")

    return builder.compile()

# Run it
if __name__ == "__main__":
    graph = build_graph()
    output = graph.invoke({})
    print(output)
