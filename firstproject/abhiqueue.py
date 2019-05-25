#from stack import Stack

class Queue:

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


def main():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.print()

    #print( q.dequeue() )
    q.dequeue()
    q.print()

    #q.enqueue('apple')
    q.enqueue(4)
    q.print()

main()