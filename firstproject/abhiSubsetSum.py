
#geek for geeks
#https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/

####################################################
####################################################
####################################################
#    MY SOLUTION IS USING DYNAMIC PROGRAMMING
####################################################
####################################################
####################################################


A=[-2, -3, 4, -1, -2, 1, 5, -3]
####################################################
def makeIndex(i,j):
    return '{0}_{1}'.format(i,j)
hash = {}
#sum INCLUSIVE of I and J
def subsetSum(i,j):
    global A
    global hash

    #Return single index
    if i == j:
        return A[i]

    keyH = makeIndex(i,j)

    if keyH in hash:
        return hash[keyH]

    tempSum=0
    for ii in range(i,j+1):
        tempSum+=A[ii]
    hash[keyH] = tempSum
    return hash[keyH]

####################################################
#ass=subsetSum(2,4) works
print('Array is',A)
n = len(A)
print('Array Length is ',n)

numberOfSubsets = n - 1
numberOfLenghtsPossible = n - 1
print('numberOfLenghtsPossible ',numberOfLenghtsPossible)

allLenghtPossible=[i+1 for i in range(numberOfLenghtsPossible)]
print('numberOfLenghtsPossible ',allLenghtPossible)

for currentLength in allLenghtPossible:
    print('---------Current Length  ',currentLength,'------------')
    for start in range(0,n-currentLength,1):#start goes from 0 to n-1
        #calculating INCLUSIVE start to finish
        finish = start+currentLength
        print(start,"   ",finish)
        hash[makeIndex(start,finish)] = subsetSum(start,finish-1)+A[finish]


#TODO go through hash and find the max sum
hash_reverse={}
subsetSumList=[]
for k in hash:
    hash_reverse[hash[k]]=k
    subsetSumList.append(hash[k])

maxSum=max(subsetSumList)
print('------ANSWER---------')
print('Max sum is',maxSum)
print('Start / end index of max sum is',hash_reverse[maxSum])
