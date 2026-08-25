# 🤖 AI Code Review Agent

> An AI-powered GitHub Pull Request review system designed to analyze code changes across bugs, security, performance, and code quality using FastAPI, LangGraph, Ollama, and Next.js.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![Next.js](https://img.shields.io/badge/Next.js-Frontend-black)
![LangGraph](https://img.shields.io/badge/LangGraph-AI-orange)
![Ollama](https://img.shields.io/badge/Ollama-LLM-purple)

---

## 📌 Overview

AI Code Review Agent is a developer-focused AI application that analyzes GitHub Pull Requests and generates structured review feedback.

The system is designed around multiple review areas:

* 🐞 Bug and logic analysis
* 🔒 Security-focused analysis
* ⚡ Performance considerations
* ✨ Code quality and style
* 📊 Overall review risk assessment

The goal is to help developers identify potential issues earlier in the Pull Request workflow.

---

## 🎯 Problem

Code review is an important part of software development, but reviewing Pull Requests manually can take significant time.

This project explores how an AI-based workflow can assist developers by automatically analyzing changed code and producing structured review feedback.

The system is intended as an **AI-assisted review tool**, not a replacement for human code reviewers.

---

## ✨ Features

* 🤖 AI-assisted Pull Request analysis
* 🔍 Multi-agent review workflow
* 🐞 Bug and logic analysis
* 🔒 Security-focused review
* ⚡ Performance suggestions
* ✨ Code quality feedback
* 📊 Review risk scoring
* 📈 Review analytics
* 🔗 GitHub integration
* 🌐 Web-based dashboard
* ⚡ FastAPI backend
* 🧠 Local LLM inference with Ollama

---

## 🏗️ Architecture

The high-level workflow is:

```text
GitHub Pull Request
        │
        ▼
GitHub API / Webhook
        │
        ▼
FastAPI Backend
        │
        ▼
LangGraph Workflow
        │
 ┌──────┼──────────┐
 │      │          │
 ▼      ▼          ▼
Bug   Security  Performance
Agent   Agent      Agent
 │      │          │
 └──────┼──────────┘
        ▼
   Style / Quality
       Agent
        │
        ▼
  Aggregator Agent
        │
        ▼
 Structured Review
        │
 ┌──────┴───────────┐
 ▼                  ▼
Dashboard       GitHub Output
```

The architecture separates the application into frontend, backend, AI agents, database, and service layers.

---

## 🧠 How It Works

1. A Pull Request is identified through GitHub integration.
2. The backend receives the Pull Request information.
3. Changed code is passed into the AI review workflow.
4. Specialized agents analyze different review dimensions.
5. Results are aggregated into a structured review.
6. The final review is exposed through the backend and application interface.

---

## 🛠️ Tech Stack

### Frontend

* Next.js
* React
* TypeScript
* Tailwind CSS

### Backend

* Python
* FastAPI
* SQLAlchemy
* Pydantic

### AI / LLM

* LangGraph
* Ollama
* Llama-family models

### Database

* SQLite

### Integration

* GitHub REST API

---

## 📂 Project Structure

```text
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
└── README.md
```

---

## ⚙️ Getting Started

### Prerequisites

Make sure the following are installed:

* Python 3.11+
* Node.js
* Ollama
* Git

---

## 1. Clone the Repository

```bash
git clone https://github.com/abdullahk970/AI-Code-Review-Agent.git

cd AI-Code-Review-Agent
```

---

## 2. Backend Setup

```bash
cd backend

python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 3. Environment Variables

Create a `.env` file inside the backend directory.

Example:

```env
GITHUB_TOKEN=your_github_token
DATABASE_URL=sqlite:///database.db
OLLAMA_BASE_URL=http://localhost:11434
MODEL=llama3
```

### Security

Do not commit real tokens or credentials to GitHub.

Use environment variables for sensitive configuration.

---

## 4. Start the Backend

From the backend directory:

```bash
uvicorn main:app --reload
```

The FastAPI development server should then be available locally.

---

## 5. Ollama Setup

Start Ollama:

```bash
ollama serve
```

Pull the model configured for the project:

```bash
ollama pull llama3
```

The exact model can be changed through the application's configuration.

---

## 6. Frontend Setup

Open a new terminal:

```bash
cd frontend

npm install

npm run dev
```

Then open the local development URL shown by Next.js.

---

## 📡 API

The project exposes backend endpoints for review and review-history functionality.

| Method | Endpoint   | Purpose                          |
| ------ | ---------- | -------------------------------- |
| GET    | `/`        | Backend health check             |
| POST   | `/review`  | Submit a Pull Request for review |
| GET    | `/reviews` | Retrieve review history          |
| GET    | `/stats`   | Retrieve review statistics       |

> Endpoint availability may depend on the current repository implementation and configuration.

---

## 📊 Review Output

A review is represented as structured information such as:

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

The exact output depends on the code under review and the configured model/workflow.

---

## 🧪 Evaluation

AI-generated code review should be evaluated carefully because LLM outputs can contain false positives or miss real issues.

Future evaluation for this project should measure areas such as:

* Bug-detection precision
* Security finding precision
* False-positive rate
* Review consistency
* Review latency
* Model/resource usage

No benchmark results are claimed here until they are measured on a defined evaluation dataset.

---

## 🔐 Security Considerations

The application interacts with GitHub and may process repository code.

Important considerations include:

* Keep GitHub tokens outside source code.
* Use environment variables for secrets.
* Validate GitHub webhook requests when webhooks are enabled.
* Avoid exposing sensitive repository information in logs.
* Restrict production CORS origins.
* Apply authentication and authorization before production deployment.

---

## ⚠️ Limitations

This project currently has several limitations that should be considered:

* AI-generated findings may contain false positives.
* AI models may miss subtle bugs or security vulnerabilities.
* Review quality depends on the selected LLM.
* Local inference requires suitable hardware and model resources.
* The current project is primarily intended as an AI engineering and development project rather than a certified production security/code-analysis system.

---

## 🔮 Future Improvements

Planned improvements include:

* Automated evaluation benchmarks
* Improved retrieval/context handling
* Additional review agents
* More structured review outputs
* GitHub Actions integration
* Docker-based deployment
* Additional LLM providers
* Improved authentication and security
* Review history and analytics improvements

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Make your changes.
4. Test the changes.
5. Commit and push your branch.
6. Open a Pull Request.

---

## 👨‍💻 Author

**Muhammad Abdullah Khan**

* GitHub: [abdullahk970](https://github.com/abdullahk970)
* LinkedIn: [Muhammad Abdullah Khan](https://www.linkedin.com/in/muhammad-abdullah-khan-9b0980316?utm_source=share_via&utm_content=profile&utm_medium=member_android)

---

## 📄 License

This project is licensed under the MIT License.
