# Republic Day Python

### Republic Day Flag Hoisting – Smart Analytics & Alert System

## Question

On Republic Day, flag hoisting is conducted at multiple locations.

Write a Python program that:

1. Asks for the **number of locations**.
    - If the number is `0` or less, show an error message and stop.
2. For each location, take:
    - Location name
    - Number of participants
    - Flag hoisting time (`HH:MM`)
3. Store all details and generate a report that shows:
    - Total participants and average per location
    - Location with **highest** and **lowest** participation
    - Event counts:
        - Mega (≥300), Large (150–299), Medium (75–149), Small (<75)
    - Time insights:
        - Events before 08:00 (Early)
        - Events after 10:30 (Late)
    - Alerts:
        - Participants < 30 → *Low Engagement*
        - Time after 10:30 → *Late Ceremony*
4. Decide overall celebration status:
    - ≥1500 → *National Pride Celebration*
    - 800–1499 → *Grand Celebration*
    - <800 → *Local Celebration*
5. Print a clean report with a patriotic message.
