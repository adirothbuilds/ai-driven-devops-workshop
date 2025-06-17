# 00 – Getting Started with AI-Driven DevOps 🧠⚙️

This section helps you **start quickly** with the repo, even if you've never used OpenAI, .env files, or prompt-based tools before.

---

## 🚀 Quickstart Checklist

### 1. **Create a `.env` file**

Copy the template file:
```bash
cp .env.example .env
```
Then, fill in your OpenAI key:
```
OPENAI_API_KEY=sk-...
```
> You can generate it at: [OpenAI API Keys](https://platform.openai.com/account/api-keys)

---

### 2. **Install requirements**

```bash
pip install -r requirements.txt
```
> All demo folders use `openai`, `python-dotenv`, and standard libraries only.

---

### 3. **Test your setup**

Try running the hello world of LLMs:

```bash
python 01-llm-basics/basic_prompt_call.py
```

Expected output:

``` bash
== DevOps GPT Helper ==
🔧 Enter your DevOps question: What is a Dockerfile?
🧠 Answer from GPT: [...]
```

---

### 4. **Troubleshooting**

#### ❌ ImportError?
Make sure you're running the script from the correct folder, and your virtual environment is active:
```bash
source .venv/bin/activate
```

#### ❌ Rate Limit / Invalid Key?

Check `.env` again, and ensure your API key is not expired or deactivated.

#### ❌ Missing `.env`?

Each script expects `.env` to be in the **same directory** or at project root.

---

### 5. **Run any demo**

Each folder (`02-log-summarization`, `03-alert-analysis`, etc.) has a README. Follow it to explore that use case.

---

## ✅ You’re Ready

You now have:

- ✅ API key configured
- ✅ Python environment working
- ✅ Basic call tested

Now pick a folder and start experimenting like a DevOps AI Wizard 🧙‍♂️

---

Need help? Open an issue

---
Enjoy learning, hacking, and building tools with LLMs! 🛠️
