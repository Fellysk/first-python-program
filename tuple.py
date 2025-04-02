##Tuple and Sets
#a tuple is a collection of elements that are immutable(they cannont be changed after creation)
#Tuple are defined by(1,2,3,4)
#you cant add, remove   or change elements i


#my_tuple =(1, 2,3,4,5,6,7,8)
#print(my_tuple)
#print(type(my_tuple))
#Accessing tuple elements using index
#this_tuple = ("banana", "apple", "cherry")
#print(this_tuple)
#how many elements the tuple have
#print(len(this_tuple))
#acessing element
#print(this_tuple [0])
#print(this_tuple[2])

student = ('natasha', 'tinaye', 'ruth', 'Takudzwa')
print(student)
print(student[1])
print(student[1:-2])
#[start:step:end]
        

students = ('mary', 'ruth', 'Nalia', 'methew', 'diana', 'kelcee', 'Loveness')
print(students[::2])


tuple2 = (1,)
tup1=  (1,2,3,4,5,6)
tup3 = (2,4,6,8,)
print(tup1)
print(tup3)
print(tup1 + tup3)
print(tup3 * 2)
print(tuple2)

tuple4 = (3,5,7,9)
print(len(tuple4))

#to convert a list to a tuple
my_list = list(tuple4)
print(my_list)

#to add into a list 
list2 = [1,2,3,4,5]
my_list.extend(list2)
print(my_list)
my_list=tuple(my_list)
print(my_list)


tuple3 = ('Faith', 'Tanaka', 'Ruth', 'Martha')
print(tuple3)

her_list = list(tuple3)
print(her_list)
#add into a list
list3 = ["henry", 'Herbet', 'Dilany']
her_list.extend(list3)
print(her_list)

her_list.sort(reverse=True)
print(her_list)


#return a list to a tuple
her_list = tuple(her_list)
print(her_list)



#sorting
tuple5 =(10,20,30,40,50,60,70,80,90,100)
mylist1 = list(tuple5)
print(mylist1)
mylist1.sort(reverse="True")
print(mylist1)

name= ('Kuda', 'Ryan', 'Mia')
my_name= list(name)
print(my_name)

#adding new list into an tuple that have been changed to a list
newnames= ["jame",'amanda','Sydney']
my_name.extend(newnames)
print(my_name)

#sort the list
my_name.sort()
print(my_name)
#descernding order
my_name.sort(reverse=True)
print(my_name)

#change back to tuple
my_name = tuple(my_name)
print(my_name)






#LOGICAL OPERATORS
# a = 23
# b = 24
# c = 2
# print(a > b and b == c)


# correct_username = ("admin")
# correct_password = 1234

# username = input("Enter username:")
# password = int(input("enetr password:"))

# if username == correct_password and correct_password == 1234:
#     print(f"welcome{username} you are logged in")
# else:
#     print("invalid credentials")


# temp = 0
# condition = "sunny"

# temp = int(input("enter the degrees"))
# condition = input("sunny")
# if temp >= 30 and condition == "sunny":
#     print(f" the {temp} degrees it is sunny")
# else:
#     print("it is cold")

# day = input("enter day:").lower()
# if day ==  "monday":
#     print("wear uniform")
# elif day == "tuesday":
#     print("wear garments")
# elif day == "wednesady":
#     print("wear casual")
# elif day == "thursday":
#     print ("wear formal")
# else:
#     print(f"{day} is not a day")



# day = "MONDAY"
# print(day.lower())

# score=int(input("enter score:"))

# if score >= 90 and score<= 100:
#     print(f"grade A")
# elif score >=80 and score <90:
#     print(f"grade B")
# elif score >= 70 and score <89:
#     print("grade C")
# elif score>=60 and score <79:
#     print("grade D")
# elif score<   





