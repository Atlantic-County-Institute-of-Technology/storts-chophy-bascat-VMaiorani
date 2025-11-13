import random

WORD_LIST = []
LETTERS_LEN = 5


def generateword():
    try:
        with open("words_alpha.txt", "r") as dictionary:
            for word in dictionary:
                if len(word.strip()) == LETTERS_LEN:
                    WORD_LIST.append(word.strip())
    except FileNotFoundError:
        print("[!] Error! File not Found.")

def replay():
    replay = input("Would you like to play again [1 = Yes, 2 = No]:")
    if replay == 1:
        main()
    elif replay == 2:
        print("Game shutting down...")
    else:
        print("pls select an option available")

def main():
    lives = 4
    generateword()
    target = WORD_LIST[random.randint(0, len(WORD_LIST))]
    print(target)

    # if Lives >= 0:
    while lives >= 0:
        guess = input("please type in your guess: ")
        response = ["Bascat" for i in range(len(target))]

        print("current tries: " + str(lives))
        if guess == target:
            print("Correct: You Win")
            break
        else:
            for g_digit in range(len(guess)):
                for t_digit in range(len(target)):
                    if guess[g_digit] == target[t_digit]:
                        if g_digit == t_digit:
                            response[g_digit] = "Chophy"
                        else:
                            response[g_digit] = "Storts"
            print(response)
            lives -= 1
            break
    replay()


if __name__ == '__main__':
    main()
