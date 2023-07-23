slice=[5,-7,3,5,-2,4,-1]
def slow_max_slice(A):
    n = len(A)
    result = 0
    for p in range(n):
        for q in range(p, n):
            sum = 0
            for i in range(p, q + 1):
                sum += A[i]
            result = max(result, sum)
    return result

def golden_max_slice(A):
    max_ending = max_slice = 0
    for a in A:
        max_ending = max(0, max_ending + a)
        max_slice = max(max_slice, max_ending)
    return max_slice

print (slow_max_slice(slice))
print (golden_max_slice(slice))