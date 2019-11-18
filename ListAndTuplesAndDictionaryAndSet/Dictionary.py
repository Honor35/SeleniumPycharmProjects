my_dict = {
           "name" : "Kuruvila",
           "designation" : "Software Developer",
           "role" : "Developing",
           "industry" : "IT"
          }
print("*********************************************")

print("Dictionary values are = ",my_dict)

print("*********************************************")

print("The value of the key[Name] = ",my_dict["name"])  # -- give key value print the value of the key

print("*********************************************")

print(my_dict.get("name"))  # -- using get method

print("*********************************************")

print("Print Dictionary All values are : ",my_dict.values())  # -- print dictionary all values.

print("*********************************************")

print("Print all key Names : ")
for x in my_dict:
    print(x)   # -- print all key names.

print("*********************************************")

print("Print all values of dictionary :")
for x in my_dict:
    print(my_dict[x])  # -- print all values of dictionary

print("*********************************************")

print("Print all values in {key:values} format :")
for x,y in my_dict.items():  # -- items function use
    print(x ,":",y)

print("*********************************************")

my_dict["role"] = "Testing"
print(my_dict)

print("*********************************************")

my_dict["Language"] = "Python"
print(my_dict)

print("*********************************************")
my_dict.pop("role")
print(my_dict)

print("*********************************************")

my_dict.popitem() # -- remove the last element
print(my_dict)

print("*********************************************")

del my_dict["designation"]
print(my_dict)

print("*********************************************")

my_dict.clear()
print(my_dict)

print("*********************************************")

del my_dict

print("*********************************************")

print("Test Completed....")