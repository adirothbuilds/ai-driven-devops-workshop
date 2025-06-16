---
marp: true
paginate: true
---

# 02 – Log Summarization

This module demonstrates how to use a Large Language Model (LLM) to summarize system logs for DevOps-related tasks.

---

## 🎯 Objective

Help DevOps engineers:

- Quickly understand the key points in system logs
- Identify errors, warnings, and important events
- Automate log analysis using LLMs

---

## 📚 What You'll Learn

- How to use the OpenAI API for log summarization
- How to integrate LLMs into log analysis workflows

---

## 📁 File Structure

```bash
02-log-summarization/
├── summarize_log.py           # Script to summarize logs using LLM
├── logs/                      # Directory containing sample logs
│   └── sample.log             # Example log file
└── README.md                  # This file
```

---

## 🔧 Setup Instructions

1. **Navigate to the directory**

    ```bash
    cd ai-driven-devops-workshop/02-log-summarization
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
- You can integrate this into Git hooks, CI steps, or bots later

---

Happy summarizing 👨‍💻🤖
