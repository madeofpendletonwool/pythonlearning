import secrets

dice_count = int(input("How many Dice would you like to roll?:"))
dice_sides = int(input("How many sides?: "))

while True:
    randres = "|"
    for num in range(dice_count):
            rand = secrets.SystemRandom().randint(1,dice_sides)
            randres += f"{rand}|"
            
    print(randres)
    answer = input("Roll again? q to quit: ")
    if answer == "q":
        break



