# Agentic Recruiting Copilot

This project was built for the **IBM watsonx Orchestrate Hackathon** to demonstrate how agentic AI can transform recruiting workflows.

##  Problem Statement
Recruiters spend too much time on repetitive tasks:
- Writing outreach emails
- Scheduling meetings
- Updating ATS records
- Notifying hiring managers

These manual steps slow down hiring and reduce time for meaningful candidate engagement.

##  Solution
We created an **Agentic Recruiting Copilot** powered by **IBM watsonx Orchestrate**.  
It automates recruiting workflows end‑to‑end while keeping humans in the loop for approvals.

### How watsonx Orchestrate is used
- **Workflow orchestration**: Orchestrate defines and runs the recruiting workflow (triage → ATS update → draft outreach → send email → calendar hold → Slack update → ATS stage update).
- **Digital skills**: Each task (email, calendar, Slack, ATS) is implemented as a skill that Orchestrate can call.
- **Human approval**: Orchestrate pauses at the outreach draft step until the recruiter approves.
- **Integrations**: Orchestrate connects across apps (email, calendar, Slack, ATS) to execute tasks.
- **Audit trail**: Orchestrate provides execution history, which we display in the Streamlit UI.

##  Workflow
1. Candidate triage (input details)
2. ATS upsert (add/update candidate record)
3. Draft outreach email (approval required)
4. Send email
5. Create calendar hold
6. Post Slack update
7. Update ATS stage
8. Timeline + artifacts shown in UI

##  Tech Stack
- **IBM watsonx Orchestrate** → workflow orchestration, approvals, skill execution
- **Python + Streamlit** → simple front‑end UI
- **Custom Python endpoints** → registered as Orchestrate skills (email, calendar, Slack, ATS)

##  Impact
- Saves recruiters hours of manual work
- Ensures consistency and transparency
- Augments human potential with agentic AI
- Demonstrates how **watsonx Orchestrate** can redefine productivity in HR

