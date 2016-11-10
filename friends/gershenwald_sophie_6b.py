#Sophie Gershenwald, Assignment 6, Part 2

def funcName(name):
    print(name+"****")
    word = name.upper()
    asum = 0
    for letter in word:
        print(letter)
        if letter == "A" or letter == "J" or letter == "S":
            asum += 1
        elif letter == "B" or letter == "K" or letter == "T":
            asum += 2
        elif letter == "C" or letter == "L" or letter == "U":
            asum += 3
        elif letter == "D" or letter == "M" or letter == "V":
            asum += 4
        elif letter == "E" or letter == "N" or letter == "W":
            asum += 5
        elif letter == "F" or letter == "O" or letter == "X":
            asum += 6
        elif letter == "G" or letter == "P" or letter == "Y":
            asum += 7
        elif letter == "H" or letter == "Q" or letter == "Z":
            asum += 8
        elif letter == "I" or letter == "R":
            asum += 9
        else: #elif c == " " or "." or "-" or "!":
            asum += 0

    return int(asum)

def personality_number(name):
    asum = funcName(name) #asum is of type int
    asum_list = []
    while int(asum) >= 10 and (int(asum) != 11 or int(asum) != 22):
        for integer in str(asum):
            asum_list.append(int(integer))
        asum = sum((asum_list))
        print(asum_list, asum)
    num = str(asum)

    if num == "1":
        return('Your personality number is: ' + num + "\n" + 'Your personality associations are: initiating action, pioneering, leading, independent, attaining, individual')
    elif num == "2":
        return('Your personality number is: ' + num + "\n" + 'Your personality associations are: cooperation, adaptability, consideration of others, partnering, mediating')
    elif num == "3":
        return('Your personality number is: ' + num + "\n" + 'Your personality associations are: expression, verbalization, socialization, the arts, the joy of living')
    elif num == "4":
        return('Your personality number is: ' + num + "\n" + 'Your personality associations are: a foundation, order, service, struggle against limits, steady growth')
    elif num == "5":
        return('Your personality number is: ' + num + "\n" + 'Your personality associations are: expansiveness, visionary, adventure, the constructive use of freedom')
    elif num == "6":
        return('Your personality number is: ' + num + "\n" + 'Your personality associations are: responsibility, protection, nurturing, community, balance, sympathy')
    elif num == "7":
        return('Your personality number is: ' + num + "\n" + 'Your personality associations are: analysis, understanding, knowledge, awareness, studious, meditating')
    elif num == "8":
        return('Your personality number is: ' + num + "\n" + 'Your personality associations are: practical endeavors, status oriented, power seeking, material goals')
    elif num == "9":
        return('Your personality number is: ' + num + "\n" + 'Your personality associations are: humanitarian, giving nature, selflessness, obligations, creative expression')
    elif num == "11":
        return('Your personality number is: ' + num + "\n" + 'Your personality associations are: higher spiritual plane, intuitive, illumination, idealist, a dreamer')
    elif num == "22":
        return('Your personality number is: ' + num + "\n" + 'Your personality associations are: the Master Builder, large endeavors, powerful force, leadership')

def main():
    name = raw_input("Enter your name: ")
    print(personality_number(name))   

main()

