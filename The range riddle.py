import random

moods = ["Happy", "Tired", "Sad", "Mad", "Excited", "Calm"]
day_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

for day in day_of_week:
    mood = random.choice(moods)

    print(f"On {day}, I felt {mood}")