# 09 – LangChain Basics: Chaining Logic with LLMs

This optional section introduces LangChain – a framework that helps you build modular, chainable pipelines around LLMs.

> LangChain is ideal for building tool-aware agents, memory handling, and multi-step logic.

---

## 🎯 Goals

- Understand LangChain's capabilities and use cases
- Create a simple LLMChain with prompt templates
- Integrate a custom tool (e.g., log lookup)
- Build an agent capable of dynamic tool usage

---

## 📂 Folder Structure

```bash
09-langchain-basic/
├── agent_chain.py          # Full agent using the tool via LangChain
├── .env.example            # OpenAI key
└──  README.md
```

---

## 🧠 Concepts

### ✅ LangChain Features

- Prompt Templates
- Chains (sequential logic)
- Agents (dynamic tool routing)
- Memory
- Tool/API Integration

---

## 🚀 Quickstart

Install dependencies:

```bash
pip install langchain langchain_community openai python-dotenv
```

Run the agent (with tool integration):

```bash
python agent_chain.py
```

---

## 🔍 Example Prompt Flow

```bash
User: Search logs for 'docker error'
→ Agent detects need for tool → Calls `search_logs()` → Responds with simulated output
```

You can modify the chain or agent to:

- Log outputs to memory
- Use multiple tools
- Chain multi-step reasoning

---

## ⚠️ Disclaimer

LangChain is powerful but should be used wisely – avoid overengineering when simpler solutions suffice 😅

---

More info:

👉 [LangChain Documentation](https://python.langchain.com/)
