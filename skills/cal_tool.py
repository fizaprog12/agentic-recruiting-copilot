def create_event(title, attendees: list, slot: str, location="Google Meet"):
    invite = {
        "title": title,
        "attendees": attendees,
        "slot": slot,
        "location": location,
        "link": "https://meet.mock/link/xyz"
    }
    print(f"[CAL] {invite}")
    return invite
