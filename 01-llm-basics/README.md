# 01 – LLM Basics

This module demonstrates how to interact with a Large Language Model (LLM) using Python for DevOps-related tasks.

---

## 🎯 Objective

Help DevOps engineers with **no prior AI experience**:

- Understand how LLMs like GPT work in basic scenarios
- Make their first API call to a model
- See practical examples like summarizing logs or asking infrastructure questions

---

## 📚 What You'll Learn

- How to use the OpenAI API
- What is a "prompt" and how to structure it for DevOps needs
- How to read logs and ask the model to explain them
- First steps in integrating LLMs into internal tooling

---

## 📁 File Structure

```bash
01-llm-basics/
├── basic_prompt_call.py       # Simple CLI prompt interface to GPT
├── summarize_log.py           # Load a log file and summarize it via LLM
├── .env.example               # Environment variable template
└── README.md                  # This file
```

---

## 🔧 Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/adirothbuilds/ai-driven-devops-workshop.git
cd ai-driven-devops-workshop/01-llm-basics
```

2. **Create a virtual environment (optional but recommended):**

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate    # Windows
```

3. **Install dependencies:**

```bash
pip install openai python-dotenv
```

4. **Configure your API key:**

```bash
cp .env.example .env
# then edit `.env` and add your OpenAI API key
```

---

## 🚀 Usage Examples

### 🔹 basic_prompt_call.py

```bash
python basic_prompt_call.py
```

Example input:

```bash
What causes a Docker image to become bloated?
```

Example output:

```bash
Large Docker images often result from including unnecessary dependencies, not cleaning up cache layers, or using full base OS images instead of slim ones...
```

### 🔹 summarize_log.py

```bash
python summarize_log.py /path/to/build.log
```

Example input:

```bash
/path/to/build.log
```

Example output:

```bash
The build log indicates that the process failed due to missing dependencies in step 3. Consider reviewing the dependency installation step.
```

---

## ⚠️ Notes for Beginners

- This code is for educational purposes only
- Not intended for production use
- The goal is to help you become familiar with how LLMs can support your day-to-day workflows

---

## 💡 Tips

- Use temperature=0.2–0.4 for more consistent answers
- Think of a "prompt" as a clear question or instruction – write it like you're talking to a junior engineer
- You can integrate this into Git hooks, CI steps, or Slack bots later

---

Happy prompting 👨‍💻🤖
