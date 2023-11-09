import secrets

roll1 = secrets.SystemRandom().randint(1, 6)
roll2 = secrets.SystemRandom().randint(1, 3)

while roll1 != 1 or roll2 != 1:
    print(f"Your first roll was {roll1} and your second roll was {roll2}. Not Snake eyes johnson yet!")
    roll1 = secrets.SystemRandom().randint(1, 6)
    roll2 = secrets.SystemRandom().randint(1, 3)

print(f"Your first roll was {roll1} and your second roll was {roll2}. SNAKE EYES JOHNSON")
