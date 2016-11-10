arr = [['a', 'b', 'c', 'd', 'a'], [1,2,3,45,6]]

for element in arr:
    if 'a' in element:
        print(element.index('a'))
        print(arr[element.index('a')])