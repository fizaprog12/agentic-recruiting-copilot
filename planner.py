def plan(goal: dict):
    steps = [
        {"id": "parse", "action": "triage"},
        {"id": "ats_upsert", "action": "ats_upsert"},
        {"id": "outreach_draft", "action": "email_draft", "approve": True},
        {"id": "outreach_send", "action": "email_send"},
        {"id": "calendar_hold", "action": "calendar_hold"},
        {"id": "slack_notify", "action": "slack_update"},
        {"id": "ats_stage", "action": "ats_stage"},
    ]
    return steps
