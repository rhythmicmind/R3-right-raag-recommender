import json
import random
from pathlib import Path
from typing import Optional, Dict, Any, List

DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "ragas.json"


def _norm(s: str) -> str:
    return " ".join(s.strip().lower().split())


def load_data(path: Path = DATA_PATH) -> Dict[str, Any]:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def resolve_alias(mood: str, aliases: Dict[str, str]) -> str:
    m = _norm(mood)
    return _norm(aliases.get(m, m))


def filter_by_tradition(ragas: List[Dict[str, Any]], tradition: str) -> List[Dict[str, Any]]:
    t = _norm(tradition)
    if t in ("", "surprise", "either", "any"):
        return ragas
    return [r for r in ragas if _norm(r.get("tradition", "")) == t]


def recommend_raaga(
    mood: str,
    tradition: str = "surprise",
    mode: Optional[str] = None,          # alaap/gat for Hindustani
    seed: Optional[int] = None,
    data_path: Path = DATA_PATH
) -> Dict[str, Any]:
    """
    Returns:
      {
        raaga: str|None,
        tradition: str,
        mood: str,
        mode: str|None,
        evidence: list[str],
        error?: str
      }
    """
    data = load_data(data_path)
    aliases = data.get("aliases", {})
    mood_resolved = resolve_alias(mood, aliases)

    ragas = data.get("ragas", [])
    pool = filter_by_tradition(ragas, tradition)

    candidates = []
    requested_mode = _norm(mode) if mode else None

    for r in pool:
        name = r.get("name")
        tr = _norm(r.get("tradition", ""))
        evidence = r.get("evidence", [])

        # Hindustani: mode-aware tags
        if "mode_emotion_tags" in r:
            if requested_mode:
                tags = r["mode_emotion_tags"].get(requested_mode, [])
                tags = [_norm(x) for x in tags]
                if mood_resolved in tags:
                    candidates.append(
                        {"raaga": name, "tradition": tr, "mode": requested_mode, "evidence": evidence}
                    )
            else:
                # If mode not specified, allow match in either mode
                for m, tags in r["mode_emotion_tags"].items():
                    tags = [_norm(x) for x in tags]
                    if mood_resolved in tags:
                        candidates.append(
                            {"raaga": name, "tradition": tr, "mode": _norm(m), "evidence": evidence}
                        )
                        break

        # Carnatic (or others): emotion_tags
        elif "emotion_tags" in r:
            tags = [_norm(x) for x in r.get("emotion_tags", [])]
            if mood_resolved in tags:
                candidates.append(
                    {"raaga": name, "tradition": tr, "mode": None, "evidence": evidence}
                )

    if seed is not None:
        random.seed(seed)

    if not candidates:
        return {
            "raaga": None,
            "tradition": _norm(tradition),
            "mood": mood_resolved,
            "mode": requested_mode,
            "evidence": [],
            "error": "No matching raaga found for the selected mood/tradition/mode."
        }

    choice = random.choice(candidates)
    choice["mood"] = mood_resolved
    return choice
