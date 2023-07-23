
def diffBy1(a, b):
    if abs(len(a) - len(b)) > 1:
        return False

    # get longer string
    if (len(a)> len(b)):
        s1=list(a)
        s2=list(b)
    else:
        s1=list(b)
        s2=list(a)

    print(s1)
    print(s2)
    count=0
    j=0
    i=0
    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            count = count+1
            if len(s1) == len(s2):
                i=i+1
                j=j+1
            else:
                i=i+1
        else:
            i=i+1
            j=j+1

    if count > 1:
        return False
    else:
        return True

print(diffBy1("ple", "pale"))
print(diffBy1("pale", "ple"))
print(diffBy1("pale", "pile"))
print(diffBy1("ban", "bye"))
print(diffBy1("123", "1234"))
print(diffBy1("pale", "bale"))