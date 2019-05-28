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
        for j in range(i,sizeA):#no going from i is right because problem said a node to itself will have distance 0; see below
            sum = A[i]+A[j]+distance(i,j)
            if(max<sum):
                max=sum
    return max
    pass

#print(solution([1,3,-3]))

print(solution([-8,4,0,5,-3,6]))

"""
inner Loop
no going from i is right because problem said a node to itself will have distance 0; see below
it gave an example
where it went from 0 to 0. element 0 was 3
A[0]+A[0]-(0-0)
3   + 3  -(0-0)
Answer is 6 and this is the best answer. I remember from the webpage
"""