import streamlit as st
import pandas as pd
import os
from datetime import datetime

# =========================
# Config
# =========================
st.set_page_config(page_title="Hopes & Fears Study", layout="wide")

CSV_PATH = "responses.csv"
MIN_CHARS = 70
MAX_CHARS = 350

SHARED_LABELS = [
    "Not at all",
    "Rarely",
    "Occasionally",
    "Moderately",
    "Often",
    "Very often",
    "Almost always",
]

TASKS = [
    # You can replace these with your real tasks later
    {"title": "Email triage", "potential": "High", "description": "Automatically categorize + summarize inbox threads."},
    {"title": "Invoice data entry", "potential": "High", "description": "Extract fields from PDFs and pre-fill accounting system."},
    {"title": "Meeting notes", "potential": "Medium", "description": "Summarize calls and draft action items."},
    {"title": "Customer support replies", "potential": "Medium", "description": "Draft first-response templates for common issues."},
    {"title": "Calendar scheduling", "potential": "Low", "description": "Suggest slots and propose invites with constraints."},
    {"title": "Weekly KPI report", "potential": "High", "description": "Pull metrics + generate a short narrative update."},
    {"title": "Research literature scan", "potential": "Medium", "description": "Find + cluster relevant papers and produce a summary."},
    {"title": "Code review suggestions", "potential": "Medium", "description": "Suggest improvements and flag possible bugs."},
    {"title": "Expense categorization", "potential": "High", "description": "Classify expenses and detect anomalies."},
    {"title": "Slide drafting", "potential": "Medium", "description": "Turn bullet notes into a structured slide outline."},
    {"title": "Transcription cleanup", "potential": "High", "description": "Clean transcripts and highlight key quotes."},
    {"title": "Personalized learning plan", "potential": "Low", "description": "Recommend study steps and practice based on progress."},
]

# =========================
# Helpers
# =========================
def init_state():
    defaults = {
        "page": 1,
        # page 1
        "prolific_id": "",
        "occupation": "",
        # page 2
        "fear_rating": 2,
        "fear_text": "",
        "fear_shared": SHARED_LABELS[0],
        "hope_rating": 4,
        "hope_text": "",
        "hope_shared": SHARED_LABELS[0],
        # page 3
        "clicked_tasks": set(),
        "selected_task": None,  # for modal-like detail
        "saved": False,
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v


def go(n: int):
    st.session_state.page = n
    st.rerun()


def append_to_csv(row: dict, csv_path: str = CSV_PATH):
    df_new = pd.DataFrame([row])
    file_exists = os.path.exists(csv_path)
    df_new.to_csv(csv_path, mode="a", header=not file_exists, index=False)


# =========================
# Basic styles (optional)
# =========================
st.markdown(
    """
<style>
.block-container {max-width: 1200px; padding-top: 2rem;}
.page-title {text-align:center; font-weight: 900; letter-spacing: .5px; margin-bottom: 1.2rem;}
.small-help {opacity: .75;}
.task-tile button {width: 100%;}
</style>
""",
    unsafe_allow_html=True,
)

init_state()

# =========================
# PAGE 1 — Intro
# =========================
def page1():
    st.markdown('<div class="page-title">WE ARE EXPLORING FEARS & HOPES ABOUT AI AGENTS</div>', unsafe_allow_html=True)
    st.write(
        """
**In this survey, you will be asked to:**
- Task 1: Share your fears and hopes about AI Agents
- Task 2: Explore a Task Automation Gallery
- Task 3: Submit your responses

All questions are mandatory.
"""
    )

    st.write("")
    st.text_input("Please enter your Prolific ID", key="prolific_id", placeholder="e.g., 5f2c...")

    st.text_input("What is your occupation?", key="occupation", placeholder="e.g., Student, Data Analyst...")

    # Validation
    ok = len(st.session_state.prolific_id.strip()) > 0 and len(st.session_state.occupation.strip()) > 0
    if not ok:
        st.info("Please fill in both fields to continue.")

    c1, c2, c3 = st.columns([1, 6, 2])
    with c3:
        st.button("Start survey →", disabled=not ok, type="primary", on_click=lambda: go(2))


# =========================
# PAGE 2 — Fears & Hopes
# =========================
def page2():
    st.markdown('<div class="page-title">TELL US ABOUT YOUR FEARS AND HOPES</div>', unsafe_allow_html=True)

    left, right = st.columns(2, gap="large")

    with left:
        st.subheader("I rate my fears about AI Agents as")
        st.slider("", 1, 7, key="fear_rating", label_visibility="collapsed")
        c1, c2 = st.columns(2)
        with c1: st.caption("No fear at all")
        with c2: st.caption("Terrified")

        st.subheader("I fear AI Agents because…")
        st.text_area(
            "",
            key="fear_text",
            height=180,
            max_chars=MAX_CHARS,
            placeholder="Write your fears here",
            label_visibility="collapsed",
        )
        fear_count = len(st.session_state.fear_text.strip())
        st.caption(f"{fear_count}/{MAX_CHARS} (Min. {MIN_CHARS} characters)")

        st.subheader("To what extent do you believe your fears are shared by most people?")
        st.radio(
            "",
            options=SHARED_LABELS,
            key="fear_shared",
            horizontal=True,
            label_visibility="collapsed",
        )

    with right:
        st.subheader("I rate my hopes about AI Agents as")
        st.slider("", 1, 7, key="hope_rating", label_visibility="collapsed")
        c1, c2 = st.columns(2)
        with c1: st.caption("No hope at all")
        with c2: st.caption("Full of hope")

        st.subheader("I have hope in AI Agents because…")
        st.text_area(
            "",
            key="hope_text",
            height=180,
            max_chars=MAX_CHARS,
            placeholder="Write your hopes here",
            label_visibility="collapsed",
        )
        hope_count = len(st.session_state.hope_text.strip())
        st.caption(f"{hope_count}/{MAX_CHARS} (Min. {MIN_CHARS} characters)")

        st.subheader("To what extent do you believe your hopes are shared by most people?")
        st.radio(
            "",
            options=SHARED_LABELS,
            key="hope_shared",
            horizontal=True,
            label_visibility="collapsed",
        )

    # Validation
    fear_ok = len(st.session_state.fear_text.strip()) >= MIN_CHARS
    hope_ok = len(st.session_state.hope_text.strip()) >= MIN_CHARS
    can_next = fear_ok and hope_ok

    st.write("---")
    if not can_next:
        st.warning("Please write at least 70 characters for BOTH fears and hopes to continue.")

    c1, c2, c3 = st.columns([1, 6, 2])
    with c1:
        st.button("← Back", on_click=lambda: go(1))
    with c3:
        st.button("Next →", disabled=not can_next, type="primary", on_click=lambda: go(3))


# =========================
# PAGE 3 — Gallery + Save
# =========================
def page3():
    st.markdown('<div class="page-title">TASK AUTOMATION GALLERY</div>', unsafe_allow_html=True)
    st.caption("Click at least 3 tasks. When ready, save your answers to the CSV.")

    # Grid layout
    cols_per_row = 4
    for i in range(0, len(TASKS), cols_per_row):
        row = st.columns(cols_per_row, gap="medium")
        for j, task in enumerate(TASKS[i : i + cols_per_row]):
            with row[j]:
                pot = task["potential"]
                # simple color hint
                badge = "🟥 High" if pot == "High" else ("🟨 Medium" if pot == "Medium" else "🟩 Low")

                st.markdown(f"**{task['title']}**  \n<span class='small-help'>{badge}</span>", unsafe_allow_html=True)

                if st.button("Open", key=f"open_{i+j}"):
                    st.session_state.selected_task = task["title"]

                # Track clicks as “explored”
                if st.button("Mark as explored", key=f"explore_{i+j}"):
                    st.session_state.clicked_tasks.add(task["title"])

                st.caption(f"Explored: {'✅' if task['title'] in st.session_state.clicked_tasks else '—'}")

    st.write("---")

    # Details area
    if st.session_state.selected_task:
        t = next((x for x in TASKS if x["title"] == st.session_state.selected_task), None)
        if t:
            st.subheader(f"Task: {t['title']}")
            st.write(f"**Automation potential:** {t['potential']}")
            st.write(t["description"])
            st.button("Close details", on_click=lambda: st.session_state.update({"selected_task": None}))

    explored_count = len(st.session_state.clicked_tasks)
    st.info(f"Tasks explored: **{explored_count}** / 3 minimum")

    can_save = explored_count >= 3

    # Save row
    st.write("")
    c1, c2, c3 = st.columns([1, 6, 2])
    with c1:
        st.button("← Back", on_click=lambda: go(2))

    with c3:
        if st.button("Save responses →", disabled=not can_save, type="primary"):
            row = {
                "timestamp": datetime.utcnow().isoformat(),
                "prolific_id": st.session_state.prolific_id.strip(),
                "occupation": st.session_state.occupation.strip(),
                "fear_rating": st.session_state.fear_rating,
                "fear_text": st.session_state.fear_text.strip(),
                "fear_shared": st.session_state.fear_shared,
                "hope_rating": st.session_state.hope_rating,
                "hope_text": st.session_state.hope_text.strip(),
                "hope_shared": st.session_state.hope_shared,
                "tasks_explored": ";".join(sorted(st.session_state.clicked_tasks)),
            }
            append_to_csv(row, CSV_PATH)
            st.session_state.saved = True

    if st.session_state.saved:
        st.success(f"Saved ✅ to `{CSV_PATH}` (in your project folder).")


# =========================
# Router
# =========================
if st.session_state.page == 1:
    page1()
elif st.session_state.page == 2:
    page2()
else:
    page3()
