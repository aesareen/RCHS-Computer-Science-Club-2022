import random as rand

# Track One
spanish_word = input("Please enter a Spanish Word: ")

if spanish_word[-1] == 'o':
    print(f"{spanish_word} is a masculine word!")
elif spanish_word[-1] == 'a':
    print(f"{spanish_word} is a feminine word!")
else:
    print(f"I can not tell if {spanish_word} is a Spanish word")


# Track Two
def people():
    first_names = ["Juan", "María", "José", "Pedro", "Alejandra", "Rosa", "Rico"]

    last_names = ["García", "Rodríguez", "Martín", "Rubio", "Hernández", "González"]

    professions = ["carpenter", "musician", "police worker", "street food vendor"]

    cities = ["Mexico City", "Guadalajara", "Tijuana", "Saltillo", "Puebla"]

    first_name = rand.choice(first_names)
    last_name = rand.choice(last_names)
    profession = rand.choice(professions)
    city = rand.choice(cities)
    age = str(rand.randint(21, 74))

    return print(f"{first_name} {last_name} is a {age} year old {profession} from {city}.")


people()
