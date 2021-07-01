import emp,pickle
f = open("D:/practice_session_topics/emp.dat","wb")
n = int(input("enter nos of employees:"))
for i in range(n):
    eno = int(input("enter employee no:"))
    ename = input("enter employee name:")
    esal = float(input("enter employee salary:"))
    eaddr = input("enter employee address:")
    e = emp.Employee(eno,ename,esal,eaddr)
    pickle.dump(e,f)
f.close()