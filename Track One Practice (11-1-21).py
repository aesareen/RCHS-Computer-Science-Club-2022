members = ["Arnav", "Fillip", "Sohini", "Luke", "Tushar", "Gabe", "Aryan", "Aaditya", "Kevin", "Avery"]

name = input("What is your name? ")

if name in members:
    print(f"Welcome {name}! Enjoy homecoming!")
else:
    age = int(input("How old are you? "))
    if 15 <= age <= 18:
        school = input("What High School do you attend? ")
        if school == "Raleigh Charter":
            print(f"Alright, welcome {name}, but make sure you buy a ticket!")
        else:
            print(f"I am sorry! You don't go to this school. Leave now!")
    else:
        print("What are you doing here? You are aren't even supposed to be at a High School homecoming!")

candy = input("What candy do you have? ")

if candy == "Airheads":
    airhead_type = input("What type of Airhead do you have? ")
    if airhead_type in ["Blue", "Mystery", "Green"]:
        print("Great! I will take them, and I offer 4 Snickers")
    elif airhead_type == "Red":
        print("Ew! I hate red Airheads! Get them away from me!")
    else:
        print("I don't know that Airhead flavor, seems kind of sketchy")
elif candy == "Reeses":
    reeses_type = input("What type of Reeses do you have? ")
    if reeses_type == "Cups":
        print("Those are so small! I will offer a Hershey Kiss")
    elif reeses_type == "Pieces":
        print("For a bag of Reeses Pieces, I will offer 4 Hersheys!")
    else:
        print("Reeses sure releases some weird types of candy!")

