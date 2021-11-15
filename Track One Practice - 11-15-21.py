# In Club

# Exercise One:
people = ["Ian", "Luke", "Tushar", "Arnav"]

person = False
while not person:
    name = input("What is your name? ")
    if name in people:
        print(f"Hi {name}!")
        break
    else:
        print("You're not allowed.")

# Exercise Two:
shows = [{"name": "Squid Game", "rating": 8.1, "channel": "Netflix"},
         {"name": "You", "rating": 7.7, "channel": "Netflix"},
         {"name": "The Good Doctor", "rating": 8.1, "channel": "ABC"},
         {"name": "Game of Thrones", "rating": 9.2, "channel": "HBO"}]

for show in shows:
    print(f"{show['name']}, currently on {show['channel']}, has a rating of {show['rating']} stars out of 10.")

# Your Practice!

# Exercise One
capital = ["Monaco", "Brussels", "Lisbon", "Kathmandu", "Tehran", "Kinshasa", "Beijing"]

country = ["Monaco", "Belgium", "Portugal", "Nepal", "Iran", "DRC", "China"]

population = [.03, .15, .56, 1, 8.69, 12.69, 21.54]

size = None

for i in range(0, len(capital)):
    cap = capital[i]
    coun = country[i]
    pop = population[i]
    if pop < 1:
        size = "small"
    elif pop < 10:
        size = "medium"
    else:
        size = "large"
    pop = str(pop * 1000000)
    print(f"The capital of {coun} is {cap}, and it is a {size} capital with a population of {pop}")

# Exercise Two:
dishes_amount = int(input("How many dishes do you have for us today? "))

cal_total = 0
sugar_total = 0
for i in range(0, dishes_amount):
    cal = int(input(f"How many calories are in the dish {i + 1}? "))
    sugar = int(input(f"How many grams of sugar are in dish {i + 1} (in grams)? "))
    cal_total += cal
    sugar_total += sugar

print(f"Your total calorie count for all of your dishes is {cal_total} and your  sugar total is {sugar_total} g.")
