import random

wins = 0
losses = 0
ties = 0


while True:
    choice = input("Vyber si: rock / paper / scissors / quit: ").lower()

    if choice == "quit":
        print("Ukončil jsi hru")
        print("Výhry: " + str(wins))
        print("Remízy: " + str(ties))
        print("Prohry: " + str(losses))
        break

    computer = random.choice(["rock", "paper", "scissors"])
    print("Počítač vybral: " + computer)

    if choice == "rock":
        if computer == "rock":
            ties = ties + 1
            print("Remíza")
        elif computer == "paper":
            losses = losses + 1
            print("Prohrál jsi")
        elif computer == "scissors":
            wins = wins + 1
            print("Vyhrál jsi")
        else:
            print("Error")

    elif choice == "paper":
        if computer == "paper":
            ties = ties + 1
            print("Remíza")
        elif computer == "scissors":
            losses = losses + 1
            print("Prohrál jsi")
        elif computer == "rock":
            wins = wins + 1
            print("Vyhrál jsi")
        else:
            print("Chyba")

    elif choice == "scissors":
        if computer == "scissors":
            ties = ties + 1
            print("Remíza")
        elif computer == "rock":
            losses = losses + 1
            print("Prohrál jsi")
        elif computer == "paper":
            wins = wins + 1
            print("Vyhrál jsi")
        else:
            print("Chyba")

    else:
        print("Chyba")

    print("Výhry: " + str(wins))
    print("Remízy: " + str(ties))
    print("Prohry: " + str(losses))