import random

class Item:
    """
    Represents an item that can be dropped.
    
    Attributes:
        name (str): The name of the item.
        rarity (int): The rarity of the item (0-99, higher values are rarer).
    """
    def __init__(self, name, rarity):
        self.name = name
        self.rarity = rarity

def drop_random_items(enemy_level):
    """
    Simulates dropping random items after defeating an enemy in battle.
    
    Args:
        enemy_level (int): The level of the defeated enemy.
        
    Returns:
        list: A list of dropped Item objects.
    """
    # Define a list of possible items and their rarities
    possible_items = [
        Item("Health Potion", 50),
        Item("Mana Potion", 40),
        Item("Gold Coin", 90),
        Item("Sword", 10),
        Item("Shield", 20)
    ]

    # Initialize a list to store the dropped items
    dropped_items = []

    # Determine the number of items to drop based on enemy level
    if 1 <= enemy_level <= 5:
        number_of_items_to_drop = 1
    elif 6 <= enemy_level <= 10:
        number_of_items_to_drop = 2
    else:
        number_of_items_to_drop = 3

    # Randomly select items to drop based on rarity
    for _ in range(number_of_items_to_drop):
        random_value = random.randint(0, 99)  # Generate a random value between 0 and 99

        # Filter items based on their rarity
        filtered_items = [item for item in possible_items if random_value < item.rarity]

        # If there are filtered items, randomly select one and add it to the dropped_items list
        if filtered_items:
            random_item = random.choice(filtered_items)
            dropped_items.append(random_item)

    return dropped_items

def main():
    enemy_level = 8  # Replace with the actual enemy level
    dropped_items = drop_random_items(enemy_level)

    print("Dropped Items:")
    for item in dropped_items:
        print(f"{item.name} ({item.rarity} rarity)")

if __name__ == "__main__":
    main()
