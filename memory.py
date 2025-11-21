import json, uuid, time, os

class Memory:
    def __init__(self, path="data/state.json"):
        self.path = path
        os.makedirs(os.path.dirname(path), exist_ok=True)
        try:
            with open(path) as f:
                self.state = json.load(f)
        except:
            self.state = {}
            self.save()

    def save(self):
        with open(self.path, "w") as f:
            json.dump(self.state, f, indent=2)

    def new_case(self, meta):
        cid = str(uuid.uuid4())
        self.state[cid] = {"meta": meta, "timeline": [], "artifacts": {}}
        self.save()
        return cid

    def log(self, cid, entry):
        entry["ts"] = time.time()
        self.state[cid]["timeline"].append(entry)
        self.save()

    def set_artifact(self, cid, key, value):
        self.state[cid]["artifacts"][key] = value
        self.save()
