import random

# Track One
born = input("Were you born in the United States (y/n)? ")
if born == "y":
    time_in_US = int(input("How many years have you been a resident in the U.S. ? "))
    if time_in_US < 14:
        print("I am sorry, you have be a resident in the U.S. for at least 14 years ")
    else:
        age = int(input("How old are you? "))
        if age < 35:
            print("I am sorry, you are not old enough to be president. Maybe try again in a few years!")
        else:
            print("Yay you are eligible to be president! Now, go campaign!")
else:
    print("I am sorry, you are not eligible to be president. You have to be born in the U.S.")


# Track Two
def spending():
    choices = ["approves", "rejects"]
    agree = False
    while agree == False:
        amount = int(input("Please enter a proposed amount for the infrastructure bill: $"))
        if amount < 700000000:
            print("The Democrat will never accept this! It is way too low!")
        elif amount > 1800000000000:
            print("The Republican will never accept this! It is way too high!")
        else:
            dem_choice = random.choice(choices)
            repub_choice = random.choice(choices)
            if dem_choice != repub_choice:
                print(f"They disagree! The Democrat {dem_choice} the bill and the Republican {repub_choice} it.")
            else:
                print(f"Yay! They agree! The ${amount} bill will pass!")
                agree = True

# spending()
