# Enter your code here. Read input from STDIN. Print output to STDOUT
"""
PS: I don't know how to bowl... Not completely aware of all the edge cases but these are the ones accounted for:

1)
"""
import sys

n = sys.stdin.read()
#print((n))

n_split = n.split("\n")
strike_stack = []

num_balls_bowled = 0
is_first_roll = True
extra_rolls = 0
cur_score = 0

total_score = 0

for line in n_split[1:]:

    if is_first_roll:
        cur_score = 0
        num_balls_bowled += 1

    total_score += int(line)
    leng = len(strike_stack)
    for i in range(0, leng):
        # print("bonus")
        f = strike_stack[0]
        strike_stack = strike_stack[1:]
        total_score += int(line)
        if f - 1 > 0:
            strike_stack.append(f - 1)

    cur_score += int(line)

    if is_first_roll and int(line) == 10:
        strike_stack.append(2)
        is_first_roll = not is_first_roll
        if num_balls_bowled == 10:
            extra_rolls = 2
    elif (cur_score == 10):
        strike_stack.append(1)
        if num_balls_bowled == 10:
            extra_rolls = 1

    is_first_roll = not is_first_roll
    #print(total_score)
    if num_balls_bowled == 10:
        break

if extra_rolls > 0:
    for i in range(1, extra_rolls+1):
        total_score += int(n_split[-i])
        if len(strike_stack) > 0:
            total_score += int(n_split[-i])
            strike_stack = []
print(total_score)

