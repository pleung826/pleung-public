
def jump(x, y, d):
    count=0
    sum=x
    while sum < y:
        count = count+1
        sum = sum+ d
        if sum > y:
            break

    return count

print(jump(10,85,30))
