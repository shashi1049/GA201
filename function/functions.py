# first function

'''def channel_1():
    x = "Masai"
    print(x)


channel_1()
channel_1()
channel_1()
channel_1()'''

# This will print "Masai" 4 times as I have called the def 4 times.


# Add using the function
'''def superman():
    a = 10
    b = 15
    sum = a+b
    print(sum)


# Subtract using the function
def batman():
    x = 10
    y = 5
    difference = x-y
    print(difference)  # 5


superman()  # 25
batman()  # 5'''

# Multiplication using the function


'''def spiderman():
    x = 5
    y = 2
    mult = x*y
    print(mult)


# Division using the function
def ironman():
    x = 10
    y = 5
    div = x/y
    print(div)


spiderman()  # 10
ironman()  # 2'''

'''def superman(a,b):
	sum_val=a+b
	print(sum_val)


x=4;
y=5;
superman(x,y); # 9
A=5;
B=10
superman(A,B); # 15
'''

'''#Add using the function
def superman(a,b):
 sum=a+b;
 print(sum);


# Subtract using the function
def batman(x,y):
	difference=x-y;
	print(difference);


#Multiplication using the function
def spiderman(x,y):
	mult=x*y;
	print(mult);


#Division using the function
def ironman(x,y):
	div=x/y;
    print(div);


superman(10,15);  #25
batman(10,5);  # 5
spiderman(2,5);  # 10 
ironman(10,5); # 2'''

# Addition using a def and return statement

'''def superman(a,b):
	sum=a+b;
	return sum;


bucket=superman(10,15);
print(bucket); # 25'''


'''def superman(a,b):
	sum=a+b;
	return sum;


def batman(x):
	square=x*x;
	return square 


def aquaman(y):
	div=y/10;
	return div;


step1=superman(10,15); 

step2=batman(step1);

step3=aquaman(step2);

print(step3);  #62.5
'''
# check for prime
'''def check_prime(n):
  flag = False
  for i in range(2,n):
    if n%i==0:
      flag = True
      break
  if flag == True:
    print("not prime")
  else:
    print("prime")


x=check_prime(13)'''

# using the above check_prime() function I am checking the prime numbers
# in a given limit.

'''for i in range(lower_limit,upper_limit+1):
  x=check_prime(i);
  if(x==True):
    print(i,"is a Prime Number");
  else:
    print(i, "is Not a Prime Number");
'''

# to check char is lowercase


def is_lowercase(char):
    if len(char) == 1 and char.isalpha():
        return char.islower()
    else:
        return False


print(is_lowercase('a'))  # True
print(is_lowercase('Z'))  # False
print(is_lowercase('1'))  # False
print(is_lowercase(' '))  # False
