# ## DATA TYPES

# #Strings
# my_name = " 1. Felistus"
# print(my_name)

# location = " 2.  1 Horwe close mufakose"
# print(location)

# favorite_food = " 3.  lasgana made by Kelvin"
# print(favorite_food)

# religion = " 4  l full time Christian, i believe in Jesus Christ who died for us for our sins"
# print(religion)

# carrer_path = " 5.  I wish to be a full time lecturer"
# print(carrer_path)

# dream = "6   to travel the world with my family"
# print(dream)

# current_situation = '7.   l am a student at Uncommon.org'
# print(current_situation)

# dreams = "8.   I wish to be very healthy, 2. go to work. 3. married to Kelvin  4. live a peacefull life 5. provide for my parents"
# print(dreams)

# values = '9.   Trust in God, 2. Faithfull, 3. loyalty,   4. Love,  5. Peace, 6. Respect,  7. Submission'
# print(values)

# his_name = 'Kelvin SK'
# print(his_name)



# #integers




# num = 1,2,3,4,5,6,7,8,9
# print(num)

# id_num = 63217093727
# print(id_num)


# income = 1900
# print(income)


# markup = 150
# print(markup)

# address = 12345
# print(address)

# add = 2 + 6
# print(add)

# subtract = 4 - 5
# print(subtract)

# multiply =  5 * 5
# print(multiply)

# power = 20**4
# print(power)

# divide = 8//2
# print(divide)

# modulo_division = 7/2
# print(modulo_division)


# #Floats
# target_amount = 10.60
# print(target_amount)












#Boolens
#THEY return True or False

sadza = ""
if sadza == 10 :
    print(f"you puchased {sadza} ")
else:
    print("you have inssuficientcy funds")


password = ''
admin =""
if password == 1234:
    print("welcome admin Tasy")

elif password !=1234:
    print("try again")
else:
    print('incorrect password')



food = ""
if food == "lasgnae":
    print("l love it")

elif food != "lasgne":
    print("another plate please")
else:
    print('i want to change the menu')



numbers = 20
if numbers > 30:
    print('number is greater ')   
elif numbers < 30:
    print("the number is lessor")
else:
    print("none of the above")



num = 7
if num % 2 == 0:
    print('even number')
else: 
    print('old number')

num = 12
if num % 2 == 0:
    print('even number')
else: 
    print('old number')




#list
my_list = ['meat', ' pork', 'fish', 'chicken']
print(my_list)
my_list[1] = "Ham"
print(my_list)
my_list.append('beef')
print(my_list)



fruits = ['guava', 'mango', 'pear', 'peach']
print(fruits)
fruits[-1] ='orange'
print(fruits)
fruits.append('sweetpotato')
print(fruits)
print(fruits[-1])
print(fruits[1:])

###Slicing a list
numbers = [1,2,3,4,5]
print(numbers)
print(numbers[1:3])
print(numbers[0:-1])
print(numbers[-2])



#Dictionary key and Value 
details ={"name": 'Felistus', "age": 24, "location" : 'Harare'}
print(details)

#Acessing the key in a dictionary
print(details['age'])
print(details['name'])
print(type(details))

#modifying a dictionary
details['age'] = 25
print(details)
details['name'] = 'kelvin'
print(details)


##adding a key pair value in a dictionary
details['GPA'] = 23,4
print(details)



###Tuples

students = ('mary', 'ruth', 'Nalia', 'methew', 'diana', 'kelcee', 'Loveness')
print(students)
print(type(students))
print(students[1])
print(students[2:-1])
print(students[2:5])
print(students[1:-2])
##start,step,end
print(students[::3])
my_list= list(students)
print(my_list)


tuple1 = (1,2,3,4,5,6,7,8,9,)
tuple2 = (20,40,60,80,)
tuple3 =(30,60,90)
print(tuple1+ tuple3)
print(tuple2+tuple1)
myse_list = list(tuple2)
print(myse_list)
##to add into the new list
list2 = [110, 120,130, 140]
myse_list.extend(list2)
print(myse_list)
myse_list=tuple(myse_list)
print(myse_list)


#loops continue to exercute until a certain condition is exercuted(or told to stop)
#loops looks at a condition and if the 

#While loops they run until a condition is met






food = input("enter the food you like:")
while not food == "q":
   print(f"you like{food}")
   food = input("enter another food you like:")
   print("bye food lover")


name = "felistus"
hername =(input("Enter the name:"))
while hername != name: 
    print('incorrect name')
    hername = (input("Enter the name:"))
    print("correct name")


maths = int(input("guess the number:"))
while not maths== 7:
     print(f"you guessed the wrong number")
     maths = int(input("guess the number:"))

print("correct number")



house = int(input("enter house number:"))
while  house != 234:
    print(f"you entered the wrong house")
    house = int(input("enter house number:"))
    print("correct house")





answer =6
guess =int(input("guess the number :"))
while guess != answer:
     guess = int(input("wrong Number! guess again:"))

print("you guessed the right number!")


name = "felistus"
hername = (input("Enter the name:"))

while hername != name: 
     print('incorrect name')
     hername = (input("Enter the name:"))
    
print("correct name")





























































