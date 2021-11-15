# Track One
games = ["Just Cause 4", "Minecraft", "Among Trees", "Watch Dogs 2"]

''' 
The next line is optional for Track One, but if wanted to have custom prices, you could align the prices with the 
corresponding game. So for example, Just Cause 4 costs $60, Minecraft $20, etc...
'''

game_prices = [60, 20, 20, 60]

# Create a total variable to store total price
total = 0

for i in range(0, len(games)):
    game = games[i]  # This will get the game at index i
    game_price = game_prices[i]  # Get corresponding game price at index i
    buy = input(f"Would you like to buy {game}? It will cost ${game_price} (y/n) ")
    if buy == "y":
        total += game_price

print(f"Hello! Your purchase is complete. Your bill is ${total}")


# Track Two
def games():
    games = ["Just Cause 4", "Minecraft", "Among Trees", "Watch Dogs 2"]
    game_prices = [60, 20, 20, 60]
    games_bought = []  # A list to store all of the games bought
    total = 0
    for i in range(0, len(games)):
        game = games[i]
        game_price = game_prices[i]
        buy = input(f"Would you like to buy {game}? It will cost ${game_price} (y/n) ")
        if buy == "y":
            total += game_price
            games_bought.append(game)
    # Input to check if member of CompSci Discount Club
    member = input("Are you a member of the CompSci Video Game Discount Program? (y/n) ")
    if member == "y":
        discount = total * .2  # Calculate Discount
        total = total - discount  # Apply Discount
        print(
            f"Hello! Thanks for being a valued member of the CompSci Discount Program! You have received a ${discount} discount, and your total now is ${round(total * 1.0475, 2)} (with tax). The games you got are: {games_bought}")  # Print out final total with discount
    else:
        print(
            f"Hello! Your purchase is complete. Your bill is ${round(total * 1.0475, 2)} (with tax). The games you got are: {games_bought}")  # Final total without discount


games()
