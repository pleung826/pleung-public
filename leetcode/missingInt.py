
def findMissingInt(list):
    missing=0
    current=list[0]
    prev=list[0]
    for i in range(1, len(list)):
        current=list[i]
        if current-prev > 1 or current-prev < 1:
            missing=prev+1
            break

        prev=list[i]

    return missing


print("missing int=", findMissingInt([2,3,1,5]))
print("missing int=", findMissingInt([2, 4, 5]))
print("missing int=", findMissingInt([2,3,4,6,1]))
