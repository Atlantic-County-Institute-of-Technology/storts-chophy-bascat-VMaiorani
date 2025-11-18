import random

WORD_LIST = []
Lives = 4

def generateword():
    try:
        with open("words_alpha.txt", "r") as dictionary:
            for word in dictionary:
                if len(word.strip()) == LETTERS_LEN:
                    WORD_LIST.append(word.strip())
    except FileNotFoundError:
        print("[!] Error! File not Found.")

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

def difficulty():
    global LETTERS_LEN
    while True:
        dif = int(input("Please select a difficulty [ 1 = EASY, 2 = MEDIUM, 3 = HARD ] :"))
        if dif == 1:
            print("You selected difficulty EASY, the word is 4 letters long")
            LETTERS_LEN = 4
            break
        elif dif == 2:
            print("You selected difficulty MEDIUM, the word is 5 letters long")
            LETTERS_LEN = 5
            break
        elif dif == 3:
            print("You selected difficulty HARD, the word is 6 letters long")
            LETTERS_LEN = 6
            break
        else:
            print("pls select an option available")

def main():
    lives = 4
    difficulty()
    generateword()
    target = WORD_LIST[random.randint(0, len(WORD_LIST))]
    print(target)

    while lives >= 0:
        print(LETTERS_LEN)
        guess = input("please type in your guess: ")
        response = []
        for letter in guess:
            response.append(f"{letter} = Bascat")
        if len(guess) == len(target):
            if guess in WORD_LIST:
                if guess == target:
                    print("Correct: You Win")
                    break
                else:
                    print("current tries: " + str(lives))
                    for g_digit in range(len(guess)):
                        for t_digit in range(len(target)):
                            if guess[g_digit] == target[t_digit]:
                                if g_digit == t_digit:
                                    response[g_digit] = str(guess[g_digit]) + " = Chophy"
                                else:
                                    response[g_digit] = str(guess[g_digit]) + " = Storts"
                    print(response)
                lives -= 1
            elif guess not in WORD_LIST:
                print("Word not found in the dictionary")
        else:
            print("please enter a letter word that is at least " + str(len(target)))
    replay()

if __name__ == '__main__':
    main()
