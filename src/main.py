"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from .recommender import (
    BALANCED_WEIGHTS,
    DEFAULT_WEIGHTS,
    load_songs,
    recommend_songs,
)


USER_PROFILES = {
    "High-Energy Pop": {
        "favorite_genre": "pop",
        "favorite_mood": "happy",
        "target_energy": 0.90,
        "target_valence": 0.90,
        "target_danceability": 0.85,
        "target_acousticness": 0.10,
    },
    "Chill Lofi": {
        "favorite_genre": "lofi",
        "favorite_mood": "chill",
        "target_energy": 0.35,
        "target_valence": 0.60,
        "target_danceability": 0.55,
        "target_acousticness": 0.85,
    },
    "Deep Intense Rock": {
        "favorite_genre": "rock",
        "favorite_mood": "intense",
        "target_energy": 0.95,
        "target_valence": 0.40,
        "target_danceability": 0.55,
        "target_acousticness": 0.05,
    },
    "Conflicted Melancholic Metal": {
        "favorite_genre": "metal",
        "favorite_mood": "melancholic",
        "target_energy": 0.90,
        "target_valence": 0.15,
        "target_danceability": 0.25,
        "target_acousticness": 0.85,
    },
}

WEIGHT_STRATEGIES = {
    "Original genre-heavy weights": DEFAULT_WEIGHTS,
    "Balanced audio-feature weights": BALANCED_WEIGHTS,
}


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    for profile_name, user_prefs in USER_PROFILES.items():
        print(f"\nProfile: {profile_name}")
        print("=" * 48)

        for strategy_name, weights in WEIGHT_STRATEGIES.items():
            recommendations = recommend_songs(user_prefs, songs, k=5, weights=weights)
            print(f"\n{strategy_name}")

            for rank, (song, score, explanation) in enumerate(recommendations, start=1):
                print(f"{rank}. {song['title']} - {score:.2f}")
                print(f"   Reasons: {explanation}")


if __name__ == "__main__":
    main()
