def readfile(filename):
    f = open(filename, 'r')  # we opened the file 'filename' for reading
    content = f.read()  # read file content in string
    lines = content.split('\n')  # spli content and create list of strings
    print(len(lines))
    for line in lines:
        print(line)
        newdict = []
    return lines

print(readfile("cwur_data_utf8.csv"))