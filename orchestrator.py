from skills import email as Email, cal_tool as Cal, slack as Slack, ats as ATS

def execute_step(step, ctx, memory, cid):
    act = step["action"]

    if act == "triage":
        profile = {
            "name": ctx.get("candidate_name", "Candidate"),
            "email": ctx["candidate_email"],
            "role": ctx["role"],
            "skills": ctx.get("skills", [])
        }
        memory.log(cid, {"event": "triage", "profile": profile})
        return {"profile": profile}

    if act == "ats_upsert":
        res = ATS.upsert_candidate(ctx["profile"])
        memory.log(cid, {"event": "ats_upsert", "res": res})
        return res

    if act == "email_draft":
        draft = Email.draft_email({
            "role": ctx["role"],
            "name": ctx.get("candidate_name", "there")
        })
        memory.log(cid, {"event": "email_draft", "draft": draft})
        return {"draft": draft}

    if act == "email_send":
        d = ctx["draft"]
        to = ctx["candidate_email"]
        res = Email.send_email(to, d["subject"], d["body"])
        memory.log(cid, {"event": "email_send", "res": res})
        return res

    if act == "calendar_hold":
        slot = ctx.get("preferred_slot", "Wed 2pm")
        evt = Cal.create_event(
            f"Intro: {ctx['role']}",
            [ctx["candidate_email"], ctx["manager_email"]],
            slot
        )
        memory.log(cid, {"event": "calendar_hold", "event": evt})
        memory.set_artifact(cid, "calendar_invite", evt)
        return evt

    if act == "slack_update":
        summary = f"Planned intro for {ctx['candidate_email']} ({ctx['role']})."
        res = Slack.post_update(ctx.get("slack_channel", "hiring"), summary)
        memory.log(cid, {"event": "slack_update", "res": res})
        return res

    if act == "ats_stage":
        res = ATS.update_stage(ctx["candidate_email"], "Contacted")
        memory.log(cid, {"event": "ats_stage", "res": res})
        return res

    raise ValueError(f"Unknown action {act}")
