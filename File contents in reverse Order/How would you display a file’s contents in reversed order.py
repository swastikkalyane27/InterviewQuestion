# example 1:

f1 = open('sample1.txt', 'w')

with open('sample.txt', 'r') as data :
    data1 = data.read()

data2 = data1[::-1]
print(data2)
f1.write(data2)
f1.close()

# example 2 :

f2 = open('sample2.txt', 'w')

with open ('sample.txt', 'r') as myfile :
    data3= []
    data3.append(myfile.readline())
    data3.append(myfile.readline())
    print(data3)

for i in reversed(data3):
    f2.write(i)
    print()


f2.close()