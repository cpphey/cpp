# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def distance(arg1,arg2):
    #assuming arg2 is bigger than arg1
    return arg2-arg1

def solution(A):
    # write your code in Python 3.6
    max=-100 #init
    sizeA = len(A)
    for i in range(0,sizeA):
        for j in range(i+1,sizeA):#I made a mistake -- I wrote "range(i,sizeA)". Correct is "range(i+1,sizeA)"
            sum = A[i]+A[j]+distance(i,j)
            if(max<sum):
                max=sum
    return max
    pass

#print(solution([1,3,-3]))

print(solution([-8,4,0,5,-3,6]))