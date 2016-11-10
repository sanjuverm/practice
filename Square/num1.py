# Enter your code here. Read input from STDIN. Print output to STDOUT
"""
import sys

the_input = sys.stdin.read()
print((the_input)) #input is coming in as a type string
"""

# def LinMod(n):
#     split_input = n.split("\n")
#     #print(split_n)
#     #split_n is now an array
#     line1 = split_input[0] #n+1 elements
#     line1_split = line1.split(",")
#     print(line1_split)
#
#     # mylist = [1, 2, 3]
#     # ans = list(map(lambda x: x + 1, mylist))
#     # print(ans) #[2,3,4]
#
#     ans = []
#     num = 0
#
#     print("******")
#
#     for line in split_input[1:]:
#         for element in line:
#             print(element)

def LinMod(n):
    lines = n.split('\n')
    values = lines[0].split(",")
    n = len(values) - 1

    for i in range(1, len(lines)):
        nums = lines[i].split(",")
        result = float(values[0])
        for j in range(0, n):
            result += float(values[j + 1]) * float(nums[j])
        if result <= 0:
            print("not fraud")
        else:
            print("suspect fraud")



LinMod("0,0\n-1\n0\n1")
print("\n")
LinMod("1.0,1.5,-2.0\n2.0,1.0\n-2.0,1.0")
print("\n")
LinMod("1,1\n-1\n0\n1\n2")

# LinMod("1.0,1.5, -2.0\n2.0,1.0\n-2.0,1.0\n")

def check():
    for i in range(1,6):
        print(i)

check()