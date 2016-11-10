"""Question 2"""
import re
n = "breakfast beach citycenter location metro view staff price\n5\n1\nThis hotel has a nice view of the citycenter. The location is perfect.\n2\nThe breakfast is ok. Regarding location, it is quite far from citycenter but price is cheap so it is worth.\n1\nLocation is excellent, 5 minutes from citycenter. There is also a metro station very close to the hotel.\n1\nThey said I couldn't take my dog and there were other guests with dogs! That is not fair.\n2\nVery friendly staff and good cost-benefit ratio. Location is a bit far from citycenter."
the_input = n.split("\n")
# print(the_input)
key_words = set(the_input[0].split(" "))
num_reviews = the_input[1]
etc = the_input[2:] #even elements are hotel ID, odd elements are review
hotel_count = {} #key is the hotel id, value is the review count

# print(key_words)
for i in range(0, len(etc), 2):
    hotel_id = etc[i]
    c = 0
    if(i%2 == 0):
        review = re.sub(r'[^\w\s]', '', etc[i+1]).lower().split(" ")
        for word in review:
            if word in key_words:
                c+=1
        if(hotel_id in hotel_count):
            # print("in count")
            hotel_count.update({hotel_id: int(hotel_count.get(hotel_id))+c})
        else:
            # print("not in count")
            hotel_count.update({hotel_id: c})

print("Question 2:")
print(sorted(hotel_count.keys(), reverse=True))


""" Question 3:"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

"""import sys
n = sys.stdin.read()"""
n = "25626 25757 24367 24267 16 100 2 7277"
the_input = n.split(" ")
target =(the_input[0])
nums = the_input[1:]

final = []
final.append(target)

for i in nums:
    diff = int(i) - int(target)
    if (diff > 127 or diff < -127):
        final.append(str(-128))
    final.append(str(diff))
    target = i
final = " ".join(final)

print("\nQuestion 3:")
print(final)




"""Question 4:"""

the_input = [66,
10,
18,
11,
21,
28,
31,
38,
40,
55,
60,
62]


target = the_input[0]
len_array = the_input[1]
nums = the_input[2:]
diff_dict = {}
val = 0

for i in nums:
    diff_dict.update({i: (target - i)}) #{18: 48, 21: 45, 38: 28, 55: 11, 40: 26, 60: 6, 11: 55, 28: 38, 62: 4, 31: 35}


for i in nums:
    value = diff_dict.get(i)
    if(value in diff_dict.keys()):
        val = 1
        break

print("\nQuestion 4:")
print(val)


