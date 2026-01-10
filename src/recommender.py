import json
import random
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "ragas.json"

def load_data(path: Path = DATA_PATH) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def normalize(s: str) -> str:
    return " ".join(s.strip().lower().split())

def resolve_alias(mood: str, aliases: dict) -> str:
    mood_n = normalize(mood)
    return normalize(aliases.get(mood_n, mood_n))

def filter_ragas(data: dict, tradition: str | None) -> list[dict]:
    ragas = data.get("ragas", [])
    if not tradition or tradition == "surprise":
        return ragas
    t = normalize(tradition)
    return [r for r in ragas if normalize(r.get("tradition", "")) == t]

def recommend_raaga(
    mood: str,
    tradition: str = "surprise",
    mode: str | None = None,
    seed: int | None = None,
    data_path: Path = DATA_PATH
) -> dict:
    """
    Returns a dict with keys:
      - raaga, tradition, mood, mode, evidence
    """
    data = load_data(data_path)
    aliases = data.get("aliases", {})
    mood_resolved = resolve_alias(mood, aliases)

    pool = filter_ragas(data, tradition)

    candidates = []
    for r in pool:
        t = normalize(r.get("tradition", ""))
        name = r.get("name")
        evidence = r.get("evidence", [])

        # Hindustani can be mode-aware if mode_emotion_tags exists
        if "mode_emotion_tags" in r and mode:
            m = normalize(mode)
            tags = r["mode_emotion_tags"].get(m, [])
            tags = [normalize(x) for x in tags]
            if mood_resolved in tags:
                candidates.append({"raaga": name, "tradition": t, "mode": m, "evidence": evidence})
        else:
            tags = r.get("emotion_tags", [])
            tags = [normalize(x) for x in tags]
            if mood_resolved in tags:
                candidates.append({"raaga": name, "tradition": t, "mode": None, "evidence": evidence})

    if seed is not None:
        random.seed(seed)

    if not candidates:
        return {
            "raaga": None,
            "tradition": tradition,
            "mood": mood_resolved,
            "mode": mode,
            "evidence": [],
            "error": "No matching raaga found for the selected mood/tradition/mode."
        }

    choice = random.choice(candidates)
    choice["mood"] = mood_resolved
    return choice
