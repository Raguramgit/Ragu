#print("hello world")
"""print("Enter a number")
a = int(input())
print ("The value of a is =", a)
print("Enter a number")
b = input()
x= int(b)
print ("The value of b is =", b)
c = a + x
print("The value of c is =", c)"""
"""""
#    0  1     2    3     4      5       6       7   8    9   10  # Positive Index
a = [1,2.33,"hi",True,'alpha','beta','theta',33.44,666,100,12.33]
#                                                   -3  -2   -1  
print(a)            # prints whole List
print(a[7])         # access the positive Index
print(a[-2])        # access the negative Index
print(a[1:9])       # start index : end before index;   
print(a[3:-1])      # start index : end before index;   
print(a[4:])        # start index : till end of List;       
print(a[:9])        # from start of List: end before index
print(a[:])         # from start of List: till end of List
print(a[0:11:2])    # start index : end before index : jump
print(a[::3])       # from start of List: till end of List: jump
print(a[::-1])      # reversing a List using jump as -1
"""
"""
print([1,2,3] + [33,44,55])
print([1,2,3] * 3)
"""

"""
a = [1,22,3.4,True,'hello',3.4]
a.append(100)
print(a)
"""
"""
a = [1,22,3.4,True,'hello',3.4]
a.insert(0,22)    
print(a)
"""
"""
a = [22,1,22,3.4,True,'hello',3.4]
a.remove(22)    
print(a)
"""
"""
a = [1,22,3.4,True,'hello',3.4]
x = a.index(22) 
print(x)
"""
"""
a=100
b=500
x=a+b
if x>1000:
    print("A is grater that 10")
elif x==600:
    print("A is same as 600")
else:
    print("A is less than 10")
print("End of if condition")    
"""
