import emp,pickle
f = open("D:/practice_session_topics/emp.dat","rb")
print("printing employees info......")
while True:
    # obj1 = pickle.load(f)
    # obj2 = pickle.load(f)
    # obj3 = pickle.load(f)
    # obj4 = pickle.load(f)
    try:
        obj = pickle.load(f)
        # obj.display()
        if obj.eno == 100:
            obj.display()
            break
    except EOFError:
        print("unpickling done!..")
        break
f.close()

