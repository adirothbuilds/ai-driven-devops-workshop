# 04 – Prompt Engineering

This module explores the art and science of writing better prompts for LLMs (Large Language Models) in the context of DevOps automation.

Rather than changing the model, we change how we speak to it – to:

- Get more accurate, structured, and useful responses
- Reduce hallucinations
- Make outputs predictable and production-friendly

---

## 🎯 Objective

Equip DevOps engineers with:

- Practical prompting techniques
- Common DevOps examples (logs, errors, infrastructure questions)
- Templates and reusable strategies

---

## 📁 File Structure

```bash
04-prompt-engineering/
├── 01-direct-vs-system.py         # Compares plain prompt vs. system message
├── 02-steering-options.py         # Shows how to 'guide' LLM with prompt variants
├── 03-ranked-prompt.py            # Select best answer out of several prompts
├── prompt-examples.md             # DevOps-focused prompt templates
└── README.md
```

---

## 🧪 Examples We'll Cover

1. **Direct Prompting**  
   → Asking a question directly with no context

2. **System Message Prompting**  
   → Giving the model a defined persona (e.g. "You are a DevOps assistant")

3. **Steering via Prompt Variants**  
   → Trying multiple phrasings to improve result quality

4. **Prompt Voting**  
   → Run several prompt styles → rank and select best result

---

## 🔧 Tech Requirements

Same as earlier modules:

- Python 3.9+
- `openai>=1.0.0`
- `python-dotenv`

---

## 🚀 Getting Started

```bash
pip install openai python-dotenv
```

Then run:

```bash
python 01-direct-vs-system.py
```

---

## 💡 Tip

> If you ever feel like the LLM doesn't "get it" – it's probably the prompt, not the model.

Prompt engineering is 80% psychology and 20% syntax ✍️🧠
