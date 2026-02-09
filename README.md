# Introduction
## Motivation
Help contribuiting to the mainful research my professor is doing to leave the world better than i found it, this world has given so much, deserves so much better, where can i help?

# Hopes & Fears Study (Streamlit)

A multi-step Streamlit survey prototype (Pages 1–4) that collects participant inputs and appends responses to a CSV file.

## My understanding of the Research Purpose

This prototype wants to be developed to explore:

- Perceptions of AI Agents in the workplace
- Emotional responses (fears and hopes)
- Interaction with task automation scenarios
- Behavioral exploration patterns within a task gallery

The application collects responses and stores them in a CSV file for analysis.

## Features
- Step-based navigation (session_state router)
- Mandatory fields + validation (min 70 chars where required)
- Task Automation Gallery with “view at least N tasks” gating
- Saves results by appending one row per participant to:
  `~/Downloads/hopes_fears_study_responses.csv` (local runs)

## My process thinking
<img width="1187" height="589" alt="image" src="https://github.com/user-attachments/assets/34cb8af1-5485-473c-8ac3-6da42174fad2" />
<img width="1187" height="589" alt="image" src="https://github.com/user-attachments/assets/34cb8af1-5485-473c-8ac3-6da42174fad2" />

## Run locally
1) Create and activate a virtual environment (optional but recommended)
```bash
python3 -m venv .venv
source .venv/bin/activate

## Data Output

Responses are saved locally as:

Downloads/hopes_fears_study_responses.csv

Each row contains:
- Prolific ID
- Occupation
- AI description
- Fear/Hope ratings
- Text responses
- Tasks viewed
