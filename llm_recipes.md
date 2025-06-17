# LLM Prompt Engineering – Cheatsheet

This is a quick reference for crafting better prompts and understanding how LLMs behave in DevOps workflows.

---

## 🧠 Prompt Anatomy

```txt
System: Defines the assistant's behavior and tone
User: The question or request
Assistant: The model's response
```

### ✅ Good Prompt Example

```txt
System: You are a DevOps assistant. Be concise and follow best practices.
User: How do I reduce Docker image size?
```

---

## 🎛 Model Parameters (OpenAI)

| Parameter     | Description                                              | Recommended |
|---------------|----------------------------------------------------------|-------------|
| `temperature` | Creativity vs. determinism (0 = consistent, 1 = diverse) | `0.3 – 0.7`  |
| `top_p`       | Alternative to temperature, controls diversity           | Leave default |
| `max_tokens`  | Max length of response                                  | `512 – 2048` |
| `stop`        | Strings that will stop generation                       | Optional     |

---

## 🧩 Prompt Engineering Tips

- Start with clear **System Prompt**.
- Use delimiters (`###`, triple backticks) for inputs when needed.
- If the model hallucinates → **Add constraints** in the prompt.
- Break large requests into smaller steps.
- Give examples inside prompt if consistency is needed.

---

## 🧪 Use Case Patterns

| Goal                    | Prompt Pattern                                |
|-------------------------|-----------------------------------------------|
| Summarize logs          | "Summarize the following logs: [logs]"        |
| Generate Dockerfile     | "Generate a Dockerfile for a [desc] app"        |
| Explain a tool          | "Explain how [tool] works in CI/CD pipeline"  |
| Fix error               | "Here’s a CI error log. Suggest a fix: [log]"  |

---

## 🚨 Common Pitfalls

- ❌ No system prompt → Output may drift
- ❌ Too vague → Model guesses what you mean
- ❌ Too long input → May get truncated or ignored

---

## 📦 Suggested Model

Use `gpt-3.5-turbo` for quick DevOps use cases.
If latency isn't an issue, `gpt-4` is more robust for multi-step reasoning.

---
Happy prompting! 🧙‍♂️
