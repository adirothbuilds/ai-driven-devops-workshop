# 08 – Tool Execution: Dockerfile Generator Agent

In this final section, we demonstrate how an LLM-based agent can **generate a valid Dockerfile** from a simple prompt and save it to disk.

This marks the transition from conversational agents → **actionable agents** that can perform real-world tasks.

---

## 🎯 Goals

- Separate agent components (system prompt, memory, tool output)
- Generate a Dockerfile from natural language instructions
- Save the file as `Dockerfile` and print it to the console

---

## 📂 Folder Structure

```bash
08-tool-execution/
├── dockerfile_agent.py            # CLI agent to generate Dockerfile
├── prompts/
│   └── system_prompt.txt          # How the agent views itself
├── memory/
│   └── interaction_log.json       # Conversation history log
├── generated/
│   └── Dockerfile                 # Output created by the agent
├── .env.example                   # API key and configs
└── README.md
```

---

## 🛠 Requirements

- Python 3.9+
- `openai`, `python-dotenv`

```bash
pip install openai python-dotenv
```

---

## 🚀 How to Run

```bash
python dockerfile_agent.py
```

Example prompt:

``` bash
🧠 Describe your app: Flask app with gunicorn and requirements.txt
```

The system will generate a Dockerfile, print it to the console, and save it under `generated/Dockerfile`.

---

## 🧱 Optional Extensions

- Generate docker-compose.yaml alongside the Dockerfile
- Validate Dockerfile using linter tools (e.g., hadolint)
- Auto-send result to Slack or GitHub PR comment

---

## ⚠️ Disclaimer

> This agent is a demo only. It performs no input validation or production security checks. The goal is to demonstrate how LLMs can **move from reasoning to real-world execution**.

---

Enjoy hacking 😎
