name1 = input("Enter Player 1 name: ")
name2 = input("Enter Player 2 name: ")

toothpicks = 13
toothpicks = int(toothpicks)
while True:
    print("|" * toothpicks)
    print(f"There are {toothpicks} left.")
    pull_picks = int(input(f"How many do you take {name1}?: "))
    while pull_picks != 1 and pull_picks != 2 and pull_picks != 3:
        pull_picks = int(input("You must choose a 1, 2, or 3!: "))
    toothpicks -= pull_picks
    if toothpicks <= 0:
        print(f"{name1} Wins!")
        break

    print("|" * toothpicks)
    print(f"There are {toothpicks} left.")
    pull_picks = int(input(f"How many do you take {name2}?: "))
    while pull_picks != 1 and pull_picks != 2 and pull_picks != 3:
        pull_picks = int(input("You must choose a 1, 2, or 3!: "))
    toothpicks -= pull_picks
    if toothpicks <= 0:
        print(f"{name2} Wins!")
        break