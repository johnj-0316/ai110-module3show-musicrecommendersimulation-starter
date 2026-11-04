# Model Card: VibeFinder 1.0

## 1. Model Name

The model is called **VibeFinder 1.0**. The name reflects its focus on a song's
sound and mood.

## 2. Goal / Task

VibeFinder suggests songs for one user profile. It compares each song with the
user's favorite genre, mood, and audio targets. It returns the five songs with
the highest scores.

## 3. Data Used

The catalog has 18 fictional songs. Each song has a genre, mood, energy, tempo,
valence, danceability, and acousticness value. The catalog includes pop, lofi,
rock, jazz, metal, folk, classical, and other genres. It is too small to show
the full range of real music. It also has no lyrics, language, or listening
history.

## 4. Algorithm Summary

The recommender compares every song with one listener profile. The original
recipe gives two points for a genre match and 1.5 points for a mood match.
Energy, valence, danceability, and acousticness earn points based on how close
they are to the user's targets. A closer value earns more points. These parts
add up to a maximum score of six points.

After every song has a score, the system sorts the catalog from highest to
lowest. It returns the top five songs. Each result lists the reasons that added
points. Tempo is not scored because it closely overlaps with energy in this
small dataset.

I also tested a balanced recipe. It lowers the genre weight from 2.0 to 1.0. It
gives more weight to the four audio features. Both recipes have a maximum score
of six points.

## 5. Observed Behavior / Biases

The model works well when genre, mood, and audio targets agree. The first song
matched the intended style for all three normal profiles. The numeric features
also helped related songs from other genres enter the top five.

The original recipe puts too much weight on genre. In the conflicting profile,
a metal song ranked first even though its valence and acousticness were poor
matches. This can hide good songs from other genres. The balanced recipe fixes
some of this problem, but it may ignore a user's clear genre preference.

## 6. Evaluation Process

I tested High-Energy Pop, Chill Lofi, and Deep Intense Rock profiles. I also
tested a Conflicted Melancholic Metal profile. The last profile mixes high
energy with low valence and high acousticness. This checks how the system
handles preferences that pull in different directions.

The first three profiles produced sensible top songs. Sunrise City won for
pop, Library Rain won for lofi, and Storm Runner won for rock. The surprising
result came from the conflicting profile. The original recipe chose Crown of
Thunder, but the balanced recipe chose Blue County Line.

The profile comparisons also showed clear patterns:

- Pop vs. lofi: Pop favored bright songs. Lofi favored calm acoustic songs.
- Pop vs. rock: Both favored high energy. Rock favored lower valence.
- Pop vs. conflicted metal: Both wanted high energy. Low valence pushed pop
  songs down for the metal profile.
- Lofi vs. rock: Their energy targets were almost opposite. Their rankings were
  also very different.
- Lofi vs. conflicted metal: Both valued acousticness. Their energy and mood
  targets led to different winners.
- Rock vs. conflicted metal: Both liked heavy music. The conflicted profile also
  made a melancholic country song competitive.

The original and balanced recipes changed three of the four rankings. Rooftop
Lights passed Gym Hero for the pop profile. Spacewalk Thoughts passed Focus
Flow for the lofi profile. Blue County Line passed Crown of Thunder for the
conflicting profile. The rock ranking did not change.

### Weight Comparison Experiment

I compared the original recipe with a balanced recipe. Both have a maximum of
six points.

| Feature | Original | Balanced |
|---|---:|---:|
| Genre | 2.00 | 1.00 |
| Mood | 1.50 | 1.50 |
| Energy | 1.00 | 1.25 |
| Valence | 0.75 | 1.00 |
| Danceability | 0.50 | 0.75 |
| Acousticness | 0.25 | 0.50 |

The balanced recipe gave less power to genre. It gave more power to the audio
features. This caused Blue County Line to replace Crown of Thunder for the
conflicting profile. It may find better cross-genre matches, but it may also
ignore a user's clear genre preference.

### Evaluation Output

### High-Energy Pop

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

### Chill Lofi

```text
1. Library Rain - 5.98
   Reasons: genre match (+2.0); mood match (+1.5); energy similarity 100% (+1.00); valence similarity 100% (+0.75); danceability similarity 97% (+0.49); acousticness similarity 99% (+0.25)
2. Midnight Coding - 5.83
   Reasons: genre match (+2.0); mood match (+1.5); energy similarity 93% (+0.93); valence similarity 96% (+0.72); danceability similarity 93% (+0.47); acousticness similarity 86% (+0.21)
3. Focus Flow - 4.40
   Reasons: genre match (+2.0); energy similarity 95% (+0.95); valence similarity 99% (+0.74); danceability similarity 95% (+0.48); acousticness similarity 93% (+0.23)
4. Spacewalk Thoughts - 3.80
   Reasons: mood match (+1.5); energy similarity 93% (+0.93); valence similarity 95% (+0.71); danceability similarity 86% (+0.43); acousticness similarity 93% (+0.23)
5. Golden Polaroid - 2.41
   Reasons: energy similarity 97% (+0.97); valence similarity 99% (+0.74); danceability similarity 91% (+0.45); acousticness similarity 97% (+0.24)
```

### Deep Intense Rock

```text
1. Storm Runner - 5.83
   Reasons: genre match (+2.0); mood match (+1.5); energy similarity 96% (+0.96); valence similarity 92% (+0.69); danceability similarity 89% (+0.45); acousticness similarity 95% (+0.24)
2. Gym Hero - 3.54
   Reasons: mood match (+1.5); energy similarity 98% (+0.98); valence similarity 63% (+0.47); danceability similarity 67% (+0.34); acousticness similarity 100% (+0.25)
3. Crown of Thunder - 2.23
   Reasons: energy similarity 98% (+0.98); valence similarity 76% (+0.57); danceability similarity 88% (+0.44); acousticness similarity 98% (+0.24)
4. Night Drive Loop - 2.10
   Reasons: energy similarity 80% (+0.80); valence similarity 91% (+0.68); danceability similarity 82% (+0.41); acousticness similarity 83% (+0.21)
5. Sunrise City - 1.89
   Reasons: energy similarity 87% (+0.87); valence similarity 56% (+0.42); danceability similarity 76% (+0.38); acousticness similarity 87% (+0.22)
```

### Conflicted Melancholic Metal

```text
1. Crown of Thunder - 3.77
   Reasons: genre match (+2.0); energy similarity 93% (+0.93); valence similarity 51% (+0.38); danceability similarity 82% (+0.41); acousticness similarity 18% (+0.05)
2. Blue County Line - 3.26
   Reasons: mood match (+1.5); energy similarity 54% (+0.54); valence similarity 81% (+0.61); danceability similarity 74% (+0.37); acousticness similarity 96% (+0.24)
3. Storm Runner - 1.85
   Reasons: energy similarity 99% (+0.99); valence similarity 67% (+0.50); danceability similarity 59% (+0.29); acousticness similarity 25% (+0.06)
4. Night Drive Loop - 1.70
   Reasons: energy similarity 85% (+0.85); valence similarity 66% (+0.49); danceability similarity 52% (+0.26); acousticness similarity 37% (+0.09)
5. Shadow Waltz - 1.70
   Reasons: energy similarity 42% (+0.42); valence similarity 78% (+0.58); danceability similarity 94% (+0.47); acousticness similarity 89% (+0.22)
```

## 7. Intended Use and Non-Intended Use

This project is designed for classroom learning. It shows how features and
weights affect recommendations. It can also be used for small scoring
experiments. It should not be used as a real streaming service. It should not
be used to judge artists, predict popularity, or make decisions about people.

## 8. Ideas for Improvement

- Use a larger catalog with real and balanced genre coverage.
- Learn feature weights from user likes and skips.
- Add lyrics, language, release year, and listening context.
