# 03 – Alert Analysis

In this module, we demonstrate how to use an LLM to analyze DevOps-related alerts and generate human-readable summaries or explanations. This can be especially useful in:

- On-call situations
- Incident postmortems
- Ticket triaging

We'll also demonstrate how to send the summarized alert to **your Gmail inbox** – useful for live demo or team notifications.

---

## 🎯 Objective

- Parse alert text or payload
- Ask the LLM to explain what’s going on (error, severity, potential cause)
- Email the result to a designated address (e.g. your Gmail)

This example simulates receiving an alert from a monitoring tool or CI system.

---

## 📁 File Structure

```bash
03-alert-analysis/
├── analyze_alert.py         # Script to analyze and email alert summaries
├── sample_alert.txt         # Simulated alert example
├── .env.example             # API keys and email credentials
└── README.md
```

---

## 🛠 Requirements

- Python 3.9+
- `openai>=1.0.0`
- `python-dotenv`
- `smtplib` (built-in)

Install dependencies:

```bash
pip install openai python-dotenv
```

---

## 🔐 Environment Variables

Create a `.env` file based on `.env.example`:

```env
OPENAI_API_KEY=your-openai-key
GMAIL_USER=your-email@gmail.com
GMAIL_PASS=your-app-password
SEND_TO=your-email@gmail.com
```

> Gmail now requires you to use an **App Password** if 2FA is enabled: [https://myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)

---

## 🚀 How to Run

```bash
python analyze_alert.py sample_alert.txt
```

You will see:

- Console output of the LLM summary
- Email sent to your inbox

---

## 📄 sample_alert.txt (example input)

``` txt
ALERT: Memory usage on production-node-2 exceeds 92% for 5 minutes.
Current usage: 93.6%
Threshold: 90%
Severity: Critical
```

---

## 📤 Example Email Output

Subject: 🔔 Alert Summary – Memory Usage (Critical)

Body:

``` txt
The alert indicates that the memory usage on production-node-2 has been critically high (93.6%) for at least 5 minutes.

Potential Cause:
- Memory leak in an application
- Improper resource allocation

Suggested Action:
- Check processes using most memory
- Restart services if needed
```

---

## ⚠️ Notes

- Do not expose your Gmail credentials in production!
- Use this only as a prototype – in real systems use secure tokens, audit logs, and alert pipelines.

---

This is how we make alerts understandable – instantly 📬🤖
