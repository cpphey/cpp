#from stack import Stack

class AbhiQueue:

    data = []
    def __init__(self):
        pass

    def enqueue(self,arg):
        self.data.append(arg)

    def dequeue(self):
        if len(self.data) <= 0:
            return
        ret = self.data[0]
        del self.data[0]
        #self.data.remove(0)
        return ret

    def print(self):
        for d in self.data:
            print(d, end='')
        print('')

    def isPresent(self,arg):
        return arg in self.data

    def __sizeof__(self):
        return len(self.data)

    def size(self):
        return self.__sizeof__()

def main():
    pass
    #q = AbhiQueue()
    #q.enqueue(1)
    #q.enqueue(2)
    #q.enqueue(3)
    #q.print()

    #print( q.dequeue() )
    #q.dequeue()
    #q.print()

    #q.enqueue('apple')
    #q.enqueue(4)
    #q.print()

#main()