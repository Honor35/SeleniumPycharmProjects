#Given Variables
a = 1
b = 1.2
c = 5j
d = "a"
e = "Python"
f = True
#************************************************************************

print(type(a))  # int
print(type(b))  # float
print(type(c))  # complex
print(type(d))  # String
print(type(e))  # String
print(type(f))  # boolean

#************************************************************************

#Casting the given variables
g = int(3)
h = int(5.8)
i = float(9)
j = str(100)

print(g)   # 3
print(h)   # 5
print(i)   # 9.0
print(j)   # "100"

#************************************************************************
z = "Python Program"
print(z[4])  # print index value of the string
print(z[2:8]) # start 2nd index and finish 7th index
print(len(z)) # length of the z.

#************************************************************************
y = "  Selenium Python   "
print(y.strip())    # strip is remove unwanted spaces

#************************************************************************
x = "Jeve"
print(x.replace("e","a"))   # replace the letters wherever the 'e' is present replace the value of 'a'

#************************************************************************
w = "Selenium,Python"
print(w.split(","))     # split operation

#************************************************************************
#inputs
print("Enter the Value :")
v = input()               # inputs functions
print("The Value is : " + v)

#************************************************************************