import random
import time


# Greetings and start
def gameStart():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n***Welcome to Viking Journey!*** \n\nVersion Alpha 0.1 By ToonLunk\n")
    print("This is one trial of many.")
    time.sleep(3)
    cross_a_river()

def gameOver():
    beginAgain = input("\n\nYou died! Continue? Y or N  ")
    if beginAgain.lower() == "y" or beginAgain.lower() == "yes":
        gameStart()
    else:
        exit()

def again():
    again = input("\nAgain? Press Y or N ")
    if again.lower() == "y" or "yes":
        gameStart()

def keepGoing():
    input("...")
    return



# Swimming through the river conditions
def failedToCold_River():
    print("\nYou begin to swim across the river.")
    keepGoing()
    print("...")
    print("It's getting very cold...")
    keepGoing()
    print("Your body begins to freeze... you freeze to death, and drown in the freezing river.")
    gameOver()


def failedToShark_River():
    print("\nYou begin to swim across the river.")
    keepGoing()
    print("...")
    print("\nYou feel something touch your foot...")
    keepGoing()
    print(
        "\nA massive shark swims up from underneath you and bites your body clean in half. With your last breath you "
        "exclaim 'Bölva Guðunum!")
    time.sleep(5)
    gameOver()


def success_River():
    print("\nYou begin swimming across the river with all of your might.")
    print("\nIt's cold... and you can see sharks and other foul beasts beneath you...")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    keepGoing()
    print("\nThe beasts sensed your testosterone and left you alone. The cold river stood no chance against your "
          "flaming "
        "heart. \n\nYou made it!")
    time.sleep(5)
    again()


# List of possibilities going across river
swim_across_river = [failedToCold_River, failedToShark_River, success_River, ]


# Going Around River conditions


def failedToDragon_aroundRiver():
    print("\nYou begin your journey going around the river. You see two mountains with a path between the two,")
    print("which seems to be the best path.")
    keepGoing()
    print("\nThere is smoking rising from the mountain on the right, but as you approach, you see a barbarian "
          "encampment on the left. You take your odds and go witht the mountain on the right.")
    keepGoing()
    print("\nYou soon realize your mistake, as the smoke was coming from an evil Dragon!")
    keepGoing()
    print("\nYou fought brave, but the Dragon had babies, and took no chances. You are slain!")
    time.sleep(5)
    gameOver()


def failedToStarving_aroundRiver():
    print("\n\nYou know going around the river will take much longer, but decide to do it anyways. You pack your sword, "
          "shield, and ale, and head towards the east, along the embankment.")
    keepGoing()
    print("\n\nYou take the last sip of your delicious ale that your uncle's servant crafted. You're hungry.")
    keepGoing()
    print("\n\nIt's been a few days now, and somewhere along the way, you chased a rabbit in desperate need of food.")
    keepGoing()
    print("\n\nYou killed the rabbit, but lost the river along the way.")
    keepGoing()
    print("\n\nYou killed the rabbit, but lost the river along the way.")
    keepGoing()
    print("\n\nYou also remember that you're allergic to rabbit meat, and starve to death.")
    time.sleep(3)
    gameOver()


def success_aroundRiver():
    print("\nYou bravely decided to take the much longer, and harder path. Some would regard this as a pussy move, but "
          "you disagree.")
    keepGoing()
    print("'\nWow! A bridge!' you exclaim. You find an abandoned fisherman's home, and a bridge connecting it to the "
          "other side of the river.\n")
    keepGoing()
    print("You enter the home and find it completely furnished, complete with a maid!")
    keepGoing()
    print("\nShe tells you her husband is off fishing, and offers you sweetcakes and cooked fish.")
    keepGoing()
    print("\nYou decide not to pilliage their home, but instead have your fill and safely cross the bridge.")
    keepGoing()
    print("You win!")
    again()


go_around_river = [failedToDragon_aroundRiver, failedToStarving_aroundRiver, success_aroundRiver]


# Coming up to the river (the start)

def cross_a_river():
    print("\nYou come across a large river. What do you do?\n")
    print("1. Try to swim across it")
    print("2. Try to go around it")
    choice = int(input("Your choice: "))
    if choice == 1:
        random.choice(swim_across_river)()
    if choice == 2:
        random.choice(go_around_river)()

gameStart()
