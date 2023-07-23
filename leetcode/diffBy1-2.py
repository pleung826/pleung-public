def diffBy1(a, b):
    count=0
    if abs(len(a) - len(b)) > 1:
        return False

    s1=list(a)
    s2=list(b)

    i=0
    j=0
    print(s1)
    print(s2)
    while i < len(a):
        if s1[i] == s2[j]:
            i=i+1
            j=j+1
        else:
            count = count+1
            if len(s1) > len(s2):
                i=i+1
            elif len(s2) > len(s1):
                j=j+1
            else:
                i=i+1
                j=j+1

    print (count)
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