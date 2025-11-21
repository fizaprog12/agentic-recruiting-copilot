def upsert_candidate(profile: dict):
    cid = profile.get("email", "unknown")
    print(f"[ATS] upsert {cid} role={profile.get('role')}")
    return {"candidate_id": cid}

def update_stage(candidate_id: str, stage: str):
    print(f"[ATS] {candidate_id} → {stage}")
    return {"status": "ok", "candidate_id": candidate_id, "stage": stage}
