# 04-prompt-engineering

import os
from openai import OpenAI
from dotenv import load_dotenv
from difflib import SequenceMatcher

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client with API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Define prompt variants and a reference answer
prompt_variants = [
    "How can I reduce Docker image size?",
    "What are some best practices to make Docker images smaller?",
    "As a DevOps expert, how would you optimize a Dockerfile to minimize image size?",
    "Explain how to debug large Docker images and reduce unnecessary layers.",
]

# Reference answer for comparison
reference_answer = (
    "To reduce Docker image size, use a minimal base image (like alpine), "
    "combine RUN instructions to reduce layers, and clean up unnecessary files after installation steps. "
    "Also, avoid copying large unused files into the image."
)

def call_prompt(prompt: str) -> str:
    """
    Sends a prompt to the GPT-3.5-turbo model and returns the generated response.
    
    Args:
        prompt (str): The input prompt to be sent to the model.
    
    Returns:
        str: The generated response from the model, stripped of leading and trailing whitespace.
    """
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4
    )
    return response.choices[0].message.content.strip()

def similarity(a: str, b: str) -> float:
    """
    Calculate the similarity ratio between two strings using the SequenceMatcher.
    
    Args:
        a (str): The first string to compare.
        b (str): The second string to compare.
    
    Returns:
        float: A similarity ratio between 0 and 1, where 1 indicates identical strings.
    """
    return SequenceMatcher(None, a, b).ratio()

if __name__ == "__main__":
    """
    Main function to execute the prompt variants, compare their answers with a reference answer,
    and print the results ranked by similarity score.
    
    This function iterates over a list of prompt variants, sends each to the model,
    compares the generated answers with a reference answer, and prints the results
    in descending order of similarity score.
    """
    results = []

    # for each prompt variant, call the model and calculate similarity with the reference answer
    for prompt in prompt_variants:
        answer = call_prompt(prompt)
        score = similarity(answer, reference_answer)
        results.append((prompt, answer, score))

    # sort results by similarity score in descending order
    sorted_results = sorted(results, key=lambda x: x[2], reverse=True)

    # Print the ranked results
    for i, (prompt, answer, score) in enumerate(sorted_results, 1):
        print(f"🏅 Ranked #{i} – Score: {score:.2f}")
        print(f"Prompt: {prompt}")
        print(f"""Answer:
{answer}""")
        print("—" * 40 + "\n")