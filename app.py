import streamlit as st
from memory import Memory
from planner import plan
from orchestrator import execute_step

st.title("Agentic Recruiting Copilot")

with st.form("candidate"):
    candidate_email = st.text_input("Candidate email", "jane@example.com")
    candidate_name = st.text_input("Candidate name", "Jane Doe")
    role = st.text_input("Target role", "Senior Data Scientist")
    manager_email = st.text_input("Hiring manager email", "manager@example.com")
    slack_channel = st.text_input("Slack channel", "hiring")
    preferred_slot = st.text_input("Preferred slot", "Wed 2pm")
    approve_draft = st.checkbox("Require approval for outreach draft", True)
    submitted = st.form_submit_button("Run workflow")

if submitted:
    mem = Memory()
    cid = mem.new_case({"role": role, "candidate_email": candidate_email})
    ctx = {
        "role": role,
        "candidate_email": candidate_email,
        "candidate_name": candidate_name,
        "manager_email": manager_email,
        "slack_channel": slack_channel,
        "preferred_slot": preferred_slot,
    }
    steps = plan({"role": role, "candidate_email": candidate_email})

    for s in steps:
        res = execute_step(s, ctx, mem, cid)

        if s.get("approve") and approve_draft and s["action"] == "email_draft":
            st.subheader("Approve outreach draft")
            st.text_input("Subject", value=res["draft"]["subject"], key="subject")
            st.text_area("Body", value=res["draft"]["body"], key="body", height=200)
            approve = st.button("Approve and continue")
            if not approve:
                st.info("Waiting for approval...")
                st.stop()
            else:
                ctx["draft"] = {
                    "subject": st.session_state["subject"],
                    "body": st.session_state["body"]
                }
        else:
            if s["action"] == "email_draft":
                ctx["draft"] = res["draft"]
            if s["action"] == "triage":
                ctx["profile"] = res["profile"]

    st.success("Workflow complete. See timeline and artifacts below.")
    st.json(mem.state[cid]["timeline"])
    st.json(mem.state[cid]["artifacts"])
