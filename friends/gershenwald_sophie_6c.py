#Sophie Gershenwald, Assignment 6, Part C

import random, string

def add_letters(word, number):
    new_word = ''

    for letter in word:
        new_word+=letter
        new_word+= random.choice(string.ascii_letters)*number
    print(new_word)
    return new_word

def remove_letters(word, number):
    return word[::number+1]

def shift_characters(word, num):
    new_word = []
    for character in word:
        shift = ord(character) + num
        newchr = chr(shift)
        new_word.append(newchr)

    return "".join(new_word)

def main():
    whichFunc = raw_input("(e)ncode, (d)ecode or (q)uit: ")

    while(whichFunc != "e" or whichFunc != "d" or whichFunc!="q"):
        whichFunc = raw_input("(e)ncode, (d)ecode or (q)uit: ")

    if whichFunc == "e":
        num = input("Enter a number between 1 and 5:")
        while num < 1 or num > 5:
            print("Not valid.")
            num = input("Enter a number between 1 and 5:")
        word = raw_input("Enter a phrase to encode: ")
        toshift = add_letters(word, num)
        final_word = shift_characters(toshift, num)
        print("Your encoded phrase is: " + final_word)

    elif whichFunc == "d":
        num = input("Enter a number between 1 and 5:")
        while num < 1 or num > 5:
            print("Not valid.")
            num = input("Enter a number between 1 and 5:")

        word = raw_input("Enter a phrase to decode: ")
        # tounshift = remove_letters(word, num)
        shifted_word = shift_characters(word, (num * -1))
        final_word = remove_letters(shifted_word, (num))

        print("Your encoded phrase is: " + final_word)

    elif whichFunc == "q":
        return ("Have a good day")
main()

#decode debugging -- sophie : tmpQqUinjxfd