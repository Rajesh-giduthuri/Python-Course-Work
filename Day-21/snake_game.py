import random

start = input("Enter 1 to start the game: ")

if start == "1":
    pos = 0
    count = 0

    while pos < 100:
        input("Press Enter to roll the dice: ")

        dice = random.randint(1, 6)
        print(f"You rolled a {dice}")

        # Move only if the position doesn't exceed 100
        if pos + dice <= 100:
            pos = pos + dice

        # Ladders
        if pos == 4:
            pos = 14
            print("You got a ladder!")
        elif pos == 21:
            pos = 70
            print("You got a ladder!")
        elif pos == 25:
            pos=80
            print("You got a ladder!")
        elif pos==5:
            pos=98
            print("You got a ladder!")    

        # Snakes
        elif pos == 15:
            pos = 1
            print("Snake! It bit you. You moved down.")
        elif pos == 27:
            pos = 4
            print("Snake! It bit you. You moved down.")
        elif pos == 55:
            pos=10
            print("Snake! It bit you. You moved down.") 
        elif pos == 35:
            pos=2
            print("Snake! It bit you. You moved down.")   
        elif pos == 67:
            pos=33
            print("Snake! It bit you. You moved down.")  
        elif pos == 91:
            pos=19
            print("Snake! It bit you. You moved down.")             
        count += 1

        print(f"Your position is: {pos}")
        print("----------------")

    print("Game over!")
    print("You reached the end! Winner!")
    print(f"Total dice rolls: {count}")

else:
    print("Enter 1 to play.")