# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    sizeA = len(A)
    identical_pairs = 0
    for i in range(0,sizeA):
        for j in range(i+1,sizeA):
            if A[i]==A[j]:
                identical_pairs+=1

    # TODO:cap a number at 1MM
    ret=0
    limit = 1000000000
    if identical_pairs <= limit:
        ret = identical_pairs
    else:
        ret = limit
    #print(ret)
    return ret
    pass


#solution([3,5,6,3,3,5])

"""
Example test:    [3, 5, 6, 3, 3, 5] 
OK 

Your code is syntactically correct and works properly on the example test.
Note that the example tests are not part of your score. On submission at least 8 test cases not shown here will assess your solution.
"""