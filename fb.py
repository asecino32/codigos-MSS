def MSS(A):
    if not A:
        return 0
    sum1 = MSS(A[:-1])            # sin incluir A[n]
    sum2 = MSS(A[:-1]) + A[-1]    # incluyendo A[n]
    return max(sum1, sum2)


A=[5,2,-1,-7, 9,-2,4,5,2,-1]
print(MSS(A))
