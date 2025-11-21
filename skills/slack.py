def post_update(channel: str, summary: str):
    msg = f"[SLACK] #{channel}: {summary}"
    print(msg)
    return {"status": "posted", "message": msg}
