from langgraph.graph import StateGraph, END
from typing import TypedDict

class GraphState(TypedDict):
    input: str
    intent: str

# Step 2: Simulate an intent classifier

def classify_node(state: GraphState):
    print("[Classify Node]")
    query = state["input"].lower()
    if "weather" in query:
        state["intent"] = "weather"
        return {"next": "weather_node", **state}
    elif "news" in query:
        state["intent"] = "news"
        return {"next": "news_node", **state}
    else:
        state["intent"] = "default"
        return {"next": "fallback_node", **state}

# Step 3: Define downstream nodes

def weather_node(state):
    print("[Weather Node] — Simulated weather result")
    return state

def news_node(state):
    print("[News Node] — Simulated news result")
    return state

def fallback_node(state):
    print("[Fallback Node] — No match found")
    return state

# Step 4: Build the graph

graph = StateGraph(GraphState)
graph.add_node("classifier", classify_node)
graph.add_node("weather_node", weather_node)
graph.add_node("news_node", news_node)
graph.add_node("fallback_node", fallback_node)

graph.add_edge("weather_node", END)
graph.add_edge("news_node", END)
graph.add_edge("fallback_node", END)

graph.set_entry_point("classifier")


graph = graph.compile()

# Step 5: Run different queries

if __name__ == "__main__":
    queries = [
        "What’s the weather in Nairobi?",
        "Show me news on GPT-4",
        "Who won the chess game last night?"
    ]
    for q in queries:
        print("\n--- Running Graph ---")
        result = graph.invoke({"input": q})
        print("Final Intent:", result["intent"])
