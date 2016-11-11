"""
omer.cansizoglu@snapchat.com
String: 1+2*3/3-4 evaluate it
"""
import re
s = "(12+1)+2*3/3-4"
num = []
symbols = []
temp = []
statement = []

"""This is to take care of double digit numbers"""
for i in range(len(s)):
    if s[i].isdigit():
        if i == len(s)-1:
            if statement[-1].isdigit():
                statement[-1] = str(statement[-1])+str(s[i])
                num[-1] = str(num[-1])+str(s[i])
            else:
                statement.append(s[i])
                num.append(s[i])
        temp.append(s[i])

    else:
        num.append("".join(temp))
        if(ord(s[i]) == 40 or ord(s[i]) == 41): #was having a lot of bugs, did not want the parentheses to be in the symbols stack
            # print(s[i], type(s[i]), ord(s[i]))
            pass
        else:
            symbols.append(s[i])

        statement.append("".join(temp))
        statement.append(s[i])
        temp = []

"""remove any arbitrary white spaces in the list"""
num = filter(None, num)
symbols = filter(None, symbols)
statement = filter(None, statement)
print(num, symbols)
print(statement)

output = 0
for i in range(len(statement)):
    temp = 0
    element = statement[i]
    if element == "(":
        i+=1
        if statement[i] == num[0]:
            temp=statement[i]
            num = num[1:]
        # elif statement[i] == symbols[0]:
