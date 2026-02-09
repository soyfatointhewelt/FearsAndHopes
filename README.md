# Introduction

# Hopes & Fears Study (Streamlit)

A multi-step Streamlit survey prototype (Pages 1–4) that collects participant inputs and appends responses to a CSV file.

## Features
- Step-based navigation (session_state router)
- Mandatory fields + validation (min 70 chars where required)
- Task Automation Gallery with “view at least N tasks” gating
- Saves results by appending one row per participant to:
  `~/Downloads/hopes_fears_study_responses.csv` (local runs)

## Run locally
<img width="1187" height="589" alt="image" src="https://github.com/user-attachments/assets/34cb8af1-5485-473c-8ac3-6da42174fad2" />
<img width="1187" height="589" alt="image" src="https://github.com/user-attachments/assets/34cb8af1-5485-473c-8ac3-6da42174fad2" />

1) Create and activate a virtual environment (optional but recommended)
```bash
python3 -m venv .venv
source .venv/bin/activate
