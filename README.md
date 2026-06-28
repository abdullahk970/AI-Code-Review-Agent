# 🤖 AI Code Review Agent

> An AI-powered GitHub Pull Request review system that automatically analyzes code for **bugs, security vulnerabilities, performance issues, and code quality** using **FastAPI, LangGraph, Ollama, and Next.js**.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![Next.js](https://img.shields.io/badge/Next.js-Frontend-black)
![LangGraph](https://img.shields.io/badge/LangGraph-AI-orange)
![Ollama](https://img.shields.io/badge/Ollama-LLM-purple)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

# 🚀 Overview

AI Code Review Agent is an intelligent code review platform that automates GitHub Pull Request reviews using AI. Instead of waiting for manual reviews, developers receive detailed feedback within seconds.

The system analyzes code changes across multiple dimensions including:

* 🐞 Bugs & Logic Errors
* 🔒 Security Vulnerabilities
* ⚡ Performance Issues
* ✨ Code Style & Best Practices

Each review includes a **risk score**, **decision status**, and actionable suggestions to improve code quality before merging.

---

# ✨ Features

* 🤖 AI-powered Pull Request Reviews
* 🔍 Multi-Agent Code Analysis
* 🔒 Security Vulnerability Detection
* ⚡ Performance Optimization Suggestions
* 🐛 Bug Detection
* ✨ Code Style Review
* 📊 Risk Score Generation
* 📈 Analytics Dashboard
* 🔗 GitHub Integration
* 💬 Detailed AI Feedback
* 🌐 Modern Next.js Dashboard
* 🚀 FastAPI REST API

---

# 🏗️ Tech Stack

### Frontend

* Next.js
* React
* TypeScript
* Tailwind CSS

### Backend

* FastAPI
* Python
* SQLAlchemy
* Pydantic

### AI

* LangGraph
* Ollama
* Llama Models

### Database

* SQLite
* PostgreSQL (Production Ready)

### APIs

* GitHub REST API

---

# 🧠 How It Works

```text
Developer Opens PR
        │
        ▼
GitHub Webhook/API
        │
        ▼
FastAPI Backend
        │
        ▼
LangGraph AI Workflow
        │
 ┌──────┼────────┐
 │      │        │
 ▼      ▼        ▼
Bug   Security  Performance
Agent   Agent      Agent
        │
        ▼
 Style Agent
        │
        ▼
 Aggregator Agent
        │
        ▼
 Final AI Review
        │
        ▼
 Dashboard + GitHub Comments
```

---

# 📂 Project Structure

```bash
AI-Code-Review-Agent/
│
├── backend/
│   ├── agents/
│   ├── api/
│   ├── database/
│   ├── models/
│   ├── services/
│   ├── utils/
│   └── main.py
│
├── frontend/
│   ├── app/
│   ├── components/
│   ├── hooks/
│   └── lib/
│
├── screenshots/
├── README.md
└── docker-compose.yml
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/AI-Code-Review-Agent.git

cd AI-Code-Review-Agent
```

---

## Backend Setup

```bash
cd backend

python -m venv venv

# Windows
venv\Scripts\activate

# Linux / Mac
source venv/bin/activate

pip install -r requirements.txt
```

Create `.env`

```env
GITHUB_TOKEN=your_github_token
DATABASE_URL=sqlite:///database.db
OLLAMA_BASE_URL=http://localhost:11434
MODEL=llama3
```

Run Backend

```bash
uvicorn main:app --reload
```

---

## Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

---

# 🤖 Ollama Setup

Install Ollama

```bash
ollama serve
```

Pull model

```bash
ollama pull llama3
```

---

# 📡 API Endpoints

| Method | Endpoint | Description         |
| ------ | -------- | ------------------- |
| GET    | /        | Health Check        |
| POST   | /review  | Review Pull Request |
| GET    | /reviews | Review History      |
| GET    | /stats   | Dashboard Analytics |

---

# 📊 AI Review Output

Each review contains:

* Overall Risk Score
* Review Decision
* Bug Analysis
* Security Findings
* Performance Suggestions
* Style Improvements
* AI Summary

Example:

```json
{
  "risk_score": 28,
  "decision": "MINOR_FIXES",
  "bugs": 2,
  "security": 1,
  "performance": 0,
  "style": 4
}
```

---

# 📸 Screenshots

Add screenshots inside a **screenshots/** folder.

Example:

```
screenshots/
│
├── dashboard.png
├── review.png
├── analytics.png
```

Then display them using:

```md
![Dashboard](screenshots/dashboard.png)

![Review](screenshots/review.png)
```

---

# 🎯 Use Cases

* Software Development Teams
* Open Source Projects
* Startups
* Enterprise Applications
* Educational Institutions
* CI/CD Automation
* GitHub Pull Request Reviews

---

# 📈 Future Improvements

* GitLab Support
* Bitbucket Integration
* Slack Notifications
* Email Reports
* SonarQube Integration
* Docker Deployment
* Kubernetes Support
* Multi-LLM Support (OpenAI, Claude, Gemini)

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new feature branch
3. Commit your changes
4. Push the branch
5. Open a Pull Request

---

# 📜 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Abdullah Khan**

GitHub: https://github.com/abdullahk970

---

## ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub. It helps others discover the project and supports future development.
