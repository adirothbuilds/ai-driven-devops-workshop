# Makefile for AI-Driven DevOps Workshop

# Variables
PRESENTATION_FILE=presentation.md
OUTPUT_FILE=slides.html
CHROME_PATH=/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome

# Default target
.PHONY: all
all: open-presentation

# Generate and open the presentation in Chrome
.PHONY: open-presentation
open-presentation:
	@echo "Generating and opening presentation..."
	marp $(PRESENTATION_FILE) --html --output $(OUTPUT_FILE)
	open $(OUTPUT_FILE)

# Run each step of the workshop
.PHONY: step-01
step-01:
	@echo "Running Step 01: LLM Basics..."
	python 01-llm-basics/basic_prompt_call.py

.PHONY: step-02
step-02:
	@echo "Running Step 02: Log Summarization..."
	python 02-log-summarization/summarize_log.py 02-log-summarization/logs/sample.log

.PHONY: step-03
step-03:
	@echo "Running Step 03: Alert Analysis..."
	python 03-alert-analysis/analyze_alert.py 03-alert-analysis/sample_alert.txt

.PHONY: step-04-01
step-04-01:
	@echo "Running Step 04-01: Prompt Engineering..."
	python 04-prompt-engineering/01-direct-vs-system.py

.PHONY: step-04-02
step-04-02:
	@echo "Running Step 04-02: Prompt Steering..."
	python 04-prompt-engineering/02-steering-options.py

.PHONY: step-04-03
step-04-03:
	@echo "Running Step 04-03: Prompt Ranking..."
	python 04-prompt-engineering/03-ranked-prompt.py

.PHONY: step-05
step-05:
	@echo "Running Step 05: RAG with Dev Docs..."
	python 05-rag-with-dev-docs/ask_with_context.py 05-rag-with-dev-docs/sample_readme.md

.PHONY: step-06
step-06:
	@echo "Running Step 06: CI Integration..."
	python 06-ci-integration/summarize_ci_log.py 06-ci-integration/ci_log_example.txt

.PHONY: step-07
step-07:
	@echo "Running Step 07: CLI Agent Demo..."
	python 07-cli-agent-demo/devops_agent.py

.PHONY: step-08
step-08:
	@echo "Running Step 08: Tool Execution..."
	python 08-tool-execution/dockerfile_agent.py
