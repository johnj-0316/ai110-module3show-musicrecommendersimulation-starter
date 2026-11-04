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

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
# e.g.:
# User profile: genre=indie, mood=chill, energy=low
# Recommendations:
#   1. ...
#   2. ...
#   3. ...
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



