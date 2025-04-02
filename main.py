print("hello world")
print("hello")

score = 0
full_name = "Felistus Gomba"
print(score)
print(full_name)
full_name = "FELISTUS GOMBA"
fullName = "Felistus"
age = 4
surname = "Gomba"
location = "Mufakose"
print(age)
print(location)
print(surname)

customerName = "Kelvin"

name_of_city = "Harare"
print(name_of_city)

customeName = "Kelvin"
print(customerName)

customerNameAndSurname ="Kelvin gomga"
print(customerNameAndSurname)
print(type(customerNameAndSurname))

name_of_organization = "uncommon"
print(name_of_organization)

print(type(surname))
print(type(score)) #this expression is printing the data type of the variable to see if its a string or booleans,interger
# print(type(city)) # this expression is printing the data type of the variable city

time = "10:30"
print(time)
print(type(time))

name_of_city = "mutare"
print(name_of_city)
print(type(name_of_city))

totalSpend = "30"
print(totalSpend)
print(type(totalSpend))

age = "6"
# integers
number_of_pupils = 40
print(number_of_pupils) #intergers
print(type(number_of_pupils))

# float numbers with qomma
name_of_pupils = 40.87
print(number_of_pupils)
print(type(number_of_pupils))

#bomdas of numbers
x= 15
y= 5
print(f"addition{x+y}")
print(f"subtration{x-y}")
print(f"multiplication{x*y}")
print(f"division{x//y}")

num = 5_000_000
print(num)

##string variables along with text
full_name = "Felistus"
print(f"hello {full_name}")
email_address = "felistusgomba@gmail.com"
print(f"your email is {email_address}")
work_place = "Uncommon"
print(f"my work place is {work_place}")

#integers variables along with text
num_of_students = 40
print(f"your class has {num_of_students} students")
age = "50"
print(f"your age is {age}")
quantity = "40"
print(f"your oranges are {quantity}")


# #floats are numbers in decimal format
# price = "10.20"
# print(f"the price of rice is ${price}")
# totalSpend = "29.30"
# print(f"the money spent on shoes is ${totalSpend}")


# #booleans contains True or False
# is_student = "True"
# print(f"are you a student?: {is_student}")
# for_sale = "False"
# print(f"is this item for sale?{for_sale}")

# is_online = "True"
# if is_online:
#     print("you are online")
# else:
#     print("you are offline")


# are_you_dating = "True"
# print(f"are you dating? {are_you_dating}")
# are_you_dating = "True"
# if are_you_dating:
#     print("yes we are dating")
# else:
#     print("we are not dating")


# #arithmetics
# #exponentials = is to the power of represmmted **
# #modulas they returnds the  remainder of any division presented by %
# #flow divion represented by // in which returns the number in a number ain a round figure
# boys = 3
# girls = 5
# print(f"addition {boys + girls}")
# print(f"subtration {boys - girls}")
# print(f"division {boys // girls}")
# print(f"multiplication {boys * girls}")
# print(f"exponential {boys ** girls}")
# print(f"modulos {boys % girls}")

# print(4 + 6)
# print(4 % 5) #returns the remainder
# print(4 * 5)
# print (3+5)


# Booleans it has 2 data type but it returns 1 data type either True or False
#they are used on condition or comparison to control the flow of a program 
is_student = True
print(f"{is_student}")
x = True
y = False
print(y)
#boolean comparison are used to check conditions
print(10 > 5)
print(7 <= 7)

#List is a colection of items in python
#a list is used to store multiple values in a single variable
# alist is identified by squre brackets
fruits = ["apple", "banana", "cherry"] 
numbers =[10, 9, 8, 7, 6,]
mixed_list = [True, 1,2 ,4, "sam", [1,2,3]]

print(fruits[0])
print(fruits[-1])



#indexing we use a positive and negative indexing(pick inside the lis) to index an elemnt inside a list
#first iteam is represented by 0 and second is reprented by 1 and -1 for the second from last
print(fruits[0])
print(fruits[-1])

#Slicing a list
#we use a mothod called potion using start and end eg 
numbers = [10,20,30,40,50,60]
print(numbers)
print(numbers[1:5])
print(numbers[:-1])
print(numbers[:3])
print(numbers[1:])
buckets = ["drink", "tea", "maheu", "bear"]
print(buckets)
print(buckets[0:2])
print(buckets[-4])



numbers[0] = 5
print(numbers)


#change element in a list thats modifying a numbers replace1 using index numbers of an element
# modify the first elemnt should be 5(5,10,20,30,40,50)
fruits = ["apple", "banana", "cherry", "orange"]
print(fruits)

fruits[1] = "matohwe"
print(fruits)

fruits[2] = "grape"
print(fruits)

#append (adding an elemnt iside a list to the end of the list) insert(giving a specific index ilist)
#fruits = ["apple", "banana", "cherry"]
#fruits.append ("avo")
#fruits.insert(1, "mango")
#print(fruits)
#print(fruits)

#Remove,delete,pop,clear
#removes a certain
#pop its like 
#delete the intere list
#clear empty the entere list it returns as an empty list
fruits = ["apple", "banana", "cherry"]
#fruits.remove("banana")
print(fruits)
del fruits[0]
print(fruits)
#Research on list functions and methods  to research

#Dictionary in Python is a coleection that stores key value to become a pair.It can be identified by curlly braces{} 
#key:value eg {"name": Felistus} key should be strings and value can be any data type
student = {
    "name" : "FG",
    "age" : 24,
    "grade" : 2
}
student["name"] = "SK"
#print(student["age"])
#print(student["name"])
#When we want to modify inside the dictionary to change name from FG to SK


 #whenever we want to access a value in a dictionary we target the Key print(dict{key}) print(student{"name"})
 #we want to acess a specific value


