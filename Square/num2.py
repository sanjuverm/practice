"""20
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0"""

def Bowling(n):
    n_split = n.split("\n")
    strike_stack = []

    num_balls_bowled = 0
    # print(num_balls_bowled)
    is_first_roll = True
    extra_rolls = 0
    #is_second_roll = False
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
        print(num_balls_bowled)
        if num_balls_bowled == 10:
            break

    if extra_rolls > 0:
        for i in range(1, extra_rolls+1):
            total_score += int(n_split[-i])
            print(len(strike_stack))
            if len(strike_stack) > 0:
                f = strike_stack[0]
                strike_stack = strike_stack[1:]
                total_score += int(n_split[-i])
                if f - 1 > 0:
                    strike_stack.append(f - 1)
    print(total_score)


    #
    #
    #
    #         if (is_first_roll):
    #             if (line < 10):
    #                 cur_score += int(line)
    #                 is_second_roll = True
    #                 is_first_roll = False
    #             elif (line == 10):
    #                 # this is a strike
    #                 cur_score += 10
    #                 strike_stack.append(1)
    #                 is_first_roll = True
    #                 is_second_roll = False
    #         elif (is_second_roll):
    #             if (line < 10 and cur_score + int(line) < 10):
    #                 cur_score += int(line)
    #                 is_first_roll = True
    #                 is_second_roll = False
    #             elif (line < 10 and cur_score + int(line) == 10):
    #                 # this is a spare
    #                 cur_score += int(line)
    #                 is_first_roll = True
    #                 is_second_roll = False
    #     #else:
    #
    #
    #     num_balls_bowled -= 1
    #
    # if(num_balls_bowled == 0):
    #     print(cur_score)


# Bowling("20\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0")
Bowling("12\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10")