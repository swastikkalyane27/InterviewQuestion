import json
# serialization
# employee = {'name': 'shubham',
#             'age': 26,
#             'salary': 1000,
#             'experience': True,
#             'eno': None
#            }
# json_string = json.dumps(employee,indent=4,separators=(".","="),sort_keys=False)
# print(type(json_string))
# print(json_string)
# with open("D:/practice_session_topics/emp.json","w") as f:
#     json.dump(employee,f,indent=4)



# import json

# print(json.dumps({"name": "John", "age": 30}))
# print(json.dumps(["apple", "bananas"]))
# print(json.dumps(("apple", "bananas")))
# print(json.dumps("hello"))
# print(json.dumps(42))
# print(json.dumps(31.76))
# print(json.dumps(True))
# print(json.dumps(False))
# print(json.dumps(None))





# de-serialization
# json_string = """{"name": "shubham",
#             "age": 26,
#             "salary": 1000.0,
#             "experience": true,
#             "eno": null
#            }"""
# emp_dict = json.loads(json_string)
# print(type(emp_dict))
# print("employee name:",emp_dict['name'])
# print("employee age:",emp_dict['age'])
# print("employee salary:",emp_dict['salary'])
# print("employee experience:",emp_dict['experience'])
# print("employee number:",emp_dict['eno'])
# for k,v in emp_dict.items():
#     print(k,":",v)


# with open("D:/practice_session_topics/emp.json","r") as f:
#     emp_dict = json.load(f)
#     for k,v in emp_dict.items():
#         print(k,":",v)


# import required packages
import json

# custom class
class Student:
	def __init__(self, roll_no, name, batch):
		self.roll_no = roll_no
		self.name = name
		self.batch = batch


class Car:
	def __init__(self, brand, name, batch):
		self.brand = brand
		self.name = name
		self.batch = batch


# main function
if __name__ == "__main__":
	
	# create two new student objects
	s1 = Student("85", "Swapnil", "IMT")
	s2 = Student("124", "Akash", "IMT")

	# create two new car objects
	c1 = Car("Honda", "city", "2005")
	c2 = Car("Honda", "Amaze", "2011")

	# convert to JSON format
	jsonstr1 = json.dumps(s1.__dict__)
	jsonstr2 = json.dumps(s2.__dict__)
	jsonstr3 = json.dumps(c1.__dict__)
	jsonstr4 = json.dumps(c2.__dict__)

	# print created JSON objects
	print(jsonstr1)
	print(jsonstr2)
	print(jsonstr3)
	print(jsonstr4)






## To get price of Bitcoin
# pip install request
# import requests
# response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
# print(type(response))
# bitcoin_info = response.json()
# print(type(bitcoin_info))
# print(bitcoin_info)
# print("Bitcoin price as on:",bitcoin_info["time"]["updated"])
# print("In USD:",bitcoin_info["bpi"]["USD"]["rate"])
