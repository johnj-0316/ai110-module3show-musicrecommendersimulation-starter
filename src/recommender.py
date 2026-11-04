import csv

from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from a CSV file and convert numeric fields."""
    songs = []

    with open(csv_path, mode="r", newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            row["id"] = int(row["id"])
            row["energy"] = float(row["energy"])
            row["tempo_bpm"] = float(row["tempo_bpm"])
            row["valence"] = float(row["valence"])
            row["danceability"] = float(row["danceability"])
            row["acousticness"] = float(row["acousticness"])
            songs.append(row)

    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Score one song against a user's preferences and explain the points."""
    score = 0.0
    reasons = []

    favorite_genre = user_prefs.get("favorite_genre", user_prefs.get("genre"))
    favorite_mood = user_prefs.get("favorite_mood", user_prefs.get("mood"))

    if favorite_genre and song["genre"].lower() == favorite_genre.lower():
        score += 2.0
        reasons.append("genre match (+2.0)")

    if favorite_mood and song["mood"].lower() == favorite_mood.lower():
        score += 1.5
        reasons.append("mood match (+1.5)")

    numerical_features = (
        ("energy", "target_energy", 1.0),
        ("valence", "target_valence", 0.75),
        ("danceability", "target_danceability", 0.50),
        ("acousticness", "target_acousticness", 0.25),
    )

    for song_key, target_key, weight in numerical_features:
        target = user_prefs.get(target_key, user_prefs.get(song_key))
        if target is None:
            continue

        similarity = max(0.0, 1.0 - abs(float(target) - float(song[song_key])))
        points = weight * similarity
        score += points
        reasons.append(
            f"{song_key} similarity {similarity:.0%} (+{points:.2f})"
        )

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Rank all songs by preference score and return the top results."""
    scored_songs = []

    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = "; ".join(reasons) if reasons else "No strong preference matches"
        scored_songs.append((song, score, explanation))

    scored_songs.sort(key=lambda recommendation: recommendation[1], reverse=True)
    return scored_songs[:max(0, k)]
