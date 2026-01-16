def ask(prompt, options):
    print("\n" + prompt)
    for i, (text, _) in enumerate(options, 1):
        print(f"  {i}. {text}")
    while True:
        try:
            choice = int(input("Choose: ").strip())
            if 1 <= choice <= len(options):
                return options[choice - 1][1]
        except ValueError:
            pass
        print("Invalid choice. Try again.")


def resolve_mood(valence, arousal, romantic_flag):
    # Romantic override (only if not strongly negative)
    if romantic_flag and valence >= 0:
        return "romantic"

    # Quadrant-style mapping
    if valence >= 0 and arousal <= -1:
        return "calm"
    if valence >= 0 and arousal >= 1:
        return "energetic"
    if valence < 0 and arousal <= -1:
        return "serious"
    if valence < 0 and arousal >= 1:
        return "tensed"

    # Defaults
    if valence >= 0:
        return "calm"
    return "sad"


def resolve_mode(arousal, tradition):
    # Only meaningful for Hindustani (alaap vs gat)
    if tradition != "hindustani":
        return None
    return "alaap" if arousal <= 0 else "gat"


def run_quiz():
    tradition = ask(
        "Which tradition would you like today?",
        [
            ("Hindustani (North Indian)", "hindustani"),
            ("Carnatic (South Indian)", "carnatic"),
            ("Surprise me", "surprise"),
        ],
    )

    valence = 0
    arousal = 0

    # Current state (3)
    v, a = ask(
        "1/6 — How does your inner energy feel right now?",
        [("Very low / drained", (-1, -1)), ("Balanced / steady", (0, 0)), ("Restless / charged", (0, 1))],
    )
    valence += v
    arousal += a

    v, a = ask(
        "2/6 — Which best describes your emotional weight right now?",
        [("Light / content", (1, 0)), ("Neutral", (0, 0)), ("Heavy / burdened", (-1, 0))],
    )
    valence += v
    arousal += a

    v, a = ask(
        "3/6 — Where does your attention feel directed right now?",
        [("Inward / reflective", (0, -1)), ("Neutral", (0, 0)), ("Outward / expressive", (1, 1))],
    )
    valence += v
    arousal += a

    # Desired state (3)
    v, a = ask(
        "4/6 — How would you like your mind to feel after listening?",
        [("Calm and still", (1, -1)), ("Gently uplifted", (1, 0)), ("Energised and alive", (1, 1))],
    )
    valence += v
    arousal += a

    v, a = ask(
        "5/6 — What emotional colour are you seeking?",
        [("Peace and reassurance", (1, -1)), ("Joy and brightness", (1, 1)), ("Depth and seriousness", (-1, -1))],
    )
    valence += v
    arousal += a

    romantic_flag = ask(
        "6/6 — Are you feeling or seeking warmth, tenderness, or longing?",
        [("Yes", True), ("No", False)],
    )

    mood = resolve_mood(valence, arousal, romantic_flag)
    mode = resolve_mode(arousal, tradition)

    return {
        "tradition": tradition,
        "mood": mood,
        "mode": mode,
        "scores": {"valence": valence, "arousal": arousal, "romantic": romantic_flag},
    }
