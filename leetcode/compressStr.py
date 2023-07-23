def compressStr(A):
    if len(A) == 0:
        return ""

    str=""
    count=1
    prev=A[0]
    current=A[0]

    for current in A[1:]:
        if current != prev:
            str = str + prev + f"{count}"
            count=1
            prev=current
        else:
            count = count + 1

    str = str + current + f"{count}"

    return str

print(compressStr(""))
print(compressStr("a"))
print(compressStr("aa"))
print(compressStr("aab"))
print(compressStr("aabccccaaa"))