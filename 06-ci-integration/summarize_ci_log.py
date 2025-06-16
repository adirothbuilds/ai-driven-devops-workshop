# 06-ci-integration

import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client with API key from environment variable
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def load_log(file_path: str) -> str:
    """
    Reads the content of a log file and returns it as a string.
    
    Args:
        file_path (str): The path to the log file to be read.
    
    Returns:
        str: The content of the log file as a string.
    
    Raises:
        FileNotFoundError: If the specified file does not exist.
        IOError: If there is an error reading the file.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def summarize_log(log: str) -> str:
    """
    Summarizes a CI log output, focusing on errors, warnings, and failed tests.
    This function uses a conversational AI model to analyze the provided CI log 
    and generate a concise summary. The summary highlights key issues, such as 
    errors, warnings, or failed tests, and provides insights into what might 
    have gone wrong.
    
    Args:
        log (str): The CI log output as a string.
    
    Returns:
        str: A summarized description of the CI log, focusing on critical issues.
    """
    system_prompt = (
        "You are a DevOps CI assistant. Summarize the following CI log output clearly. "
        "Focus on errors, warnings, or any failed tests. Highlight what likely went wrong."
    )
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": log}
        ],
        temperature=0.4
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python summarize_ci_log.py <log_file>")
        exit(1)

    log_file = sys.argv[1]
    log_text = load_log(log_file)
    print("""🔍 Summarizing CI log...
""")
    summary = summarize_log(log_text)
    print("""🧾 Summary:
""", summary)