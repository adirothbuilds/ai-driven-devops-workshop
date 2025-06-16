# 📄 Prompt Templates for DevOps LLM Workflows

Use these pre-built prompt formats when integrating LLMs into your DevOps workflows.

---

## 🔧 Logs & Errors

**Simple log summary:**

``` txt
Summarize the following log output and highlight any errors or unusual events:
[LOG CONTENT HERE]
```

**Explain an error:**

``` txt
Explain what this error message means and how to resolve it:
[ERROR MESSAGE HERE]
```

**Translate logs to plain English:**

``` txt
Read the following log and translate it into a human-friendly summary:
[LOG CONTENT HERE]
```

---

## 🚀 CI/CD Pipelines

**Pipeline issue analysis:**

``` txt
Our build failed. Here's the error from the CI log. What went wrong?
[CI LOG CONTENT HERE]
```

**Suggest pipeline optimization:**

``` txt
Here's a Jenkins pipeline config. How can we make it more efficient or secure?
[PIPELINE YAML HERE]
```

---

## 🐳 Docker & Infra

**Reduce Docker image size:**

``` txt
How can I reduce the size of this Docker image based on the following Dockerfile?
[DOCKERFILE HERE]
```

**Explain Docker error:**

``` txt
What does this Docker build error mean?
[ERROR HERE]
```

**DevOps bot persona:**

``` txt
You are a senior DevOps engineer. Help me understand this infrastructure problem and recommend solutions.
[INPUT]
```

---

## 📦 Package & Security

**Vulnerability fix prompt:**

``` txt
We found this vulnerability in our image/package. What steps should we take to mitigate or patch it?
[VULN INFO HERE]
```

**Dependency conflict resolution:**

``` txt
Help resolve this dependency conflict between Python packages:
[CONFLICT DETAILS]
```

---

Customize these prompts as needed and feel free to embed context using tools like RAG or history chaining.
