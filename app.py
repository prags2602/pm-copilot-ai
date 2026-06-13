import streamlit as st

st.set_page_config(page_title="Project Manager Copilot AI", layout="wide")

st.title("🧠 Project Manager Copilot AI")
st.write("Advanced Project Risk & Decision Assistant")

update = st.text_area("Enter Project Update", height=200)

# -----------------------------
# RISK DETECTION
# -----------------------------
def detect_risks(text):
    text = text.lower()
    risks = []

    if "delay" in text or "late" in text:
        risks.append(("Schedule Risk", "High"))

    if "qa" in text or "testing" in text:
        risks.append(("Resource Risk", "Medium"))

    if "client" in text or "change" in text:
        risks.append(("Scope Creep", "Medium"))

    if "blocked" in text or "dependency" in text:
        risks.append(("Dependency Blocker", "High"))

    return risks


# -----------------------------
# TASK EXTRACTION
# -----------------------------
def extract_tasks(text):
    tasks = []

    text = text.lower()

    if "delay" in text:
        tasks.append("Resolve delayed deliverables")

    if "qa" in text:
        tasks.append("Assign backup QA engineer")

    if "client" in text:
        tasks.append("Review client change request")

    if "blocked" in text:
        tasks.append("Resolve dependency blocker")

    if not tasks:
        tasks.append("Continue normal execution")

    return tasks


# -----------------------------
# HEALTH SCORE
# -----------------------------
def health_score(risks):
    score = 100

    for r, level in risks:
        if level == "High":
            score -= 25
        elif level == "Medium":
            score -= 15

    return max(score, 0)


# -----------------------------
# TIMELINE IMPACT
# -----------------------------
def timeline_impact(risks):
    if any(level == "High" for _, level in risks):
        return "6–10 days delay risk"
    elif any(level == "Medium" for _, level in risks):
        return "3–5 days delay risk"
    else:
        return "0–2 days delay risk"


# -----------------------------
# EMAIL GENERATOR
# -----------------------------
def generate_email(risks, tasks, score, timeline):
    risk_text = "\n".join([f"- {r} ({lvl})" for r, lvl in risks]) if risks else "- No critical risks identified"
    task_text = "\n".join([f"- {t}" for t in tasks])

    email = f"""
Subject: Project Status Update Report

Dear Stakeholders,

Here is the latest project status report:

📊 Health Score: {score}/100  
⏱ Timeline Impact: {timeline}

⚠️ Risks Identified:
{risk_text}

📌 Key Tasks:
{task_text}

🛠 Recommendations:
- Prioritize high-risk issues immediately
- Monitor medium-risk items closely
- Ensure daily tracking of progress
- Communicate updates proactively

Regards,  
Pragya Dhanda  
Delivery Manager
"""
    return email


# -----------------------------
# MAIN APP
# -----------------------------
if st.button("Analyze Project"):

    risks = detect_risks(update)
    tasks = extract_tasks(update)
    score = health_score(risks)
    timeline = timeline_impact(risks)
    email = generate_email(risks, tasks, score, timeline)

    # DASHBOARD
    st.subheader("📊 Project Dashboard")

    col1, col2, col3 = st.columns(3)

    col1.metric("Health Score", f"{score}/100")

    if score > 75:
        col2.success("Healthy")
    elif score > 50:
        col2.warning("At Risk")
    else:
        col2.error("Critical")

    col3.metric("Timeline Impact", timeline)

    # RISKS
    st.subheader("⚠️ Risks")

    if risks:
        for r, level in risks:
            st.write(f"- {r} ({level})")
    else:
        st.success("No major risks detected")

    # TASKS
    st.subheader("📌 Extracted Tasks")

    for t in tasks:
        st.write("• " + t)

    # ACTIONS
    st.subheader("🛠️ Recommendations")

    st.write("""
    - Escalate high-risk issues immediately  
    - Monitor medium risks  
    - Conduct daily status review  
    - Communicate with stakeholders  
    """)

    # SUMMARY
    st.subheader("📩 Executive Summary")

    st.write(
        "Automated analysis completed. Risks, tasks, and timeline impact generated "
        "to assist project decision-making."
    )

    # EMAIL OUTPUT
    st.subheader("✉️ Stakeholder Email")

    st.code(email)