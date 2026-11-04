# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Each song is represented by its genre, mood, energy, tempo, valence,
danceability, and acousticness. The recommender compares those attributes with a
specific user taste profile. The initial profile favors happy pop music with
high energy (0.80), valence (0.85), and danceability (0.80), plus low
acousticness (0.20). Tempo is stored as useful song information but is not
scored because it overlaps strongly with energy in this small dataset.

### Algorithm Recipe

The recommender calculates a score for every song using these rules:

- Add **2.0 points** for an exact genre match.
- Add **1.5 points** for an exact mood match.
- Add up to **1.0 point** for energy similarity.
- Add up to **0.75 points** for valence similarity.
- Add up to **0.50 points** for danceability similarity.
- Add up to **0.25 points** for acousticness similarity.

For every numerical feature, similarity is calculated as:

```text
similarity = 1 - abs(user target - song value)
```

All numerical values range from 0 to 1, so a perfect match receives all the
available points and a more distant value receives proportionally fewer. The
maximum possible score is 6.0. After scoring the catalog, the recommender sorts
the songs from highest to lowest score and returns the top `k` songs. An
explanation identifies the strongest matches behind each recommendation.

### Expected Biases

Genre has the largest single weight, so the system may over-prioritize familiar
genres and miss excellent cross-genre songs that match the user's mood and
audio preferences. Exact genre and mood labels also cannot represent related
categories, such as pop and indie pop. The small, synthetic catalog may make
some genres and moods appear more typical than they are, and it contains no
information about lyrics, vocals, language, cultural context, or changes within
a song. Finally, a fixed profile cannot capture how a listener's preferences
change by activity, setting, or time.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

This example uses the High-Energy Pop profile and the original weights:

```text
1. Sunrise City - 5.83
   Reasons: genre match (+2.0); mood match (+1.5); energy similarity 92% (+0.92); valence similarity 94% (+0.70); danceability similarity 94% (+0.47); acousticness similarity 92% (+0.23)
2. Gym Hero - 4.34
   Reasons: genre match (+2.0); energy similarity 97% (+0.97); valence similarity 87% (+0.65); danceability similarity 97% (+0.48); acousticness similarity 95% (+0.24)
3. Rooftop Lights - 3.71
   Reasons: mood match (+1.5); energy similarity 86% (+0.86); valence similarity 91% (+0.68); danceability similarity 97% (+0.48); acousticness similarity 75% (+0.19)
4. Sidewalk Bounce - 2.25
   Reasons: energy similarity 84% (+0.84); valence similarity 93% (+0.70); danceability similarity 94% (+0.47); acousticness similarity 98% (+0.24)
5. Tomorrow Tide - 2.12
   Reasons: energy similarity 73% (+0.73); valence similarity 96% (+0.72); danceability similarity 99% (+0.49); acousticness similarity 72% (+0.18)
```

---

## Experiments You Tried

I tested four profiles: High-Energy Pop, Chill Lofi, Deep Intense Rock, and
Conflicted Melancholic Metal. The first three profiles produced intuitive top
matches. The conflicting profile tested high energy together with low valence
and high acousticness.

I also compared two six-point weighting recipes. The original recipe gives
genre 2.0 points. The balanced recipe lowers genre to 1.0 and gives more weight
to energy, valence, danceability, and acousticness. Three rankings changed:

- Rooftop Lights moved above Gym Hero for High-Energy Pop.
- Spacewalk Thoughts moved above Focus Flow for Chill Lofi.
- Blue County Line moved above Crown of Thunder for the conflicting profile.

The Deep Intense Rock order did not change. These results show that lowering
the genre weight makes cross-genre audio matches more competitive.

---

## Limitations and Risks

The catalog contains only 18 fictional songs. It cannot represent the range of
real artists, cultures, genres, or production styles. The model does not use
lyrics, language, listening history, or the user's current activity.

Exact genre and mood labels treat related categories as different. The
original weights can over-prioritize genre and hide strong cross-genre songs.
The balanced weights reduce that bias, but they may underweight a genre choice
that the user cares about. Fixed weights also assume every listener defines a
musical vibe in the same way.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

My biggest learning moment is how recommending algorithms are not rigid, but heavily customizable based on formulas that we create. I've always believed that the algorithms behind apps like YouTube and Twitter were impossibly large, and while they may scale higher than this app, they likely still rely on the same weights and data from real users. This app is not too different in that sense.

AI tools streamline implementation, but I need to make sure I understand the logic and reasoning behind them to ensure that nothing is over-engineered or overly complicated. I also need to ensure the generated code meets my standards and requirements, despite how powerful models are today.

Bias and unfairness can still appear, as rigid algorithms and even llms can only go so far with calculations. Bias and unfairness can still show up from unclean and unfiltered data, as well as improper weights, resulting in unexpected recommendations or rankings.

If I were to continue this project, I would fine tune the formulas to fit real users, allow users to input their own preferences in a UI, and allow users to fine tune their own recommendations. Spotify does this automatically via our listens, but even Spotify can misinterpret what kind of vibe I want next without my input.



