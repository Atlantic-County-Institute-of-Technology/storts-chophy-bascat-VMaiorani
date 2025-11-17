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
    return word

def replay():
    while True:
        play = int(input("Would you like to play again [1 = Yes, 2 = No]:"))
        if play == 1:
            print("Continuing Game...")
            break
        elif play == 2:
            print("Game Shutting Down...")
            exit()
        else:
            print("pls select an option available")
    main()

def main():
    lives = 4
    generateword()
    target = WORD_LIST[random.randint(0, len(WORD_LIST))]
    print(target)

    # if Lives >= 0:
    while lives >= 0:
        temp = 0
        guess = input("please type in your guess: ")
        response = ["Bacat" for i in range(len(target))]
        if len(guess) == 5:
            if guess == target:
                print("Correct: You Win")
                break
            else:
                print("current tries: " + str(lives))
                for g_digit in range(len(guess)):
                    for t_digit in range(len(target)):
                        if guess[g_digit] == target[t_digit]:
                            if g_digit == t_digit:
                                response[g_digit] = str(guess[temp]) + " = Chophy"
                            else:
                                response[g_digit] = str(guess[temp]) + " = Storts"
                            temp += 1
                print(response)
            lives -= 1
        else:
            print("please enter a 5 letter word")
    replay()

if __name__ == '__main__':
    main()
