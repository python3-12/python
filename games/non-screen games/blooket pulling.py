import random
import pygame
from time import sleep
from datetime import datetime, timedelta

print("Welcome to Blooket Pack Opening Simulator!!\nAre you ready to open some packs?")
sleep(4)

# Initialize Pygame Mixer
pygame.mixer.init()

# Define ANSI escape codes for colors
BRIGHT_YELLOW_BG = "\033[1;43m"
RESET = "\033[0m"

bonus = random.randint(1, 100)
collected_blooks = []

# Item categories with their items and probabilities
ITEM_CATEGORIES = {
    "mystical": (["phantom king", "rainbow astronaut", "tim the alien", "spooky gost"], 0.006),
    "unique": (["wise catterpillar","wise owl"], 0.01),
    "chroma": (["blue slime monster", "rainbow panda", "teel platypus", "colored astronaut"], 0.02),
    "legendary": (["megalodon", "mega bot", "t-rex", "baby shark", "sugar glider", "astronaut"], 0.5),
    "epic": (["Bush monster", "Triceratops", "pizza", "dolphin", "narwal", "rocket ship"], 3),
    "rare": (["UFO", "Buddy bot", "watson", "brontasuarus", "jester", "planet", "space ship"], 7),
    "uncommon": (["Happy bot", "stars", "alice", "earth", "frog", "buckenear", "alien"], 17),
}
common_catagories = {
    "legendary": (["megalodon", "mega bot", "t-rex", "baby shark", "sugar glider", "astronaut"], 0.05),
    "epic": (["Bush monster", "Triceratops", "pizza", "dolphin", "narwal", "rocket ship"], 0.7),
    "rare": (["UFO", "Buddy bot", "watson", "brontasuarus", "jester", "planet", "space ship"], 3),
    "uncommon": (["Happy bot", "stars", "alice", "earth", "frog", "buckenear", "alien"], 10),
    "Abc's": (["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"], 30),
}
rare_categories = {
    "mystical": (["phantom king", "rainbow astronaut", "tim the alien", "spooky gost"], 0.09),
    "unique": (["wise catterpillar","wise owl"], 0.4),
    "chroma": (["blue slime monster", "rainbow panda", "teel platypus", "colored astronaut"], 0.7),
    "legendary": (["megalodon", "mega bot", "t-rex", "baby shark", "sugar glider", "astronaut"], 1),
    "epic": (["Bush monster", "Triceratops", "pizza", "dolphin", "narwal", "rocket ship"], 17),
    "rare": (["UFO", "Buddy bot", "watson", "brontasuarus", "jester", "planet", "space ship"], 23),
}

# Player coins at the start
coins = 75

# Define spinning wheel outcomes with probabilities
SPINNING_WHEEL_OUTCOMES = [
    (1000, 5),
    (100, 10),
    (75, 20),
    (60, 25),
    (50, 30),
    (40, 35),
    (30, 40),
    (20, 45),
    (15, 50),
]

# Track the last time the wheel was spun
last_spin_time = None

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

def choose_category(c):
    if c == 2:
        total = sum(prob for _, prob in common_catagories.values())
    elif c == 3:
        total = sum(prob for _, prob in rare_categories.values())
    else:
        total = sum(prob for _, prob in ITEM_CATEGORIES.values())
    rand = random.uniform(0, total)
    
    cumulative = 0
    if c == 2:
        for category, (items, prob) in common_catagories.items():
            cumulative += prob
            if rand < cumulative:
                return category
    elif c == 3:
        for category, (items, prob) in rare_categories.items():
            cumulative += prob
            if rand < cumulative:
                return category
    else:
        for category, (items, prob) in ITEM_CATEGORIES.items():
            cumulative += prob
            if rand < cumulative:
                return category

def randomizer(c):
    if c == 2:
        category = choose_category(2)
        item_2 = random.choice(common_catagories[category][0])
        return category, item_2
    elif c == 3:
        category = choose_category(3)
        item_3 = random.choice(rare_categories[category][0])
        return category, item_3
    else:
        category = choose_category(4)
        item = random.choice(ITEM_CATEGORIES[category][0])
        sleep(1.3)
        return category, item

def open_packs():
    global coins
    if coins < 10:
        print("Not enough coins to buy packs. You need at least ten coins.")
        return

    # Prompt user to choose between a one-pack or a five-pack
    which = input("Do you want to buy a normal pack (10 coins),rare blooks pack (25 coins), or ultra rare blooks pack (100 coins)? (1/5/10): ").strip()
    
    if which == '5':
        if coins >= 25:
            coins -= 25  # Deduct the cost of the five-pack
            for _ in range(5):
                category, item = randomizer(5)
                print(f"{BRIGHT_YELLOW_BG}{category.capitalize()}: {item}{RESET}")
                collected_blooks.append((category, item))
                sleep(1.5)
        else:
            print("You do not have enough coins for a rare blooks pack.")
    elif which == '1':
        if coins >= 10:
            coins -= 10  # Deduct the cost of the one-pack
            for _ in range(5):
                category, item_2 = randomizer(2)
                print(f"{BRIGHT_YELLOW_BG}{category.capitalize()}: {item_2}{RESET}")
                collected_blooks.append((category, item_2))
                sleep(1.5)
        else:
            print("You do not have enough coins for a normal pack.")
    elif which == '10':
        if coins >= 100:
            coins -= 100  # Deduct the cost of the one-pack
            for _ in range(1):
                category, item_3 = randomizer(3)
                print(f"{BRIGHT_YELLOW_BG}{category.capitalize()}: {item_3}{RESET}")
                collected_blooks.append((category, item_3))
                sleep(1.5)
        else:
            print("You do not have enough coins for a ultra rare pack.")
    else:
        print("Invalid input. Please enter '1' for a normal pack or '5' for a rare pack or '10' for a ultra rare pack.")


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
        "unique": 300,
        "chroma": 200,
        "legendary": 100,
        "epic": 25,
        "rare": 10,
        "uncommon": 5,
        "Abc's": 0.5
    }
    return value_map.get(category, 0)

def can_spin_wheel():
    if last_spin_time is None:
        return True  # Can spin if it's the first time

    # Check if 10 minutes have passed since the last spin
    current_time = datetime.now()
    time_diff = current_time - last_spin_time
    if time_diff >= timedelta(minutes=10):
        return True  # Allow spin after 10 minutes

    # If not enough time has passed
    remaining_time = timedelta(minutes=10) - time_diff
    print(f"You need to wait {remaining_time} before spinning again.")
    return False

# Main game loop
has_spun_wheel = False

while True:
    print(f"You have {coins} Blook Coins.")
    print("1. Open a pack.")
    print("2. Spin the wheel for bonus coins (every ten minutes).")
    print("3. Sell collected Blooks.")
    print("4. Exit.")

    action = input("Choose an action (1/2/3/4): ").strip()
    if action == '1':
        open_packs()
    elif action == '2' and can_spin_wheel():
        bonus_coins = spin_wheel()
        coins += bonus_coins
        coins += bonus
        last_spin_time = datetime.now()  # Update last spin time
        has_spun_wheel = True  # Set the flag to indicate the wheel has been spun
        print(f"You spun the wheel and earned {bonus_coins} coins and your bonus was {bonus}")
    elif action == '3':
        sell_collected_blooks()
    elif action == '4':
        print("Thank you for playing!")
        break
    else:
        print("Invalid input. Please enter '1', '2', '3', or '4'.")
