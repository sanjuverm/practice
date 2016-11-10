def print0(width):
    for line in range(width):
        if line == 0 or line == width-1:
            print("*"*width)
        else:
            print("*"+str(" "*int(width-2))+"*")


print0(5)