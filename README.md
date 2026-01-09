# R3-right-raag-recommender
🎶 Welcome, traveller! Discover the right raaga for you in this instant ---> inspired by Indian classical music theory and emotion-perception research.

## 🚀 Quickstart
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt

python src/cli.py --mood calm
python src/cli.py --mood happy --mode gat
python src/cli.py --list


---

## 2) Make the project data-driven (create `data/ragas.json`)

Create a small curated dataset (you can expand later). Example:

```json
{
  "ragas": [
    {"name": "Yaman", "tags": ["calm", "peaceful"]},
    {"name": "Desh", "tags": ["happy", "uplifting"]},
    {"name": "Tilak Kamod", "tags": ["romantic", "warm"]},
    {"name": "Darbari Kanada", "tags": ["serious", "deep"]},
    {"name": "Hamsadhwani", "tags": ["energetic", "bright"]}
  ],
  "aliases": {
    "peaceful": "calm",
    "relaxed": "calm",
    "love": "romantic",
    "focused": "serious",
    "excited": "energetic"
  }
}
