# 07-cli-agent-demo

import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client with API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def main():
    """
    Entry point for the DevOps GPT CLI Agent.
    This function initializes a conversation history with a system message and 
    enters a loop to interact with the user. Users can input DevOps-related 
    questions, and the function will generate responses using a GPT model. 
    The conversation history is maintained to provide context for the responses.
    The user can exit the loop by typing 'exit' or 'quit'. The function also 
    handles keyboard interruptions and unexpected errors gracefully.
    
    Raises:
        Exception: If an unexpected error occurs during the execution.
    """
    print("🤖 DevOps GPT CLI Agent")
    print("""Type your DevOps question or 'exit' to quit.
""")

    # Initialize conversation history with a system message
    history = [
        {
            "role": "system",
            "content": (
                "You are a helpful AI DevOps assistant. Provide concise, clear answers to DevOps-related questions. "
                "If errors or logs are provided, identify the cause and suggest solutions."
            )
        }
    ]

    # Main loop for user input
    while True:
        try:
            # Get user input
            user_input = input("🛠️  You: ")
            if user_input.lower() in ("exit", "quit"):
                print("👋 Goodbye!")
                break
            
            # Append user input to conversation history and get response from GPT
            history.append({"role": "user", "content": user_input})
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=history,
                temperature=0.3
            )
            answer = response.choices[0].message.content.strip()
            
            # Print the assistant's response and append it to history
            history.append({"role": "assistant", "content": answer})
            print(f"""🤖 GPT: {answer}
""")

        except KeyboardInterrupt:
            print("""
👋 Session interrupted. Goodbye!""")
            break
        except Exception as e:
            print(f"⚠️ Error: {e}")

if __name__ == "__main__":
    main()