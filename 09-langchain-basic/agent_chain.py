from langgraph.prebuilt import create_react_agent
from langchain_core.runnables import Runnable
from langchain_core.messages import HumanMessage, AIMessage
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Tool setup
def log_search_tool(query: str) -> str:
    """
    Search DevOps logs for a given keyword.
    """
    return f"[FAKE LOG RESULT] Found 2 entries containing '{query}' in CI pipeline logs."

# Create the LangGraph Agent
agent = create_react_agent(
    model="openai:gpt-3.5-turbo",
    tools=[log_search_tool],
    prompt="You are a helpful DevOps assistant. "
           "If a tool returns a result, summarize it clearly for the user."
)

# Create a runnable agent executor
# This allows us to invoke the agent with user input
agent_executor: Runnable = agent

if __name__ == "__main__":
    print("🤖 DevOps Agent is ready!")
    while True:
        user_input = input("\n💬 Ask something (or type 'exit'): ")
        if user_input.lower() == "exit":
            break
        
        # Invoke the agent with user input
        result = agent_executor.invoke({
            "messages": [HumanMessage(content=user_input)]
        })

        # Extract and print the last AI message from the result
        messages = result.get("messages", [])
        response_found = False
        # Iterate through messages in reverse order to find the last AIMessage
        for msg in messages[::-1]:
            # Check if the message is an AIMessage and has content
            if isinstance(msg, AIMessage) and msg.content:
                print("\n📣 Agent Reply:\n", msg.content.strip())
                response_found = True
                break
        if not response_found:
            print("\n📣 Agent Reply:\n No response received.")
