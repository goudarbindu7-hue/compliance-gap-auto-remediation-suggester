
# Tool-89 — AI Developer 2 (Complete All-Days Pack)

This repository contains:
1) A **production-ready AI service** (Flask + Groq)  
2) **Day-by-day deliverables (Day 1 → Day 20)** aligned to the capstone plan  
3) Security, tests, Docker, and demo assets

## Structure
- ai-service/            → Complete AI microservice
- days/                  → Daily tasks, checklists, and artifacts (Day 1–20)
- docs/                  → Extra docs (demo script, architecture)

## Quick Start
```bash
cd ai-service
cp .env.example .env
pip install -r requirements.txt
python app.py
```

Health: http://localhost:5000/health

## Demo Flow (6 mins)
1. Create record from backend (or simulate via POST)
2. POST /describe → show description
3. POST /recommend → show 3 actions
4. POST /generate-report → show structured report
5. GET /health → show uptime

