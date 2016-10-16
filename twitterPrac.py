def StairCase(n):
    arr = []
    i = 1
    for i in range(1, n+1):
        arr.append(" "*(n-i)+"#"*i)

    for i in arr:
        print(i)
    #print(arr)

StairCase(6)


#Diagonal Difference: https://www.hackerrank.com/challenges/diagonal-difference?h_r=next-challenge&h_v=zen

def DiagDiff(n, a):
    #n is size of a, where a is an array
    left_diag_sum = 0
    right_diag_sum = 0

    lstart = 0
    rstart = n - 1

    for row in a:
        left_diag_sum += row[lstart]
        right_diag_sum += row[rstart]
        lstart += 1
        rstart -= 1

    diff = abs(left_diag_sum - right_diag_sum)
    print(diff)

DiagDiff(3, [[11, 2, 4],[4, 5, 6], [10, 8, -12]]) #answer should be 15

def PlusMinus(n, arr):

    pos_sum = 0
    neg_sum = 0
    zeroes = 0
    for i in range(n):
        if arr[i] > 0:
            pos_sum += 1
        elif arr[i] < 0:
            neg_sum += 1
        elif arr[i] == 0:
            zeroes += 1

    print(str(float(pos_sum)/float(n)) +"\n"+ str(float(neg_sum)/float(n)) + "\n"+ str(float(zeroes)/float(n)))

PlusMinus(6, [-4, 3, -9, 0, 4, 1])


def TimeDiff(time):# 07:05:45PM
    if(time):
        if time[-2:] == "PM":
            if(time[0:2] == "12"):
                time = time[0:len(time) - 2]
            else:
                time = str(int(time[0:2]) + 12) + time[2:len(time) - 2]
        elif time[-2:] == "AM":
            if(time[0:2] == "12"):
                time = str("00") + time[2:len(time) - 2]
            else:
                time = time[0:len(time) - 2]
        print(time)


TimeDiff("12:05:45PM")

# https://www.hackerrank.com/challenges/anagram
def Anagram1(n, arr):
    #n is the length of the arr
    num_changes_needed = []

    for i in range(n):
        word = arr[i]
        change_letter = 0

        s1 = (word[0:len(word)/2]).lower()
        s2 = (word[(len(word)/2):]).lower()

        if(len(s1) == len(s2)): #abs(len(s1)- len(s2)) <= 1 and
            #do something
            #first edge case = if they are anagrams of each other
            count1 = [0]*26
            count2 = [0]*26

            for i in s1:
                count1[ord(i)-97]+=1
            for i in s2:
                count2[ord(i)-97]+=1
            for i in range(26):
                if count1[i] != count2[i]:
                    #they are not anagrams of each other so they need to be changed
                    change_letter+=(abs(count1[i] - count2[i]))

                else:
                    change_letter+=0
            if(change_letter == 0): #they are anagrams of each other
                num_changes_needed.append(0)
            else:
                num_changes_needed.append(change_letter/2)

        else:
            num_changes_needed.append(-1)
        # print(s1, s2, num_changes_needed)
        print(num_changes_needed)

Anagram1(6, ["aaabbb", "ab", "abc", "mnop", "xyyx", "xaxbbbxx"])

print("\n\n\n")


"""
Python 3: HackerRank to read in input
import sys
s = sys.stdin.read()

n = s.split("\n")
#print(n) --> n is an array

"""
import re

def twitter1(n):
    for i in n:
        split_n = i.split("/")

        exp_tree = "".join(split_n[0].split())
        operation = "".join(split_n[1].split()).upper()


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
    """normal_exp_tree = "".join(word.split())
    # print("normal_exp_tree: "+normal_exp_tree)
    exp_split = normal_exp_tree.split("(")
    print("exp_split: ")
    print(exp_split)
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
    return("".join(simplified))"""


    normal_exp_tree = "".join(word.split())
    exp_split = filter(None, re.split('(\W)', normal_exp_tree))
    print(exp_split)

    for i in exp_split:
        if (i == "(" and exp_split.index(i) == 0):
            print("(")
        else:

    simplified = []

    print("Simplified : ")
    print(simplified)

# twitter1("(AB) C((D E )F) /SR")
# s_simplify("(AB) C((D E )F) ") #ABC(DEF)
# twitter1(["(AB)C/", "(AB)C/S", "(AB)C/RS", "A(BC)/RS", "A(BC)/RSR"]) #[(AB)C, ABC, C(BA), CBA, ABC]
s_simplify("C(BA)") #C(BA)
s_simplify("(CB)A") #CBA
# s_simplify("(AB) C((D E )F)")


def buildParseTree(fpexp):
    fplist = fpexp.split()
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree
    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in ['+', '-', '*', '/', ')']:
            currentTree.setRootVal(int(i))
            parent = pStack.pop()
            currentTree = parent
        elif i in ['+', '-', '*', '/']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')':
            currentTree = pStack.pop()
        else:
            raise ValueError
    return eTree