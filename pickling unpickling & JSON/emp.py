class Employee:
    def __init__(self,eno,ename,esal,eaddr):
        self.eno = eno
        self.ename = ename
        self.esal = esal
        self.eaddr = eaddr
    def display(self):
        print("emp no:{}, emp name:{}, emp sal:{}, emp addr:{}".format(self.eno,self.ename,self.esal,self.eaddr))