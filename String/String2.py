# print char of string based on index
'''name = "Masai"
print(name)

print(name[0])   # M
print(name[1])   # a
print(name[2])   # s
print(name[3])   # a
print(name[4])   # i'''
# print(name[5])   # IndexError: string index out of range

# length of String

'''name = "Jantar Mantar"
print(len(name))'''    # 13

# check for valid password length should be 6 or more

'''password = "naved@8755"
if (len(password) < 6):
    print("Invalid : Your Password must be atleast 6 characters long")
else:
    print("Valid Password")'''


# loop

'''name = "Masai School"
for i in range(0, len(name)):
    print(name[i])'''


# String vs List

'''name1 = "Masai"
print(name1)
print(name1[0])

name2 = ["M", "a", "s", "a", "i"]
print(name2)
print(name2[0])'''

# upper()

'''s = "change happens in a moment"
print(s.upper())    # CHANGE HAPPENS IN A MOMENT'''

# title()

'''s = "change happens in a moment"
print(s.title())    # Change Happens In A Moment'''

# capitalize()

'''s = "change happens in a moment"
print(s.capitalize())    # Change happens in a moment'''

# isupper()

'''s = "change happens in a moment"
print(s.isupper())    # False
c = "KITE"
print(c.isupper())    # True

'''

# islower()

'''s = "change happens in a moment"
print(s.islower())    # True
c = "KITE"
print(c.islower())    # False
'''

# isnumeric()

'''s = "change happens in a moment"
print(s.isnumeric())    # False
c = "12345"
print(c.isnumeric())    # True
d = "12383a"
print(d.isnumeric())    # False
e = "12312 4"
print(e.isnumeric())    # False  (space( ) is special character not the numeric)
'''

# isalpha()

'''s = "change happens in a moment"
print(s.isalpha())    # False (space( ) is special character not the alphabet)
c = "12345"
print(c.isalpha())    # False
d = "abc12"
print(d.isalpha())    # False
e = "kind"
print(e.isalpha())    # True
'''

#string to list
#delimiter ⇒ space(” “), hyphen (-), comma(,), special characters(#, @, $ etc. )
#split()
'''s="change happens in a moment"
print(s.split(" "))  # ['change', 'happens', 'in', 'a', 'moment']'''

#list to string

'''lista=["Sam", "is", "an", "honest", "person"]
print(" ".join(lista))  # Sam is an honest person
print("-".join(lista))  # Sam-is-an-honest-person
print("#".join(lista))  # Sam#is#an#honest#person
print("_".join(lista))  # Sam_is_an_honest_person
print("/".join(lista))  # Sam/is/an/honest/person'''

#String to list of character

'''s="Nobleman"
print(list(s))   # ['N', 'o', 'b', 'l', 'e', 'm', 'a', 'n']'''

#Update String using List and third variable. [First Method]


'''name = "Masai";
name2 = []

for i in range(0, len(name)):
	name2.append(name[i]);


name2[0] = "N";
bag=""
for i in range(0, len(name2)):
	bag = bag + name2[i];

print(bag)
'''

#Update String using List and third variable. [Second Method]

'''name = "Masai"
output = ""
for i in range(0,len(name)):
 if i==0:
		output = output + "N";
 else:
		output = output + name[i];
	


print(output)
'''

#removing char from string

'''name = "Masai"
output = ""

for i in range(0, len(name)):

	if(name[i] != "s"):
		output = output + name[i];
    
print(output)
'''

#count the name starting with n/N

'''names = ["Nobita", "Naruto", "Shinchan","PowerRangers","Aladin","Noddy"]
count=0

for i in range(0,len(names)):
    name = names[i];
    if(name[0]=="N" or name[0]=="n"):
	    count += 1;
    
print(count)
'''
# Count the names which contain A in them.

'''names= ["Nobita", "Naruto", "Noddy", "Shinchan", "Oswald"];
count=0
for i in range(0,len(names)):
	name = names[i]
    for j in range(0,len(name)):
	    if(name[j]=='a' or name[j]=='A'):
		    count+= 1;
		    break;
print(count)
'''

