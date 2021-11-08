# Exercise One:
string = input("What is the word? ")
for letter in string:
    print(letter)

# Exercise Two:
for num in range(1, 16):
    print(num ** 2)

# Exercise Three:
for num in range(1, 50):
    if num in [11, 8, 20, 21]:
        print(f"{num} is a lucky number!")
    else:
        if num % 2 == 0:
            print(f"{num} is an even number!")
        else:
            print(f"{num} is an odd number!")

# Exercise Four
total = 0
for num in range(10, 21, 2):
    total += num

print(total)
