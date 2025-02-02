# Import the random library to use for the dice later
import random

# Hero's Attack Functions
def hero_attacks(combat_strength, m_health_points):
    ascii_image = """
                                @@   @@ 
                                @    @  
                                @   @   
               @@@@@@          @@  @    
            @@       @@        @ @@     
           @%         @     @@@ @       
            @        @@     @@@@@     
               @@@@@        @@       
               @    @@@@                
          @@@ @@                        
       @@     @                         
   @@*       @                          
   @        @@                          
           @@                                                    
         @   @@@@@@@                    
        @            @                   
      @              @                   
      """
    print(ascii_image)
    print("Player's weapon (" + str(combat_strength) + ") ---> Monster (" + str(m_health_points) + ")")
    if combat_strength >= m_health_points:
        m_health_points = 0
        print("You have killed the monster")
    else:
        m_health_points -= combat_strength
        print("You have reduced the monster's health to " + str(m_health_points))
    return m_health_points

# Monster's Attack Function
def monster_attacks(m_combat_strength, health_points):
    ascii_image2 = """                                                                 
           @@@@ @                           
      (     @*&@  ,                         
    @               %                       
     &#(@(@%@@@@@*   /                      
      @@@@@.                                 
               @       /                    
                %         @                  
            ,(@(*/           %              
               @ (  .@#                 @   
                          @           .@@. @
                   @         ,              
                      @       @ .@          
                             @              
                          *(*  *      
             """
    print(ascii_image2)
    print("Monster's Claw (" + str(m_combat_strength) + ") ---> Hero (" + str(health_points) + ")")
    if m_combat_strength >= health_points:
        health_points = 0
        print("You have killed the monster")
    else:
        health_points -= m_combat_strength
        print("The monster has reduced your health to " + str(health_points))
    return health_points

# Game
# Define The number of lives for the Hero and Monster
numLives = 10  # number of player's lives remaining
mNumLives = 12  # number of monster's lives remaining

# Define the Dice
diceOptions = list(range(1, 7))
# Define the Weapons
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]

# Print out the weapons using a for loop
for weapon in weapons:
    print(weapon)

# Define the Loot
loot_options = ["Health Potion", "Poison Potion", "Secret Note", "Leather Boots", "Flimsy Gloves"]
good_loot_options = ["Health Potion", "Leather Boots"]
bad_loot_options = ["Poison Potion"]

# Define the number of stars awarded to the Player
num_stars = 0

# Use a While Loop to get valid input for Hero and Monster's Combat Strength
i = 0

while i in range(5):
    combat_strength = input("Enter your combat Strength (1-6): ")
    m_combat_strength = input("Enter the monster's combat Strength (1-6): ")

    # Validate input: Check if the string inputted is numeric
    if (not combat_strength.isnumeric()) or (not m_combat_strength.isnumeric()):
        # If one of the inputs are invalid, print error message and halt
        print("One or more invalid inputs. Player needs to enter integer numbers for Combat Strength")
        i = i + 1
        continue

    # Note: Now safe to cast combat_strength to integer
    # Validate input: Check if the string inputted is a number between 1-6
    elif (int(combat_strength) not in range(1, 7)) or (int(m_combat_strength)) not in range(1, 7):
        print("Enter a valid integer between 1 and 6 only")
        i = i + 1
        continue

    # Break out of while loop if input was valid
    else:
        break

# Input was valid - broke out of while loop
combat_strength = int(combat_strength)
m_combat_strength = int(m_combat_strength)

# Roll for weapon
input("Roll the dice for your weapon (Press enter)")
weaponRoll = random.choice(diceOptions)

# Max out the combat strength at 6
combat_strength = min(6, (combat_strength + weaponRoll))
print("The hero\'s weapon is " + str(weapons[weaponRoll - 1]))

# Weapon Roll Analysis
input("Analyze the Weapon roll (Press enter)")
if weaponRoll <= 2:
    print("--- You rolled a weak weapon, friend")
elif weaponRoll <= 4:
    print("--- Your weapon is meh")
else:
    print("--- Nice weapon, friend!")

# If the weapon rolled is not a Fist, print out "Thank goodness you didn't roll the Fist..."
if weapons[weaponRoll - 1] != "Fist":
    print("--- Thank goodness you didn't roll the Fist...")

# Roll for player health points
input("Roll the dice for your health points (Press enter)")
health_points = random.choice(diceOptions)
print("Player rolled " + str(health_points) + " health points")

# Roll for monster health points
input("Roll the dice for the monster's health points (Press enter)")
m_health_points = random.choice(diceOptions)
print("Player rolled " + str(m_health_points) + " health points for the monster")

input("Analyze the roll (Press enter)")
# Compare Player vs Monster's strength
print("--- You are matched in strength: " + str(combat_strength == m_combat_strength))

# Check the Player's overall strength and health
print("--- You have a strong player: " + str((combat_strength + health_points) >= 15))

# Loop while the monster and the player are alive. Call fight sequence functions
print("You meet the monster. FIGHT!!")
while m_health_points > 0 and health_points > 0:

    input("You strike first (Press Enter)")
    m_health_points = hero_attacks(combat_strength, m_health_points)
    if m_health_points == 0:
        num_stars = 3
    else:
        input("The monster strikes (Press Enter)")
        health_points = monster_attacks(m_combat_strength, health_points)
        if health_points == 0:
            num_stars = 1
        else:
            num_stars = 2

stars = "*" * num_stars
print("Hero gets <" + stars + "> stars")

# Define Monster's Powers
# Creating a dictionary to store the monster's magic powers and their corresponding strengths
monster_powers = {
    "Fire Magic": 2,        # Fire Magic has a strength of 2
    "Freeze Time": 4,       # Freeze Time has a strength of 4
    "Super Hearing": 6      # Super Hearing has a strength of 6
}

# Roll for Monster's Magic Power
# Simulating the roll for the monster's magic power by randomly selecting one of the monster's powers
input("Press Enter to roll for the monster's magic power")
selected_power = random.choice(list(monster_powers.keys()))  # Randomly selecting a magic power
print(f"Monster rolled: {selected_power} with strength {monster_powers[selected_power]}")

# Update Monster's Combat Strength
# Increasing the monster's combat strength based on the rolled magic power
m_combat_strength = min(m_combat_strength + monster_powers[selected_power], 6)  # Ensuring the combat strength doesn't exceed 6
print(f"Monster's updated combat strength: {m_combat_strength}")

# Define the Loot Belt
# Creating an empty list called 'belt' to store the player's collected loot items
belt = []

# Collecting Loot for the Player
# Indicating that the player has found a loot bag and prompting for input to start the collection
print("You found a loot bag!")
input("Press Enter to roll for the first item in your loot bag")

# Rolling for the first item and adding it to the belt
first_loot = random.choice(loot_options)  # Selecting a random loot item
loot_options.remove(first_loot)  # Removing the selected item from loot options
belt.append(first_loot)  # Adding the loot item to the player's belt
print(f"You collected: {first_loot}")
print(f"Your belt contains: {belt}")

# Collecting the Second Loot Item
# Repeating the loot collection process for the second item
input("Press Enter to roll for the second item in your loot bag")
second_loot = random.choice(loot_options)  # Selecting a second loot item
loot_options.remove(second_loot)  # Removing the second item from loot options
belt.append(second_loot)  # Adding the second loot item to the player's belt
print(f"You collected: {second_loot}")
print(f"Your belt now contains: {belt}")

# Organizing the Loot Belt
# Sorting the items in the player's belt alphabetically
print("Organizing your loot belt alphabetically...")
belt.sort()  # Sorting the belt items
print(f"Your belt is now organized: {belt}")

# Using the First Loot Item
# Indicating the monster encounter and prompting the player to use the first loot item
print("You see a monster in the distance. You can use the first item in your belt.")
first_item_used = belt.pop(0)  # Removing the first item from the belt
print(f"You used: {first_item_used}")

# Checking the type of loot and adjusting health points
if first_item_used in good_loot_options:  # If the loot is beneficial
    health_points = min(health_points + 2, 6)  # Increasing health points but not exceeding 6
    print(f"Your health has increased to {health_points}")
elif first_item_used in bad_loot_options:  # If the loot is harmful
    health_points = max(health_points - 2, 0)  # Decreasing health points but not dropping below 0
    print(f"Your health has decreased to {health_points}")
else:
    print("This item was not helpful.")
