def draft_email(context: dict, tone="professional"):
    role = context.get("role", "")
    name = context.get("name", "there")
    body = (
        f"Hi {name},\n\n"
        f"I’m impressed by your background for our {role}. "
        "Are you open to a quick 20–30 min intro?\n"
        "Here are a few slots: Tue 10am, Wed 2pm, Thu 11am.\n\n"
        "Best,\nRecruiting"
    )
    subject = f"Intro chat about {role}"
    return {"subject": subject, "body": body}

def send_email(to: str, subject: str, body: str):
    # Replace with SMTP or provider SDK for real sends
    print(f"[EMAIL] to={to} subj={subject}\n{body}")
    return {"status": "sent", "id": "mock-email-123"}
