

heightft = input("Enter your height (feet first ex. 5):")
heightin = input("Enter your height (Now Inches):")
weight = input("Enter your weight in lbs:")

height = float(heightft) * 12 + float(heightin)


BMI = (float(weight) * 703) // (float(height) * float(height))

if BMI <= 16:
    print("Underweight Champ of the century")
elif BMI <= 18.4:
    print(f"Your BMI of {BMI} makes you Underweight")
elif BMI <= 24.9:
    print(f"Your BMI of {BMI} makes you Normal. Noice")
elif BMI <= 29.9:
    print(f"Your BMI of {BMI} makes you Somewhat Overweight")
elif BMI <= 34.9:
    print(f"Your BMI of {BMI} makes you Moderatly Overweight")
elif BMI <= 39.9:
    print(f"Your BMI of {BMI} makes you severly Overweight")
else:
    print(f"Your BMI of {BMI} makes you Morbidly Overweight")
