# Enter your code here. Read input from STDIN. Print output to STDOUT

"""
Code logic: 
1) Read in the input
2) Split the input by "/" as the slash indicates the separation between expression tree and operation
**Note: the check of: if "/" in n does not compile in this editor, ever. This makes accounting for one of the first edge cases really difficult.
3) identify which half of the split input goes to express tree and which ones goes to operation. make sure to keep all the letters in operation uppercase (hence the .upper() method)

4) identify if the operation is empty or None or a space --> if so, just return the expression tree as is. 
otherwise, for every letter in operation, complete that command. 

5) the R command, or reverse, can be written with a stack (push all the letters to a stack and then append each popped character to a new list)

6) the S command, or simplify, is the tricky one. we can either create an actual expression tree out of this or go by brute force. In the first hour of completing this exercise, I went with brute force. 
    1) split the word based on "("
    2) filter out the empty elements of that split list
    3) for each element in the split expression tree list, count how many closed parentheses there are ")". this acts as a naive stack implementation. based on how many parentheses there are, simplify accordingly. here there are 3-4 edge cases (if you have one ")", 2 or more ")", or none at all)
    4) then simplify the simplified expression by double checking if the first element is a "(" or not. if it is, then you take out the first pair of parentheses. if it is not, then you print as is. (this is another edge case)
    
Notes: some things that I tried to account for , like the length of the input after splitting, broke the console. I wish there was the ability to run the code and see my output for what it was rather than having it cut off after 5 lines. This was not the same error(S) that I was receiving when I was printing/testing the code in my personal IDE. 

Checks like the following failed in the main running of the code in the HackerRank IDE but was not the same errors I was receiving in my personal one:
    #if("/" not in n): #verify that you have a slash and can split it. if you don't then assign a blank operation and the input to exp_tree. 
        #exp_tree = n
        #operation = ""
    #else:
        #split_n = n[i].split("/")
        #if(len(split_n) == 2):
        #exp_tree = "".join(split_n[0].split())
        #operation = "".join(split_n[1].split()).upper() # we are making sure that everything is uppercase for the denoted operation

This code also failed for one test case (aka the main execution of my method)

for i in n:
    split_n = i.split("/")
    # print("split_n",split_n)
    if(len(split_n) == 2): #CODE FAILED HERE AT THIS LINE
        exp_tree = "".join(split_n[0].split())
        operation = "".join(split_n[1].split()).upper()
    else:
        exp_tree = "".join(split_n[0].split())
        operation = ""

    if (operation == " " or operation == None or operation == ""):
        print(exp_tree)
    else:
        final_result = exp_tree
        for letter in operation:
            # print(letter)
            if (letter == "R"):
                final_result = r_reverse(final_result)
            elif (letter == "S"):
                final_result = s_simplify(final_result)
        print(final_result)

Every time I would try to include tests like "if parameter exists", the code would break in HackerRank but it was more than okay for my personal IDE. 

I decided to keep my code more organized by writing a method for the R command and a method for the S command

The most natural way I first wrote Reverse was return word[::-1], but then I realized that I had to also switch the parentheses. hence, writing a for loop to account for the cases of the parentheses. 

"""

import sys
s = sys.stdin.read()
n = s.split("\n") #n is now an array of all the input

def r_reverse(word):
    normal_exp_tree = "".join(word.split())
    reverse_tree = []
    for i in reversed(normal_exp_tree):
        if (i == ")"):
            reverse_tree.append("(")
        elif (i == "("):
            reverse_tree.append(")")
        else:
            reverse_tree.append(i)
    new_word = "".join(reverse_tree)
    return(new_word)

def s_simplify(word):
    normal_exp_tree = "".join(word.split())
    exp_split = normal_exp_tree.split("(")
    exp_split = filter(None, exp_split)
    
    # print(exp_split)
    simplified = []
    for i in exp_split:
        if (i.count(")") >= 2):
            simplified.append("("*(i.count(")")-1)+"".join(i.split(")"))+")"*(i.count(")")-1))
        elif (i.count(")") < 2 and i.count(")") > 0 and i.count("(") == 0):
            simplified.append("(" + "".join(i.split(")")) + ")")
        elif (i.count(")") == 0):
            simplified.append("".join(i.split(")")))


    simplified = "".join(filter(None, simplified))
    # print(simplified)
    for i in simplified:
        if i == "(" and simplified.index(i) == 0:

            simplified = simplified[1:]#.replace("(", "")
            simplified = simplified.replace(")", "", 1)
    # print("****", simplified)
    return simplified


for i in range(len(n)):
    
    split_n = n[i].split("/")
    #if(len(split_n) == 2):
    exp_tree = "".join(split_n[0].split())
    operation = "".join(split_n[1].split()).upper() # we are making sure that everything is uppercase for the denoted operation

    if (operation == " " or operation == None or operation == ""):#if the operation is blank, then we are going to return the expression tree
        print(exp_tree)
    else: #if we have an operation or series of operation
        final_result = exp_tree #create a base word that we will ultimately print
        for letter in operation: #for each command/letter in our operation sequence, identify if it is S, R, or neither
            if (letter == "R"): #if it is R, then reverse the exp_tree
                final_result = r_reverse(final_result)
            elif (letter == "S"): #if it is S, then simplify it
                final_result = s_simplify(final_result)
        print(final_result)

