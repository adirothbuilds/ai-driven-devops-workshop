# 05 – RAG with Dev Docs

In this module, we demonstrate how to apply **Retrieval-Augmented Generation (RAG)** to DevOps workflows by combining LLMs with relevant internal documentation.

Instead of relying only on the LLM's training data, we:

- Inject context from README files, CI logs, configs, etc.
- Ask more specific questions
- Get more accurate, company-specific answers

---

## 🎯 Objective

Help DevOps engineers:

- Use their own documentation as dynamic LLM input
- Reduce hallucinations and generic answers
- Build foundations for context-aware bots or assistants

---

## 📁 File Structure

```bash
05-rag-with-dev-docs/
├── ask_with_context.py       # Load a file and inject it into the prompt
├── sample_readme.md          # Example README or internal doc
├── .env.example              # API key
└── README.md
```

---

## 🧠 What is RAG?

RAG stands for **Retrieval-Augmented Generation**:
> "Instead of asking a model to guess, give it relevant information to work with."

In our case, we:

1. Load a document (e.g. sample_readme.md)
2. Ask a question like "How is deployment handled in this service?"
3. Inject the doc + question into the LLM prompt

---

## 🚀 Usage

```bash
python ask_with_context.py sample_readme.md
```

Then enter your question interactively:

``` txt
How is rollback handled?
```

---

## 🛠 Requirements

Same as previous modules:

- Python 3.9+
- `openai>=1.0.0`
- `python-dotenv`

Install dependencies:

```bash
pip install openai python-dotenv
```

---

## ⚠️ Notes

- This is a very basic RAG approach (file → prompt)
- For real apps, use vector DBs and semantic search (e.g. with LangChain or LlamaIndex)
- Even simple RAG can greatly improve LLM usefulness in ops

---

## 🔥 Tip

> Start simple: even injecting one config file or doc can cut hallucinations by 70%+.

This is how DevOps gets smarter 📚⚙️
