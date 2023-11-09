import time
import secrets

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
# Pick a random number from 1 to 3
num = secrets.SystemRandom().randint(1,3)

# Turn that random number into the computer's RPS move
if num == 1:
    comanswer = rock
elif num == 2:
    comanswer = paper
else:
    comanswer = scissors


# Ask a user to enter their move
player = input("What move do you choose? Rock, Paper or Scissors:")

# Print the rock, paper, or scissors ASCII art that corresponds to the player's move
if player == "Rock":
    output = 1
    print("You Chose Rock" """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)""")
elif player == "Paper":
    output = 2
    print( "You chose Paper" """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
""")
else:
    output = 3
    print("You chose Scissors" """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

if output == 1:
    playanswer = rock
elif output == 2:
    playanswer = paper
else:
    playanswer = scissors

# Print the rock, paper, or scissors ASCII art that corresponds to the computer's move
print("And the Computer chose...")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
print(comanswer)

time.sleep(1)


# Figure out who wins and print the result!
if num == 1 and output == 1:
    print("You BOTH Chose Rock! TIE")
elif num == 2 and output == 1:
    print("Paper BEATS rock! YOU LOSE")
elif num == 3 and output == 1:
    print("Rock SMASHES scissors! YOU WIN")
elif num == 1 and output == 2:
    print("Paper BEATS rock! YOU WIN")
elif num == 1 and output == 3:
    print("Rock SMASHES scissors! YOU LOSE")
elif num == 2 and output == 2:
    print("You BOTH Chose Paper! TIE")
elif num == 2 and output == 3:
    print("Scissors SLICES Paper YOU WIN")
elif num == 3 and output == 2:
    print("Scissors SLICES Paper YOU LOSE")
elif num == 3 and output == 3:
    print("You BOTH Chose Scissors! TIE")



