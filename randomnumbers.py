import secrets

coin = secrets.SystemRandom().randint(1, 2)

if coin == 1:
    print("Ya landed on heads!")
else:
    print("Tails LOL")


