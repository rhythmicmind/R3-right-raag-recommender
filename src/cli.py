import argparse
from recommender import recommend_raaga
from quiz import run_quiz

def main():
    p = argparse.ArgumentParser(prog="R3-right-raag-recommender")
    p.add_argument("--mood", type=str, default=None, help="Skip quiz and set mood directly")
    p.add_argument("--tradition", type=str, default="surprise", help="hindustani | carnatic | surprise")
    p.add_argument("--mode", type=str, default=None, help="hindustani only: alaap | gat")
    p.add_argument("--quiz", action="store_true", help="Run the guided quiz (recommended)")
    p.add_argument("--seed", type=int, default=None, help="Random seed for repeatable picks")
    args = p.parse_args()

    if args.quiz or args.mood is None:
        q = run_quiz()
        mood = q["mood"]
        tradition = q["tradition"]
        mode = q["mode"]
        print("\n— Your result —")
        print(f"Tradition: {tradition}")
        print(f"Mood: {mood}")
        if mode:
            print(f"Mode: {mode}")
    else:
        mood = args.mood
        tradition = args.tradition
        mode = args.mode

    rec = recommend_raaga(mood=mood, tradition=tradition, mode=mode, seed=args.seed)

    if rec.get("raaga") is None:
        print("\n❌ No match found.")
        print(rec.get("error", ""))
        return

    print("\n🎶 Recommendation")
    if rec.get("mode"):
        print(f"Try listening to **Raaga {rec['raaga']}** ({rec['tradition']}, {rec['mode']}).")
    else:
        print(f"Try listening to **Raaga {rec['raaga']}** ({rec['tradition']}).")

    if rec.get("evidence"):
        print(f"Evidence tag(s): {', '.join(rec['evidence'])}")

if __name__ == "__main__":
    main()
