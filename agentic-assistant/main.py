from agents.base_agent import agent

print("\n--- Weather Test ---")
response = agent.run("What's the weather in Berlin?")
print(response)

print("\n--- Search Test ---")
response = agent.run("Search for the latest developments in AI regulation.")
print(response)

print("\n--- Combined Query ---")
response = agent.run("What's the weather in Nairobi and also search about AI news?")
print(response)
