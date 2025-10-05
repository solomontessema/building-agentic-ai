from agents.base_agent import agent

print("\n--- Multi-Step Test ---")
query = "Find the weather in Nairobi and summarize the result in one sentence."
response1 = agent.run(query)
print(response1)

response2 = agent.run("What's the latest news on AI regulation?")
print(response2)

query = "Find the weather in Nairobi and summarize the result in one sentence."
response3 = agent.run(query)
print(response3)