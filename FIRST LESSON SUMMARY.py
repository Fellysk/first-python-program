##SUMMARY OF WEEK 1 
#Variable

print("Hello Felly")
name = "Felistus"

print(name)
full_name = "Felistus Gomba"
print(full_name)

age = 25
print(age)

location = " 1 Horwe"
print(location)
fruits = ["banana", "matohwe","apple", "guava"]
print(fruits)

rice = "20"

if rice == 20 :
    print(f" you purchased {rice}") 
else:
    print("you have insufficient funds")











x= 4
if x > 10:

    print(f"{x} is greater than 10")
else:
    print(f"{x}is less"   )


time= 10.30
if time < 12:
    print(f" you came early")
else:
    print(f"you are late")
    

rice = 5
if rice == 5:
    print(f" you purchased rice")
else:
    print(f"you havent purchased")    




totalSpend = 20.30
print(type(totalSpend))
if rice == 5: 
    print(f"you have pruchases rice")


    
 


#How to see the type of data type used
name_of_city = "Harare"
print(type(name_of_city))

drink = 20
mango = 4
print(f"{drink+mango}")
print(type(drink))

number_of_student = 30
print(f" your class has {number_of_student} student")
print(type(number_of_student))
## DATA TYPES
#Strings represented by ""
#integer represented by whole numbers
#floats represented by numbers with commas 
#boolean they are conditional statements that returns True or False they are represented by curly braces
#list a list is used to store multiple values in a single variable and seen by squre bracket eg fruits =["banana", "apple", "paar"]
#dictionary they store key and a value in which they are seen by curly braces. The key is the is represnted in the form of a string whulst a value is any type of a data type


#FLOATS 
#Addition of floats
x = 10.40
y= 20.40
print(10.40 + 20.40)

total_spend = 5.30
print(f"the money for shoes is ${totalSpend}")

burger = 10.40
nuggets = 16.30
print(f"our prices for nuggets is ${nuggets} and for burger is {burger}")


##BOOLEANS
x = 2
if x == 4:
    print(f" {x} is greater")
else:
    print(f"{x} is lesser")


drink = 20
food = 10
if drink < 19:
    print(f"you have purchased your drink and your change i 1")   
else: 
    print(f"you have insufficinet funds") 

shoes = 5
if shoes == 3:
    print( f"you have purchased")
else:
    print(f"none")

chips = 3
fanta = 4
money_availalble = 10
if money_availalble > chips + fanta:
    print(f"you have purchased both")
else:
    print(f"you have inssufficient funds")


user_name = "Kevy"    
password = "makeup"

if user_name == user_name and password == password:
    print(f"welcome Kevy")
else:
    print(f"invalid password")


student = "Kesly"
ID_number = " 123"
if student == student and ID_number == ID_number:
    print(f"welcome {student}")
else:
    print(f"invalid ID number")


#List
fruits = ["guava", "apple", "peach", "banana"]  
print(fruits)
print(type(fruits))
 ##change element in a list we use indexing methos
fruits = ["guava", "apple", "peach", "banana"] 
fruits[2] = "hacha"
print(fruits)

fruits[1] = "pear"
print(fruits)

#APPEND ( Adding an item in a list)
fruits.append ("mango")
print(fruits)


community = ['Takudzwa', 'Faith', 'Maria', 'Jayden']
print(community)

#replacing
community[2] = 'Tafara'
print(community)


community[-2] = 'Marcia'
print(community)

community.append ("Farai")
print(community)

community.remove ('Takudzwa')
print(community)

#Slicing a list
#using indexing method of the positive and negative indexing of the start and the end potion

my_list = ["Takunda", "Tafadzwa", "Peace", "Loveness"]
print(my_list)
my_list[2]
print(my_list)
my_list[:3]
print(my_list)
my_list[1: 2]

#dictionary
#It store Key Value to ecome a pair it reprenetd by currly braces
#key should be a string "name" and value can be of any dat type
#a key and value and put side by side by a colony
students_register ={
    "name" : 'Sheila',
    "age" : 13,
    "location" : 'harare',
    'Class' : 'red',
    'School' : "Tendai"

    }
print(students_register)
students_register ["name"] = 'Tafara' 
print(students_register)

#DICTIONARY
student = {
    "name": "felly",
    "age": 23
}


student["age"] = 29
print(student)
student["name"] = "Faith"
print(student)
#add elements in a dictionary
student.update ({ "country": "zImbzbwe", "city" : "harare"})
print(student)
student.update({"phonenumber" : "0774226870", "address": "1 Horwe Close"})
print(student)

del student["phonenumber"]
print(student)
