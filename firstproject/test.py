# you can write to stderr for debugging purposes, e.g.
# sys.stderr.write("this is a debug message\n")
import sys

def genLine(letter,size):
    line=''
    for i in range(size):
        line+=letter
    return line

def solution(N):
    # write your code in Python 3.6
    for row in range(N):
        if row < N-1:
            sys.stdout.write("L")
            sys.stdout.write("\n")
        else:
            sys.stdout.write(genLine("L",N))
            sys.stdout.write("\n")
    pass

#print(genLine("L",3))
solution(100)