# Enter your code here. Read input from STDIN. Print output to STDOUT
#n = input() #(AB) C((D E )F) /S
#print(n)
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
    # print("normal_exp_tree: "+normal_exp_tree)
    exp_split = normal_exp_tree.split("(")
    # print("exp_split: ")
    # print(exp_split)
    exp_split = filter(None, exp_split)
    # print(exp_split)
    # print("****")
    simplified = []
    for i in exp_split:
        if (i.count(")") >= 2):
            simplified.append("("*(i.count(")")-1)+"".join(i.split(")"))+")"*(i.count(")")-1))
        elif (i.count(")") < 2 and i.count(")") > 0):
            # simplified.append("".join(i.split(")")))
            simplified.append("(" + "".join(i.split(")")) + ")")
        elif (i.count(")") == 0):
            simplified.append("".join(i.split(")")))
    simplified = filter(None, simplified)
    # print("".join(simplified))
    return("".join(simplified))


for i in range(len(n)):
    split_n = n[i].split("/")

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


