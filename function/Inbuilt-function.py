# first do the question without using the functions, then do the problem using
# the functions

'''def checkNumber(num):
    if num % 2 == 0:
        return "true"
    else:
        return "false"


x = checkNumber(7)
print(x)   # or i can write print(checkNumber(7))'''

# count even number

# step 1: I will declare a function to check the even number

'''
def checkNumber(num):
    if num % 2 == 0:
        return "true"
    else:
        return "false"


# step 2: I can a run a loop within the given range and use this function to do
# the job.
count = 0
for i in range(100):
    x = checkNumber(i)
    if (x == "true"):
        count = count+1


print(count)
'''

# count odd

# step 1: I will declare a function to check the even number


'''def checkNumber(num):
    if num % 2 == 0:
        return "true"
    else:
        return "false"

 # step 2: I can a run a loop within the given range and use this function to do
 # the job.
count = 0
for i in range(100):
    x = checkNumber(i)
    if (x == "false"):
        count = count+1


print(count)'''

# reverse a string


'''def reverseString(str):
    output = ""
    for i in range(len(str)-1, -1, -1):
        output = output+str[i]

    return output


new_str = reverseString("Hello")
print(new_str)
'''

# check pallindrome


'''def reverseString(str):
    output = ""
    for i in range(len(str)-1, -1, -1):
        output = output+str[i]

    return output


original_string = "masai"
reversed_output = reverseString("Hello")

# create another function to check palindrome


def palindrome(str1, str2):
    if str1 == str2:
        print("Yes it is a palindrome")
    else:
        print("Not a palindrome")
'''

# Write  a function to multiply the elements of two arrays

'''arr1=[20,40,60,80];
arr2=[3,7,9,4];

def multiply(a,b):
  final =[]
  for i in range(len(a)):
    product=a[i]*b[i]
    final.append(product)
  print(final)

print(multiply(arr1,arr2)) # [60,280,540,320]'''

# converting to number

'''x="12";
y="24";
print(x+y); # 1224

num1=int(x);
num2=float(y);
print(num1+num2); # 36'''

# convert to string

'''num1=12;
num2=36;
print(num1+num2); # 48

x=str(num1)
y=str(num2)
print(x+y);    # 1236
'''

# append()

'''a = ["apple", "banana", "cherry"]
b = ["Ford", "BMW", "Volvo"]
a.append(b)

print(a)  # appends an element to the end of the list.'''

# pop()
'''list_1=[1,2,3,4];
x=list_1.pop();
print(x);'''

# last index

'''str1 = "this is string example....wow!!!"
str2 = "i"

print(str1.rindex(str2))   # 11
'''
# first index
'''str1 = "this is string example....wow!!!"
str2 = "i"

print(str1.index(str2))    # 2
'''
# insert()

'''fruits = ['apple', 'banana', 'cherry']

fruits.insert(1, "orange")'''


# join()

'''list = ["chunnu", "munnu", "tunnu"]
x = "".join(list)

print(x)  # chunnumunnutunnu
'''
# slice()

a = ["a", "b", "c", "d", "e", "f", "g", "h"]
x = slice(2)
print(a[x])  # ['a', 'b', 'c','d', 'e']
