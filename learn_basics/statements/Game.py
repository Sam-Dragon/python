print("Welcome to Treasure Land.\n Your mission is to find the treasure.")
direction = input("You are on cross road. would you like to go left or right?")
if direction == "left":
    action = input("You need to go to island. Would you like to swim or wait?")
    if action == "wait":
        door = input("You have arrived the island. Select the door to proceed. [Red, Yellow or Blue]?")
        if door == "Yellow":
            print("You are the winner")
        else:
            print("Game Over.")
    else:
        print("Game Over.")
else:
    print("Game Over.")
