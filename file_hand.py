# how would you display a files contents in reversed order?
with open("D:/practice_session_topics/grp_b.txt","w+") as f:
    print(f.tell())
    f.write("shubham\tswastik\takshay\tshubham\tsushant\tpratik")
    print(f.tell())
    f.seek(0)
    print(f.tell())
    data = f.read()
    
    # using slicing
    # result = data.split("\t")
    # print(*result[::-1])
    
    #using for loop 
    # str2 = ""
    # for i in result:
    #     str2 = i + " " + str2
    # print(str2)
    
    #using reversed 
    # reverse_data = reversed(data.split("\t"))
    # str1 = " ".join(reverse_data)
    # print(str1)




