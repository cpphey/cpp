class AbhiStack:

    data = []

    def __init__(self):
        pass

    def push(self,arg):
        self.data.append(arg)

    def pop(self):
        #Len check
        if len(self.data) <= 0:
            return
        ret = self.data[len(self.data)-1]
        del self.data[len(self.data)-1]
        return ret

    def print(self):
        for i in self.data:
            print(i,end='')
        print('')

    def __sizeof__(self):
        return len(self.data)

    def size(self):
        return self.__sizeof__()
"""
def main():
    s = AbhiStack()
    #s.push(1);s.push(2);s.push(3);s.push(4);s.push(5);s.push(6);s.push(7);
    s.print()
    s.pop()
    s.print()
    print("\nMain done")
    pass

#main()
"""