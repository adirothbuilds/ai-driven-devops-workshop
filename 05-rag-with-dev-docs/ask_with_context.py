# 05-rag-with-dev-docs

import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def load_context(file_path: str) -> str:
    """
    Loads the content of a file and returns it as a string.
    
    Args:
        file_path (str): The path to the file to be read.
    
    Returns:
        str: The content of the file as a string.
    
    Raises:
        FileNotFoundError: If the file does not exist.
        IOError: If there is an error reading the file.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def ask_question_with_context(context: str, question: str) -> str:
    """
    Generates a response to a user's question based on provided documentation context.
    
    Args:
        context (str): The documentation or context to use for answering the question.
        question (str): The user's question to be answered.
    
    Returns:
        str: The response generated based on the provided context and question.
    """
    prompt = (
        "You are a DevOps assistant. Use the following documentation to answer the user's question.\n\n"
        f"---\nDOCUMENTATION:\n{context}\n---\n\n"
        f"QUESTION:\n{question}\n"
    )
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python ask_with_context.py <path_to_doc>")
        exit(1)

    context_file = sys.argv[1]
    context_text = load_context(context_file)

    question = input("❓ Ask your DevOps question: ")
    print("\n🤖 Thinking...\n")
    answer = ask_question_with_context(context_text, question)
    print("💬 Answer:\n", answer)