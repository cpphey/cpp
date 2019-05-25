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
s=[1,2,3,4, 5, 6]
ps = Powerset()
for i in s:
    ps.insert(i)

print('Powerset')
print(ps.p)
print('Expected length of powerset', 2**len(s))
print('Actual length of powerset',len(ps.p))