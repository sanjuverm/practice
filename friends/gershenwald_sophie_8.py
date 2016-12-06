#Sophie Gershenwald, File Input and Output, Assignment 8


def main():
      
#Part 1
    
    file_name = input("Enter a filename (i.e. class1 for class1.txt): ")
    try:
        filename = file_name + '.txt'
        file = open(filename, 'r')
        print("Successfully opened", filename)
    except FileNotFoundError:
        print("Sorry, I can't find this filename.")

#Part 2       

    print("**** ANALYZING ****")

    valid = 0
    invalid = 0
    scorelist = []
    answerkey = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
    keysplit = answerkey.split(',')
    n_numbers = []
    filestring = file.read()
    linelist = filestring.split('\n')
    nonsort = []

    for line in linelist:
        answers = line.split(',')
        N_NUMBER = answers[0]

        if N_NUMBER[0] == "N" and N_NUMBER[1:9].isnumeric() and len(N_NUMBER) == 9:

            if len(answers) == 26:
                valid += 1
                score = 0
                for index in range(1, len(answers)):
                    useranswer = answers[index]
                    keyanswer = keysplit[index - 1]
                    if useranswer == keyanswer: 
                        score += 4
                    elif useranswer == "":
                        score += 0
                    else:
                        score -= 1
                        
                scorelist.append(score)
                nonsort.append(score)
                n_numbers.append(N_NUMBER)

            else:
                invalid += 1
                print("Invalid line of data: does not contain exactly 26 values: ")
                print(line)

        else:
            invalid += 1
            print("Invalid line of data: N number is invalid:")
            print(line)

    print()
    
    if invalid == 0:
        print("No errors found!")

    print()
    print("**** REPORT ****")
    print()
    print("Total valid lines of data:", valid)
    print("Total invalid lines of data:", invalid)
    
    print(scorelist)
    highest = max(scorelist)
    lowest = min(scorelist)

    listsum = sum(scorelist)
    listlen = len(scorelist)
    mean = float(listsum) / float(listlen)
    
    scorelist.sort()
    
    index = (listlen - 1)//2
    if listlen % 2 == 0:
        median = scorelist[index]
    else:
        median = (scorelist[index] + scorelist[index + 1])/2.0
    
    print("Mean (average) score:", mean)
    print("Highest score:", highest)
    print("Lowest score:", lowest)
    print("Range of scores:", highest - lowest)
    print("Median score:", median)

#Part 4

    content = []

    File_name = (file_name + "_grades.txt")
    file = open(File_name, 'w')
    for index in range(len(n_numbers)):
        content.append(n_numbers[index], ",", nonsort[index])
        file.write(content)

    file.write("\n")

    file.close()

    
main()
