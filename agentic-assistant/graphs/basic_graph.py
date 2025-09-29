from langgraph.graph import StateGraph, END
from typing import TypedDict

# Define the state schema
class GraphState(TypedDict):
    input: str

def start_node(state: GraphState) -> GraphState:
    print("Start node received:", state)
    return state  # Pass state to next node

def tool_node(state: GraphState) -> GraphState:
    print("Tool node received:", state)
    return state  # Final state returned

# Initialize graph with schema
graph = StateGraph(GraphState)
graph.add_node("start", start_node)
graph.add_node("tool_node", tool_node)
graph.set_entry_point("start")
graph.set_finish_point("tool_node")  # ✅ fixed

graph = graph.compile()
output = graph.invoke({"input": "Test"})
print("Graph output:", output)

