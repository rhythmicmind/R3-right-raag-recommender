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
    if romantic_flag and valence >= 0:
        return "romantic"
    if arousal <= -1 and valence >= 0:
        return "calm"
    if arousal >= 1 and valence >= 0:
        return "energetic"
    if arousal <= -1 and valence < 0:
        return "serious"
    if arousal >= 1 and valence < 0:
        return "tensed"
    return "calm"

def resolve_mode(arousal, tradition):
    # Only used for Hindustani
    if tradition != "hindustani":
        return None
    return "alaap" if arousal <= 0 else "gat"

def run_quiz():
    tradition = ask(
        "Which tradition would you like today?",
        [("Hindustani (North Indian)", "hindustani"),
         ("Carnatic (South Indian)", "carnatic"),
         ("Surprise me", "surprise")]
    )

    # Part A: current state
    valence = 0
    arousal = 0

    v, a = ask(
        "How does your inner energy feel right now?",
        [("Very low / drained", (-1, -1)),
         ("Balanced / steady", (0, 0)),
         ("Restless / charged", (0, 1))]
    )
    valence += v; arousal += a

    v, a = ask(
        "Which best describes your emotional weight right now?",
        [("Light / content", (1, 0)),
         ("Neutral", (0, 0)),
         ("Heavy / burdened", (-1, 0))]
    )
    valence += v; arousal += a

    v, a = ask(
        "Where does your attention feel directed right now?",
        [("Inward / reflective", (0, -1)),
         ("Neutral", (0, 0)),
         ("Outward / expressive", (1, 1))]
    )
    valence += v; arousal += a

    # Part B: desired state
    v, a = ask(
        "How would you like your mind to feel after listening?",
        [("Calm and still", (1, -1)),
         ("Gently uplifted", (1, 0)),
         ("Energised and alive", (1, 1))]
    )
    valence += v; arousal += a

    v, a = ask(
        "What emotional colour are you seeking?",
        [("Peace and reassurance", (1, -1)),
         ("Joy and brightness", (1, 1)),
         ("Depth and seriousness", (-1, -1))]
    )
    valence += v; arousal += a

    romantic_flag = ask(
        "Are you feeling or seeking warmth, tenderness, or longing?",
        [("Yes", True), ("No", False)]
    )

    mood = resolve_mood(valence, arousal, romantic_flag)
    mode = resolve_mode(arousal, tradition)

    return {
        "tradition": tradition,
        "mood": mood,
        "mode": mode,
        "scores": {"valence": valence, "arousal": arousal, "romantic": romantic_flag}
    }
