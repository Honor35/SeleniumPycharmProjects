my_list = ["India","America","canada","australia"]
print("Print all values in MyList :")
print(my_list)   # -- print all list values

print("*********************************************")

print("Print the third value in MyList :")
print(my_list[2]) # -- print index position value

print("*********************************************")
#Change index position value
print("Change index position value then Print the first value in MyList :")
my_list[0] = "London"  # --change index value
print(my_list)

print("*********************************************")

print("Print the traversing element one by one in MyList :")
for i in my_list:    # -- traversing element one by one
    print(i)

print("*********************************************")

print("Print the length of MyList :")
print(len(my_list))   # -- length of the list

print("*********************************************")

print("Insert the new element into the list then Print the values of MyList :")
my_list.append("india")  # -- append use to insert the new element into the list
print(my_list)

print("*********************************************")

print("Insert the value in the specific index position then Print the inserted value in MyList :")
my_list.insert(3,"new york")  # -- insert the value in the specific index position
print(my_list)

print("*********************************************")

print("Remove the particular index value then Print the values of MyList :")
my_list.remove("india")   # -- remove the particular index value
print(my_list)

print("*********************************************")

print("hide the index value(default hide index value is last element) then Print the values of MyList :")
my_list.pop(3)     # -- hide the index value(default hide index value is last element)
print(my_list)

print("*********************************************")

print("Delete the index value then Print the values of MyList :")
del my_list[0]   # -- delete the index value
print(my_list)

print("*********************************************")

print("Clear the list of all index values then Print the values of MyList :")
my_list.clear()  # -- clear the list all index values
print(my_list)

print("*********************************************")

state = ["Andhra","karnadaka","india","telungana","kerala"]
print(state)

print("*********************************************")

state.reverse()
print(state)

print("*********************************************")

my_list_1 = ["Letters",1,3.94,True,'x']   #  -- store all type of elements
print(my_list_1)

print("*********************************************")

my_list_2 = ["hi",[1,2,3],['a','b','c']]   # -- nested list
print(my_list_2)

print("*********************************************")

print(my_list_2[1])  # -- print nested list index value

print("*********************************************")

print(my_list_2[1][2])  # -- print inner list value specify index position

print("*********************************************")

print("Test Completed....")