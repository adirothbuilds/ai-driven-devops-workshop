---
marp: true
paginate: true
---

# 07 – CLI Agent Demo

This module introduces a simple, single-file **AI DevOps agent** that runs from your terminal.

You can ask it questions, paste in logs, and get fast LLM-powered answers. This is useful for:

- Local experimentation
- On-the-fly debugging support
- Giving DevOps engineers a "GPT shell assistant"

---

## 🎯 Objective

Provide a minimal, interactive DevOps assistant that runs in the CLI with memory-style flow.

---

## 📁 File Structure

```bash
07-cli-agent-demo/
├── devops_agent.py          # Main interactive CLI tool
├── .env.example             # API key config
└── README.md
```

---

## 💻 What It Does

- Loads your OpenAI key from `.env`
- Starts a terminal session (like a chat)
- Maintains light memory of previous Q&A
- Can summarize logs, explain errors, or assist with commands

---

## 🔧 Requirements

- Python 3.9+
- `openai>=1.0.0`
- `python-dotenv`

Install:

```bash
pip install openai python-dotenv
```

---

## 🚀 Run It

```bash
python devops_agent.py
```

Then enter questions like:

``` txt
How do I restart a Kubernetes pod?
Explain what this error means: EADDRINUSE
```

Exit by typing `exit`, `quit`, or `Ctrl+C`

---

## ⚠️ Notes

- This is a basic REPL (read-eval-print loop) wrapper around the OpenAI API
- You can customize the system message to act like a CI bot, SRE assistant, or Docker advisor

---

## 💡 Tip

> You don’t need to build a full UI to get the value of an agent.

Start with a CLI – and grow from there 🧠💻
