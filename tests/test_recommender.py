from pathlib import Path
from src.recommender import recommend_raaga

DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "ragas.json"

def test_hindustani_calm_alaap_returns_raaga():
    rec = recommend_raaga("calm", tradition="hindustani", mode="alaap", seed=0, data_path=DATA_PATH)
    assert rec["raaga"] is not None

def test_carnatic_happy_returns_raaga():
    rec = recommend_raaga("happy", tradition="carnatic", seed=0, data_path=DATA_PATH)
    assert rec["raaga"] is not None

def test_unknown_mood_fails_cleanly():
    rec = recommend_raaga("not_a_mood", tradition="hindustani", seed=0, data_path=DATA_PATH)
    assert rec["raaga"] is None
    assert "error" in rec
