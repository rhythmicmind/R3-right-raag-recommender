# R3-right-raag-recommender
🎶 Welcome, traveller! 
Discover the right raaga for you in this instant ---> inspired by Indian classical music theory and emotion-perception research.

## Quickstart!
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt

python src/cli.py --mood calm
python src/cli.py --mood happy --mode gat
python src/cli.py --list
```

## Overview

**R3 (Right Raag Recommender)** is a lightweight, research-inspired recommendation system that suggests an Indian classical raaga based on:

1. **How you feel right now**, and  
2. **How you would like to feel after listening**.

Unlike generic mood playlists, this project treats music as a **regulative and transformative experience**, reflecting how Indian classical music is traditionally performed and experienced.

The recommender currently supports both:
- **Hindustani (North Indian) classical music**
- **Carnatic (South Indian) classical music**

---

## 🎯 Design Philosophy

Indian classical music is not only expressive — it is **intentional**.

Listeners often engage with a raaga to:
- calm the mind,
- gently uplift emotion,
- process heaviness,
- or gradually transform their internal state.

This project mirrors that idea by distinguishing between:
- **current emotional state** (reflection), and
- **desired emotional state** (transition).

Rather than enforcing abrupt mood changes, the system recommends ragas that **respect emotional continuity**, much like a real concert or mehfil.

---

## 🧠 Research Inspiration

This project is inspired by empirical research on music and emotion, particularly:

- Listener studies showing that **Hindustani ragas evoke distinct emotional responses**.
- Findings that **tempo and rhythmic structure (e.g., alaap vs gat)** modulate emotional arousal, while tonal structure influences emotional valence.
- Research indicating that **the same raaga can shift emotional character depending on performance mode**.
- Studies on **Carnatic music** showing consistent emotion and rasa clustering across listeners.

These ideas inform:
- the quiz questions,
- the mood model (valence × arousal),
- and the raaga mappings stored in the dataset.

> ⚠️ Note:  
> This is an educational, research-inspired project — **not** a medical, therapeutic, or psychological diagnostic tool.

---

## 🧩 How It Works

### 1️⃣ Tradition Selection
The user first chooses:
- Hindustani
- Carnatic
- or *Surprise me*

This ensures recommendations respect stylistic and cultural context.

---

### 2️⃣ Emotion-Aware Quiz

The system asks:
- **3 questions about how you feel right now**
- **3–4 questions about how you would like to feel**

The questions are grounded in concepts such as:
- arousal (energy level),
- emotional valence (light ↔ heavy),
- introspection vs expression,
- desired emotional transformation.

---

### 3️⃣ Mood Resolution

Responses are mapped onto a simple emotional space:

| Valence | Arousal | Resulting Mood |
|------|------|------|
| Positive | Low | Calm |
| Positive | High | Happy / Energetic |
| Negative | Low | Serious / Sad |
| Negative | High | Tensed |
| Romantic flag | — | Romantic |

The **desired state gently nudges** the final outcome rather than overriding it.

---

### 4️⃣ Raaga Recommendation

Using the resolved mood:
- A raaga is selected from a **curated, research-inspired dataset**.
- For Hindustani music, the system may also consider **performance mode**:
  - **Alaap** → calmer, introspective listening
  - **Gat** → more rhythmic, energetic expression

---

## 📁 Dataset Structure

All mappings live in: data/ragas.json


Each raaga entry includes:
- tradition (`hindustani` / `carnatic`)
- emotion tags
- supporting research source(s)
- (for Hindustani) emotion differences between **alaap** and **gat**

The dataset is designed to be:
- transparent,
- extendable,
- and easy to audit.

---

## 🚀 How to Run (CLI)

```bash
python src/cli.py
```

### Example:

🎶 Welcome, traveller.
You feel: heavy and restless
You wish to feel: calmer and reassured

Recommended:
Raaga Yaman (Hindustani, alaap)
