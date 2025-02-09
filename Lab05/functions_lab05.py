# Importing the random library to use for the dice later
import random

# Hero's Attack Function
def hero_attacks(combat_strength, m_health_points):
    # Printing the ASCII image for the attack
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
    # Analyzing the damage between the player and the monster
    print("    |    Player's weapon (" + str(combat_strength) + ") ---> Monster (" + str(m_health_points) + ")")
    if combat_strength >= m_health_points:
        # If the player's strength is greater than or equal to the monster's health, the monster is defeated
        m_health_points = 0
        print("    |    You have killed the monster")
    else:
        # If the player only damages the monster, reducing its health
        m_health_points -= combat_strength
        print("    |    You have reduced the monster's health to: " + str(m_health_points))
    return m_health_points

# Monster's Attack Function
def monster_attacks(m_combat_strength, health_points):
    # Printing the ASCII image for the monster's attack
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
    # Analyzing the damage between the monster and the player
    print("    |    Monster's Claw (" + str(m_combat_strength) + ") ---> Player (" + str(health_points) + ")")
    if m_combat_strength >= health_points:
        # If the monster's strength is greater than or equal to the player's health, the player is defeated
        health_points = 0
        print("    |    Player is dead")
    else:
        # If the monster only damages the player, reducing its health
        health_points -= m_combat_strength
        print("    |    The monster has reduced Player's health to: " + str(health_points))
    return health_points

# Function to collect loot
def collect_loot(loot_options, belt):
    print("!!You find a loot bag!! You look inside to find 2 items:")
    # Selecting loot randomly and adding to the belt
    lootRoll = random.choice(range(1, len(loot_options) + 1))
    loot = loot_options.pop(lootRoll - 1)
    belt.append(loot)
    print("Your belt: ", belt)

    # Collecting second loot item
    lootRoll = random.choice(range(1, len(loot_options) + 1))
    loot = loot_options.pop(lootRoll - 1)
    belt.append(loot)
    print("Your belt: ", belt)

    # Sorting the belt alphabetically
    belt.sort()
    print("Your belt: ", belt)

    return belt, loot_options

# Function to use loot
def use_loot(loot_options, belt, health_points):
    print("!!You see a monster in the distance! So you quickly use your first item:")
    # Using loot from the belt to modify health
    first_item = belt.pop(0)
    if first_item in good_loot_options:
        health_points = min(6, (health_points + 2))
        print("You used " + first_item + " to up your health to " + str(health_points))
    elif first_item in bad_loot_options:
        health_points = max(0, (health_points - 2))
        print("You used " + first_item + " to hurt your health to " + str(health_points))
    else:
        print("You used " + first_item + " but it's not helpful")
    return health_points
