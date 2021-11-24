import random
random.seed()


def main():
    name = input("Enter your name: ")
    print(f"Hello, {name}")
    rating = 0
    with open("rating.txt", "r") as ratings:
        for line in ratings:
            line = line.split()
            if line[0] == name:
                rating = int(line[1])
                break
    options = input().split(",")
    if options == ['']:
        options = ["rock", "paper", "scissors"]
    print("Okay, let's start")

    while True:
        human = input()
        if human == "!exit":
            break
        if human == "!rating":
            print("Your rating:", rating)
        if human not in options:
            print("Invalid input")
            continue
        computer = random.choice(options)
        if computer == human:
            print(f"There is a draw ({computer})")
            rating += 50
            continue

        if winner(options, human, computer) == 'human':
            print(f"Well done. The computer chose {computer} and failed")
            rating += 100
        else:
            print(f"Sorry, but the computer chose {computer}")


def winner(options, human, computer):
    while options[0] != human:
        options.insert(0, options.pop())
    winners = options[1:int((len(options) + 1) / 2)]
    if computer in winners:
        return "computer"
    return "human"


if __name__ == "__main__":
    main()
