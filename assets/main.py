import random

WORD_LIST = []
LETTERS_LEN = 5

def GenerateWord():
    try:
        with open("words_alpha.txt", "r") as dictionary:
            for word in dictionary.readline():
                if len(word.strip()) == LETTERS_LEN:
                    WORD_LIST.append(word.strip())
    except FileNotFoundError:
        print("[!] Error! File not Found.")
    # value = word.randint(LETTERS_LEN)
    # return  str(value)

def main():
    target = WORD_LIST[random.randint(len(WORD_LIST))]
    print(target)
    # print(target)
    # guess = input("please type in your guess: ")
    # response = ["Bascat" for i in range(len(target))]
    #
    # if guess == target:
    #     print("Correct")
    #
    # else:
    #     for g_digit in range(len(guess)):
    #         for t_digit in range(len(target)):
    #             if guess[g_digit] == target[t_digit]:
    #                 if g_digit == t_digit:
    #                     response[g_digit] = "Chophy"
    #                 else:
    #                     response[g_digit] = "Storts"
    # print(response)

if __name__ == '__main__':
    main()
