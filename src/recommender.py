import csv

from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

DEFAULT_WEIGHTS = {
    "genre": 2.0,
    "mood": 1.5,
    "energy": 1.0,
    "valence": 0.75,
    "danceability": 0.50,
    "acousticness": 0.25,
}

BALANCED_WEIGHTS = {
    "genre": 1.0,
    "mood": 1.5,
    "energy": 1.25,
    "valence": 1.0,
    "danceability": 0.75,
    "acousticness": 0.50,
}

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
    target_valence: Optional[float] = None
    target_danceability: Optional[float] = None
    target_acousticness: Optional[float] = None

class Recommender:
    """Score, explain, and rank songs using content features."""

    def __init__(self, songs, weights: Optional[Dict[str, float]] = None):
        self.songs = songs
        self.weights = weights or DEFAULT_WEIGHTS

    @staticmethod
    def _value(item, key: str, fallback: Optional[str] = None):
        """Read a field from a dictionary or dataclass-like object."""
        if isinstance(item, dict):
            value = item.get(key)
            return value if value is not None or fallback is None else item.get(fallback)

        value = getattr(item, key, None)
        return value if value is not None or fallback is None else getattr(item, fallback, None)

    def score_song(self, user, song) -> Tuple[float, List[str]]:
        """Score one song and return the reasons that earned points."""
        score = 0.0
        reasons = []
        favorite_genre = self._value(user, "favorite_genre", "genre")
        favorite_mood = self._value(user, "favorite_mood", "mood")

        if favorite_genre and self._value(song, "genre").lower() == favorite_genre.lower():
            score += self.weights["genre"]
            reasons.append(f"genre match (+{self.weights['genre']})")

        if favorite_mood and self._value(song, "mood").lower() == favorite_mood.lower():
            score += self.weights["mood"]
            reasons.append(f"mood match (+{self.weights['mood']})")

        for song_key, target_key in (
            ("energy", "target_energy"),
            ("valence", "target_valence"),
            ("danceability", "target_danceability"),
            ("acousticness", "target_acousticness"),
        ):
            target = self._value(user, target_key, song_key)
            if target is None and song_key == "acousticness":
                likes_acoustic = self._value(user, "likes_acoustic")
                if likes_acoustic is not None:
                    target = 0.8 if likes_acoustic else 0.2
            if target is None:
                continue

            song_value = self._value(song, song_key)
            similarity = max(0.0, 1.0 - abs(float(target) - float(song_value)))
            points = self.weights[song_key] * similarity
            score += points
            reasons.append(
                f"{song_key} similarity {similarity:.0%} (+{points:.2f})"
            )

        return score, reasons

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Return songs ranked from highest to lowest score."""
        ranked = sorted(
            self.songs,
            key=lambda song: self.score_song(user, song)[0],
            reverse=True,
        )
        return ranked[:max(0, k)]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Explain the points earned by a recommended song."""
        _, reasons = self.score_song(user, song)
        return "; ".join(reasons) if reasons else "No strong preference matches"

    def recommend_with_scores(self, user, k: int = 5) -> List[Tuple]:
        """Return ranked songs with their scores and explanations."""
        results = []
        for song in self.songs:
            score, reasons = self.score_song(user, song)
            explanation = "; ".join(reasons) if reasons else "No strong preference matches"
            results.append((song, score, explanation))

        results.sort(key=lambda result: result[1], reverse=True)
        return results[:max(0, k)]

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

def score_song(
    user_prefs: Dict,
    song: Dict,
    weights: Optional[Dict[str, float]] = None,
) -> Tuple[float, List[str]]:
    """Score one song through the Recommender class."""
    return Recommender([], weights).score_song(user_prefs, song)

def recommend_songs(
    user_prefs: Dict,
    songs: List[Dict],
    k: int = 5,
    weights: Optional[Dict[str, float]] = None,
) -> List[Tuple[Dict, float, str]]:
    """Rank songs through the Recommender class."""
    return Recommender(songs, weights).recommend_with_scores(user_prefs, k)
