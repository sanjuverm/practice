"""Given a 4.x4 grit of letters, find the existence of a word.

Find "CATCH", return true on success.

x C A T
x x T C
x x C x
x x H x"""

word = "CATCH"
grid = [
    ["x", "C", "A", "T"],
    ["x", "x", "T", "C"],
    ["x", "x", "C", "x"],
    ["x", "x", "H", "x"]
]
d = {} #key is letter, value is count
for letter in word:
    if d.get(letter):
        d.update({letter:d.get(letter)+1})
    else:
        d.update({letter: 1})

# print(d)

for row in range(len(grid)):
    for element in range(len(grid[row])):
        i = grid[row][element]
        if d.get(i):
            d.update({letter: d.get(letter) - 1})

if(sum(d.values()) <= 0):
    print("True")
else:
    print("False")