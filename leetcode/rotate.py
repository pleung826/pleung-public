
def rotate(A, n):
    part1=A[n:]
    part2=A[0:n]

    print(part1)
    print(part2)
    return part1 + part2

print(rotate([1,2,3,4,5], 2))