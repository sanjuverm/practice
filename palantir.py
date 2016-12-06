"""
Check if the String for a chemical reaction is balanced and return true if so

2 H2 + O2 -> 2 H2O
true

NaCl + AgNO3 -> NaNO3 + Ag
false
"""
import re
def break_string(s):
    s_split = s.split(" -> ")
    left_side = make_dictionary(s_split[0])
    right_side = make_dictionary(s_split[1])

    print(left_side, right_side)


def make_dictionary(l): #taking in a list, returning dictionary key = element, value = count
    l_split = filter(None, map(lambda each: each.strip("+"), l.split(" ")))
    print(l_split)
    d = {}
    multiplier = 0
    count = 0

    for i in range(len(l_split)):
        current = l_split[i]

        if current.isdigit():
            multiplier = current
        else:
            if i == 0 or not l_split[i-1].isdigit():
                multiplier = 1

            if multiplier == 1: #current is an element
                #split by uppercase and lowercase
                if(len(current) > 2): #multiple elements that need to be split and added to the dictionary count
                    elements = re.findall('[A-Z][^A-Z]*', current)
                    print(elements, "~~~~~")
                    for j in range(len(elements)):
                        element_breakdown = filter(None, re.split('(\d+)', elements[j]))




                print(current, "***")
            else: #current is an element
                element_breakdown = filter(None, re.split('(\d+)', current)) #[H, 2]
                print("element breakdown", element_breakdown)

        print("mult: ", multiplier, "current", current)



    return l_split
def main():
    break_string('2 H2 + O2 -> 2 H2O')
    print("\n*******\n")
    break_string('NaCl + AgNO3 -> NaNO3 + Ag')


main()