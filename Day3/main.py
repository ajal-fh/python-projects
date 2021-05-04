banner = open('banner2.txt','r')
print(banner.read())
banner.close()
welcome_msg = '''Welcome to Treasure Island.
Your mission is to find the treasure'''

print(welcome_msg)


if (input("You're at a crossroad. Where do you want to go? Type 'left' or 'right'\n").lower() == 'left'):
    next_action = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.\n")
    if(next_action.lower() == 'wait'):
        door_color = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which color do you choose?\n")
        if (door_color.lower() == 'red'):
            print("Burnt by fire.\nGame Over.")
        elif (door_color.lower() == 'blue'):
            print("Eaten by beasts.\nGame Over.")
        elif (door_color.lower() == 'yellow'):
            print("You Win!")
        else:
            print("Game Over.")
    else:
        print("Attacked by trout.\nGame Over.")
else:
    print("Fell into a hole.\nGame Over.")


