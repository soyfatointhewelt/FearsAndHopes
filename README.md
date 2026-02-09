# Introduction
## Motivation

This project was developed while taking a break of studying to finals, to support ongoing research on how people perceive and interact with AI agents in work contexts.

As AI systems become increasingly integrated into everyday decision-making and professional environments, understanding human expectations, concerns, and emotional responses is essential for designing responsible and human-centered AI.

Through this work, I aim to contribute to meaningful research that helps ensure technological progress aligns with societal values and supports positive impact. Where can I help?

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
