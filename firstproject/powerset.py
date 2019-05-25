class Powerset:

    p = [[]]
    def __init__(self):
        pass

    def insert(self,arg):
        p_cp = self.p[:]
        for e in self.p:
            e_cp = e[:]
            e_cp.append(arg)
            p_cp.append(e_cp)
        self.p = p_cp[:]
        del e, e_cp, p_cp

####################################################################
def makePowerSet(regularset):
    global ps
    for i in regularset:
        ps.insert(i)
####################################################################
def main(s):
    makePowerSet(s)

    print('Powerset')
    print(ps.p)
    print('Expected length of powerset', 2**len(s))
    print('Actual length of powerset',len(ps.p))

ps = Powerset()
#main([1,2,3,4, 5, 6])