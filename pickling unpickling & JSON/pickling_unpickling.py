import pickle
# class Students:
#     def __init__(self,name,roll,city):
#         self.name = name
#         self.roll = roll
#         self.city = city
    
#     def disp(self):
#         print("name:",self.name,"roll:",self.roll,"city:",self.city)

# with open("class.dat","wb") as f:
#     stu1 = Students("shubham",101,"Thane\n")
#     stu2 = Students("pratik",102,"Mumbai")
#     pickle.dump(stu1,f)
#     pickle.dump(stu2,f)
#     print("Pickling done!!")

# with open("class.dat","rb") as f:
#     obj1 = pickle.load(f)
#     obj2 = pickle.load(f)
#     print("Unpickling done!!")
#     obj1.disp()
#     obj2.disp()



## using user input
# class Students:
#     def __init__(self,name,roll,city):
#         self.name = name
#         self.roll = roll
#         self.city = city
    
#     def disp(self):
#         print("name:",self.name,"roll:",self.roll,"city:",self.city)

# n = int(input("enter the numbers of students: "))
# with open("class.dat","wb") as f:
#     for i in range(n):
#         name = input("enter student name: ")
#         roll = int(input("enter student roll: "))
#         city = input("enter city name: ")
#         stu = Students(name,roll,city)
#         pickle.dump(stu,f)
# print("Pickling done!!")

# with open("class.dat","rb") as f:
#     while True:
#         try:
#             obj = pickle.load(f)
#             obj.disp()
#         except EOFError:
#             print("Done!!")
#             break
  


import pickle
class Employee:
    def __init__(self,eno,ename,esal,eaddr):
        self.eno = eno
        self.ename = ename
        self.esal = esal
        self.eaddr = eaddr
    def display(self):
        print(self.eno,"\t",self.ename,"\t",self.esal,"\t",self.eaddr)

with open("D:/practice_session_topics/emp.dat","wb") as f:
    #e = Employee(101,"shubham",10000,"badlapur")
    pickle.dump(Employee(101,"shubham",10000,"badlapur"),f)
    print("pickling done!")

with open("D:/practice_session_topics/emp.dat","rb") as f:
    obj = pickle.load(f)

    print("unpickling done!",obj)
    obj.display()
	





# Python program to illustrate
# pickle.dump()
# import pickle
# import io

# class SimpleObject(object):

# 	def __init__(self, name):
# 		self.name = name
# 		l = list(name)
# 		l.reverse()
# 		self.name_backwards = ''.join(l)
# 		return

# data = []
# data.append(SimpleObject('pickle'))
# data.append(SimpleObject('cPickle'))
# data.append(SimpleObject('last'))

# Simulate a file with StringIO
# out_s = io.StringIO()

# Write to the stream
# for o in data:
# 	print ('WRITING: %s (%s)' % (o.name, o.name_backwards))
# 	pickle.dump(o, out_s)
# 	out_s.flush()




# Python program to illustrate
#Picle.dumps()
# import pickle

# data = [ { 'a':'A', 'b':2, 'c':3.0 } ]
# data_string = pickle.dump(data)
# print ('PICKLE:', data_string )

# print(pickle.load(data_string))



# Python program to illustrate
# pickle.load()
# import pickle
# import io

# class SimpleObject(object):

# 	def __init__(self, name):
# 		self.name = name
# 		l = list(name)
# 		l.reverse()
# 		self.name_backwards = ''.join(l)
# 		return

# data = []
# data.append(SimpleObject('pickle'))
# data.append(SimpleObject('cPickle'))
# data.append(SimpleObject('last'))

# # Simulate a file with StringIO
# out_s = io.StringIO()


# Write to the stream
# for o in data:
# 	print ('WRITING: %s (%s)' % (o.name, o.name_backwards))
# 	pickle.dump(o, out_s)
# 	out_s.flush()
	
	
# # Set up a read-able stream
# in_s = io.StringIO(out_s.getvalue())

# # Read the data
# while True:
# 	try:
# 		o = pickle.load(in_s)
# 	except EOFError:
# 		break
# 	else:
# 		print ('READ: %s (%s)' % (o.name, o.name_backwards))



# Python program to illustrate
# pickle.loads()
# import pickle
import pprint

# data1 = [ { 'a':'A', 'b':2, 'c':3.0, 'd':True, 'f':None } ]
# print ('BEFORE:',)
# pprint.pprint(data1)

# data1_string = pickle.dumps(data1)
# pprint.pprint(data1_string)

# data2 = pickle.loads(data1_string)
# print ('AFTER:',)
# pprint.pprint(data2)

# print ('SAME?:', (data1 is data2))
# print ('EQUAL?:', (data1 == data2))

# data=[(1,{'a':'A','b':'B','c':'C','d':'D'}),(2,{'e':'E','f':'F','g':'G','h':'H','i':'I','j':'J','k':'K','l':'L'}),(3,['m','n']),(4,['o','p','q','r','s','t','u','v','w']),(5,['x','y','z']),]
# print(data)

# Python3 program to illustrate store
# efficiently using pickle module
# Module translates an in-memory Python object
# into a serialized byte stream—a string of
# bytes that can be written to any file-like object.

# import pickle

# def storeData():
# 	# initializing data to be stored in db
# 	Omkar = {'key' : 'Omkar', 'name' : 'Omkar Pathak',
# 	'age' : 21, 'pay' : 40000}
# 	Jagdish = {'key' : 'Jagdish', 'name' : 'Jagdish Pathak',
# 	'age' : 50, 'pay' : 50000}

# 	# database
# 	db = {}
# 	db['Omkar'] = Omkar
# 	db['Jagdish'] = Jagdish
	
# 	# Its important to use binary mode
# 	dbfile = open('examplePickle', 'ab')
	
# 	# source, destination
# 	pickle.dump(db, dbfile)					
# 	dbfile.close()

# def loadData():
# 	# for reading also binary mode is important
# 	dbfile = open('examplePickle', 'rb')	
# 	db = pickle.load(dbfile)
# 	for keys in db:
# 		print(keys, '=>', db[keys])
# 	dbfile.close()

# if __name__ == '__main__':
# 	storeData()
# 	loadData()





# import pickle

# class TextReader:
# 	"""Print and number lines in a text file."""

# 	def __init__(self, filename):
# 		self.filename = filename
# 		self.file = open(filename)
# 		self.lineno = 0

# 	def readline(self):
# 		self.lineno + 1
# 		line = self.file.readline()
# 		if not line:
# 			return None
# 		if line.endswith('\n'):
# 			line = line[:-1]
# 		return "%i: %s" % (self.lineno, line)

# 	def __getstate__(self):
# 		# Copy the object's state from self.__dict__ which contains
# 		# all our instance attributes. Always use the dict.copy()
# 		# method to avoid modifying the original state.
# 		state = self.__dict__.copy()
# 		# Remove the unpicklable entries.
# 		del state['file']
# 		return state

# 	def __setstate__(self, state):
# 		# Restore instance attributes (i.e., filename and lineno).
# 		self.__dict__.update(state)
# 		# Restore the previously opened file's state. To do so, we need to
# 		# reopen it and read from it until the line count is restored.
# 		file = open(self.filename)
# 		for _ in range(self.lineno):
# 			file.readline()
# 		# Finally, save the file.
# 		self.file = file

# reader = TextReader("Geeksforgeeks.txt")
# print(reader.readline())
# print(reader.readline())
# new_reader = pickle.loads(pickle.dumps(reader))
# print(new_reader.readline())
