
def countZero(s):
    count=0
    for c in s:
        print(c)
        if c == "0":
            count = count +1

    return count

print(countZero("10000111"))