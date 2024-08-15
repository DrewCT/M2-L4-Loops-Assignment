import random

moods = ["Happy", "Tired", "Sad", "Mad", "Excited", "Calm"]
times_of_day = ["Morning", "Afternoon", "Evening"]
day_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

for day in day_of_week:
    for time in times_of_day:

        mood = random.choice(moods)

        print(f"On {day} {time}, I felt {mood}")