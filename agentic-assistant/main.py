from agents.base_agent import agent

print("\n--- Multi-Step Test ---")
query = "Find the weather in Nairobi and summarize the result in one sentence."
response = agent.run(query)
print(response)