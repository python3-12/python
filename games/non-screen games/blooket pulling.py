import random
import pygame
from time import sleep
from datetime import datetime

print("Welcome to Blooket Pack Opening Simulator!!\nAre you ready to open some packs? (We also sell Blooks here)")
sleep(4)

# Initialize Pygame Mixer
pygame.mixer.init()

# Define ANSI escape codes for colors
BRIGHT_YELLOW_BG = "\033[1;43m"
RESET = "\033[0m"

collected_blooks = []

# Item categories with their items and probabilities
ITEM_CATEGORIES = {
    "mystical": (["phantom king", "rainbow astronaut"], 0.001),
    "chroma": (["blue slime monster", "rainbow panda"], 0.02),
    "legendary": (["megalodon", "mega bot"], 0.5),
    "epic": (["Bush monster", "Triceratops"], 3),
    "rare": (["UFO", "Buddy bot"], 7),
    "uncommon": (["Happy bot", "stars"], 17),
    "common": (["anaconda", "chick"], 23),
}

# Player coins at the start
coins = 35

# Define spinning wheel outcomes with probabilities
SPINNING_WHEEL_OUTCOMES = [
    (1000, 5),
    (100, 15),
    (70, 20),  # 10% chance to get 50 coins
    (40, 25),  # 20% chance to get 25 coins
    (20, 30),  # 30% chance to get 10 coins
    (10, 35),   # 40% chance to get 5 coins
]

def spin_wheel():
    total = 0
    cumulative_distribution = []
    
    for outcome, probability in SPINNING_WHEEL_OUTCOMES:
        total += probability
        cumulative_distribution.append((total, outcome))

    rand = random.randint(1, 100)
    
    for cumulative, outcome in cumulative_distribution:
        if rand <= cumulative:
            return outcome

def choose_category():
    total = sum(prob for _, prob in ITEM_CATEGORIES.values())
    rand = random.uniform(0, total)
    
    cumulative = 0
    for category, (items, prob) in ITEM_CATEGORIES.items():
        cumulative += prob
        if rand < cumulative:
            return category

def randomizer():
    category = choose_category()
    item = random.choice(ITEM_CATEGORIES[category][0])
    sleep(1.3)
    return category, item

def open_packs():
    global coins
    if coins < 25:
        print("Not enough coins to buy packs. You need 25 coins.")
        return

    coins -= 25  # Deduct the cost of the five-pack
    for _ in range(5):
        category, item = randomizer()
        print(f"{BRIGHT_YELLOW_BG}{category.capitalize()}: {item}{RESET}")
        collected_blooks.append((category, item))
        sleep(1.5)

def sell_collected_blooks():
    global coins
    if not collected_blooks:
        print("You have no Blooks to sell.")
        return

    print("Your collected Blooks:")
    for index, (category, item) in enumerate(collected_blooks):
        print(f"{index + 1}. {item} (Category: {category})")

    sell_indices = input("Enter the numbers of the Blooks you want to sell (or 'all' to sell all, 'cancel' to go back): ").strip().lower()
    
    if sell_indices == 'cancel':
        return
    elif sell_indices == 'all':
        sell_indices = list(range(len(collected_blooks)))  # Sell all Blooks
    else:
        try:
            sell_indices = [int(i) - 1 for i in sell_indices.split(',')]
        except ValueError:
            print("Invalid input. Please enter numbers separated by commas or 'all'.")
            return

    total_coins = 0

    for index in sell_indices:
        if 0 <= index < len(collected_blooks):
            category, item = collected_blooks.pop(index)
            total_coins += sell_item(category)
            print(f"You sold {item} for {sell_item(category)} coins.")
        else:
            print(f"Invalid number: {index + 1}. It has been skipped.")

    coins += total_coins
    print(f"Total coins earned from sales: {total_coins} coins.")

def sell_item(category):
    value_map = {
        "mystical": 1000,
        "chroma": 250,
        "legendary": 200,
        "epic": 75,
        "rare": 10,
        "uncommon": 5,
        "common": 1,
    }
    return value_map.get(category, 0)

# Main game loop
has_spun_wheel = False

while True:
    print(f"You have {coins} Blook Coins.")
    print("1. Open a five-pack for 25 Blook Coins.")
    if not has_spun_wheel:
        print("2. Spin the wheel for bonus coins (one-time only).")
    print("3. Sell collected Blooks.")
    print("4. Exit.")

    action = input("Choose an action (1/2/3/4): ").strip()
    if action == '1':
        open_packs()
    elif action == '2' and not has_spun_wheel:
        bonus_coins = spin_wheel()
        coins += bonus_coins
        has_spun_wheel = True  # Set the flag to indicate the wheel has been spun
        print(f"You spun the wheel and earned {bonus_coins} coins!")
    elif action == '3':
        sell_collected_blooks()
    elif action == '4':
        print("Thank you for playing!")
        break
    else:
        print("Invalid input. Please enter '1', '2', '3', or '4'.")
