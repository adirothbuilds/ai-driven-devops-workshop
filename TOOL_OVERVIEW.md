# 🛠️ Tooling Overview – Agent-Oriented Development

This file provides a concise overview of the major agent orchestration tools covered or referenced in this workshop.
It helps clarify use cases and ideal tool choices when building AI-powered DevOps automations.

---

## 1. `n8n` – Visual Automation Platform

**Type:** No-code / low-code workflow automation

**Best For:**

- Connecting APIs, databases, and apps
- Visual automation with AI agents
- External triggers (webhooks, cron, Telegram, etc.)

**Strengths:**

- Great for glue logic between tools
- Easy integration of OpenAI, Gmail, Airtable, etc.
- Supports Agent Memory, Custom Tools, and HTTP callouts

**Weaknesses:**

- Logic-heavy or stateful workflows can get messy
- Limited native support for real-time async agent loops

---

## 2. `LangChain` – LLM Application Framework

**Type:** Python/JS SDK for building LLM apps

**Best For:**

- Building structured LLM applications
- Prompt templates, chains, memory
- Agents that select tools and invoke logic

**Strengths:**

- Mature ecosystem
- Tool and memory abstractions
- Community recipes and templates

**Weaknesses:**

- Can be heavy for simple use cases
- Requires careful debugging with agents

---

## 3. `LangGraph` – Graph-based Agent Workflows

**Type:** Experimental framework built on top of LangChain

**Best For:**

- Multi-step agent workflows
- Directed graphs with condition-based execution

**Strengths:**

- Fine-grained control over flow
- Reusability and composability
- Supports state tracking

**Weaknesses:**

- Still evolving
- Requires deeper understanding of graph structures

---

## 4. `FlowiseAI` – Visual LLM Agent Builder (optional)

**Type:** Visual interface over LangChain/LLM logic

**Best For:**

- Quickly prototyping agents with a UI
- Integrating chains visually like Node-RED

**Strengths:**

- No-code access to LangChain logic
- Supports OpenAI, tools, memory, and more

**Weaknesses:**

- Limited flexibility for advanced logic
- Not used directly in this workshop

**Recommendation:** Try as a sandbox to explore agent behavior before going into code.

---

## Summary Table

| Tool         | Use Case                            | Best For                          | Type        |
|--------------|-------------------------------------|-----------------------------------|-------------|
| `n8n`        | Workflow + orchestration            | Glue logic, triggers, bots        | Visual       |
| `LangChain`  | Chain logic, tool agents            | LLM apps with structured steps    | Code SDK     |
| `LangGraph`  | Graph-controlled agent execution    | Stateful, multi-path workflows    | Code SDK     |
| `FlowiseAI`  | Visual LangChain interface          | Prototyping agents                | Visual (web) |

---

Feel free to expand or adjust based on future tools or needs.
