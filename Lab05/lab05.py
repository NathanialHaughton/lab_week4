# Importing the random library to use for random operations in the game
import random

# Importing the functions from another file to handle specific game operations
import functions_lab05

# Defining the dice options for small and big dice rolls
small_dice_options = list(range(1, 7))
big_dice_options = list(range(1, 21))

# Defining the available weapons in the game
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]

# Defining loot options that players can find
loot_options = ["Health Potion", "Poison Potion", "Secret Note", "Leather Boots", "Flimsy Gloves"]
good_loot_options = ["Health Potion", "Leather Boots"]  # Positive loot options
bad_loot_options = ["Poison Potion"]  # Negative loot options
belt = []  # Player's loot belt, starts empty

# Defining different monster powers
monster_powers = {
    "Fire Magic": 2,
    "Freeze Time": 4,
    "Super Hearing": 6
}

# Initializing the number of stars the player can earn
num_stars = 0

# Looping to get valid input for combat strength, ensuring valid input between 1-6
i = 0
input_invalid = True

# The loop is validating the player's input for combat strength
while input_invalid and i in range(5):
    print("    ------------------------------------------------------------------")
    print("    |", end="    ")
    combat_strength = input("Enter your combat Strength (1-6): ")
    print("    |", end="    ")
    m_combat_strength = input("Enter the monster's combat Strength (1-6): ")

    # Validating if the input is numeric
    if (not combat_strength.isnumeric()) or (not m_combat_strength.isnumeric()):
        print("    |    One or more invalid inputs. Player needs to enter integer numbers for Combat Strength    |")
        i = i + 1
        continue

    # Validating if the input is within the range 1-6
    elif (int(combat_strength) not in range(1, 7)) or (int(m_combat_strength)) not in range(1, 7):
        print("    |    Enter a valid integer between 1 and 6 only")
        i = i + 1
        continue

    else:
        input_invalid = False  # Exiting the loop when input is valid
        break

if not input_invalid:
    input_invalid = False
    combat_strength = int(combat_strength)
    m_combat_strength = int(m_combat_strength)

    # Rolling for a random weapon
    print("    |", end="    ")
    input("Roll the dice for your weapon (Press enter)")
    ascii_image5 = """
              , %               .           
   *      @./  #         @  &.(         
  @        /@   (      ,    @       # @ 
  @        ..@#% @     @&*#@(         % 
   &   (  @    (   / /   *    @  .   /  
     @ % #         /   .       @ ( @    
                 %   .@*                
               #         .              

             /     # @   *              

                 ,     %                
            @&@           @&@
            """
    print(ascii_image5)
    weapon_roll = random.choice(small_dice_options)

    # Adjusting combat strength based on the weapon roll
    combat_strength = min(6, (combat_strength + weapon_roll))
    print("    |    The hero\'s weapon is " + str(weapons[weapon_roll - 1]))

    # Checking the strength of the rolled weapon
    print("    ------------------------------------------------------------------")
    print("    |", end="    ")
    input("Analyze the Weapon roll (Press enter)")
    if weapon_roll <= 2:
        print("--- You rolled a weak weapon, friend")
    elif weapon_roll <= 4:
        print("--- Your weapon is meh")
    else:
        print("--- Nice weapon, friend!")

    # If the weapon rolled is not a Fist, thanking the player
    if weapons[weapon_roll - 1] != "Fist":
        print("    |    --- Thank goodness you didn't roll the Fist...")

    # Rolling for health points
    print("    |", end="    ")
    input("Roll the dice for your health points (Press enter)")
    health_points = random.choice(big_dice_options)
    print("    |    Player rolled " + str(health_points) + " health points")

    # Rolling for monster health points
    print("    |", end="    ")
    input("Roll the dice for the monster's health points (Press enter)")
    m_health_points = random.choice(big_dice_options)
    print("    |    Player rolled " + str(m_health_points) + " health points for the monster")

    # Collecting loot after the player finds a loot bag
    print("!!You find a loot bag!! You look inside to find 2 items:")
    input("Roll for first item (Press enter)")
    lootRoll = random.choice(range(1, len(loot_options) + 1))  # Rolling for loot
    loot = loot_options.pop(lootRoll - 1)  # Removing the loot item from the list
    belt.append(loot)  # Adding the loot item to the player's belt
    print("Your belt: ", belt)

    # Collecting second loot item
    input("Roll for second item (Press enter)")
    lootRoll = random.choice(range(1, len(loot_options) + 1))  # Rolling for second loot
    loot = loot_options.pop(lootRoll - 1)  # Removing the loot item from the list
    belt.append(loot)  # Adding the loot item to the belt
    print("Your belt: ", belt)

    # Sorting the belt items alphabetically for organization
    print("You're super neat, so you organize your belt alphabetically:")
    belt.sort()
    print("Your belt: ", belt)

    # Using the first loot item
    print("!!You see a monster in the distance! So you quickly use your first item:")
    first_item = belt.pop(0)  # Using the first item from the belt
    if first_item in good_loot_options:
        health_points = min(6, (health_points + 2))  # Increasing health if the loot is good
        print("You used " + first_item + " to up your health to " + str(health_points))
    elif first_item in bad_loot_options:
        health_points = max(0, (health_points - 2))  # Decreasing health if the loot is bad
        print("You used " + first_item + " to hurt your health to " + str(health_points))
    else:
        print("You used " + first_item + " but it's not helpful")                   
    
    print("    ------------------------------------------------------------------")
    print("    |", end="    ")
    input("Analyze the roll (Press enter)")

    # Comparing Player vs Monster's strength to check if it's a fair fight
    print("    |    --- You are matched in strength: " + str(combat_strength == m_combat_strength))

    # Checking if the player is strong enough to win the battle
    print("    |    --- You have a strong player: " + str((combat_strength + health_points) >= 15))

    # Rolling for the monster's magic power and modifying its combat strength
    print("    |", end="    ")
    input("Roll for Monster's Magic Power (Press enter)")
    ascii_image4 = """
                @%   @                       @     
         @     @                        
             &                           
      @      .                           

     @       @                    @     
              @                  @      
      @         @              @  @     
       @            ,@@@@@@@     @      
         @                     @        
            @               @           
                 @@@@@@@                 

                                      """
    print(ascii_image4)
    power_roll = random.choice(["Fire Magic", "Freeze Time", "Super Hearing"])

    # Modifying monster combat strength based on the power roll
    m_combat_strength += min(6, m_combat_strength + monster_powers[power_roll])
    print("    |    The monster's combat strength is now " + str(
        m_combat_strength) + " using the " + power_roll + " magic power")

    # Starting the fight sequence
    print("You meet the monster. FIGHT!!")
    while m_health_points > 0 and health_points > 0:

        input("You strike first (Press Enter)")
        m_health_points = functions_lab05.hero_attacks(combat_strength, m_health_points)  # Hero attacks the monster
        if m_health_points == 0:
            num_stars = 3  # Awarding stars for victory
        else:
            input("The monster strikes (Press Enter)")
            health_points = functions_lab05.monster_attacks(m_combat_strength, health_points)  # Monster strikes back
            if health_points == 0:
                num_stars = 1  # Losing the fight
            else:
                num_stars = 2  # Neutral outcome

    # Getting Hero name input and assigning stars based on the outcome
    hero_name = input("Enter your Hero's name (in two words): ")
    hero_name_split = hero_name.split()
    while len(hero_name_split) != 2 or not all(word.isalpha() for word in hero_name_split):
        print("Please enter your Hero's name in two valid words.")
        hero_name = input("Enter your Hero's name (in two words): ")
        hero_name_split = hero_name.split()
    
    short_name = hero_name_split[0][:2] + hero_name_split[1][0]  # Creating a short name

    stars = "*" * num_stars  # Creating a star string based on the outcome
    print(f"Hero {short_name} gets <{stars}> stars")  # Displaying stars awarded
