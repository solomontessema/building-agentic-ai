from langgraph.graph import StateGraph, END
from typing import TypedDict

class GraphState(TypedDict):
    input: str
    step: str

# Step 2: Define nodes

def start_node(state: GraphState) -> GraphState:
    print("[Start Node]")
    print("Input:", state["input"])
    state["step"] = "classified"
    return state

def response_node(state: GraphState) -> GraphState:
    print("[Response Node]")
    print("Step:", state["step"])
    return state

# Step 3: Initialize the graph

graph = StateGraph(GraphState)
graph.add_node("start", start_node)
graph.add_node("respond", response_node)

graph.set_entry_point("start")
graph.set_finish_point("respond")

graph.add_edge("start", "respond")

graph = graph.compile()

# Step 4: Run the graph

if __name__ == "__main__":
    output = graph.invoke({"input": "What's the weather in Nairobi?"})
    print("Final Output:", output)
