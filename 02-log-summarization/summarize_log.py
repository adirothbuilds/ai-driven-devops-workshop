# 02-log-summarization

import os
import argparse
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def summarize_text(text: str, model="gpt-3.5-turbo", max_tokens=400) -> str:
    """
    Summarizes a given system log text, highlighting errors, warnings, and 
    important events using an AI language model.

    Args:
        text (str): The system log text to be summarized.
        model (str, optional): The name of the AI model to use for summarization. 
            Defaults to "gpt-3.5-turbo".
        max_tokens (int, optional): The maximum number of tokens for the 
            generated summary. Defaults to 400.

    Returns:
        str: A summarized version of the input text, focusing on key details 
        such as errors, warnings, and significant events.
    """
    system_message = (
        "You are a DevOps assistant. Summarize the following system log clearly, "
        "highlighting errors, warnings, and any important events."
    )
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": text}
        ],
        temperature=0.3,
        max_tokens=max_tokens
    )
    return response.choices[0].message.content.strip()

def read_file(file_path: str) -> str:
    """
    Reads the content of a file and returns it as a string.
    
    Args:
        file_path (str): The path to the file to be read.
    
    Returns:
        str: The content of the file.
    
    Raises:
        FileNotFoundError: If the file does not exist at the specified path.
    """

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

if __name__ == "__main__":
    """
    Command-line interface to summarize a system log file using GPT.
    
    Usage:
        python summarize_log.py <file_path>
    
    Example:
        python summarize_log.py build.log
    """
    parser = argparse.ArgumentParser(description="Summarize a system log file using GPT.")
    parser.add_argument("file_path", help="Path to the log file (e.g., build.log)")
    args = parser.parse_args()

    try:
        log_content = read_file(args.file_path)
        print("📤 Sending log to GPT for summarization...\n")
        summary = summarize_text(log_content)
        print("📄 Summary:\n")
        print(summary)
    except Exception as e:
        print("❌ Error:", str(e))
