#it is block of reusable code
#Uses : They make your code more modular, organized and easy to mantain
#to define a function in python use the word ##def followed by the function name, parentheses() and colon :.
##ffunction_name : the name of the function should be descriptive of its task
##parameters : they are temporary variables tha is used within a function..They are placed inside the parenthess
##return: optional, specifies the value to return from the function


# def  happy_birthday (name, age):
#     print(f"happy birthday to {name}")
#     print(f"you are {age} years old")
#     print(f"happy birthday to you {name}")
#     print()


# happy_birthday( "Sydney", 28)
# happy_birthday("Nathel",13)
# happy_birthday("Anna", 29)








# def display_invoice(username,amount, due_date):
#     print(f"Hello {username}")
#     print(f"your bills is  ${amount} and it is due{due_date} ")
#     print()

# display_invoice ("John", 34.60, "06/09")  
# display_invoice ("Mark", 35.60, "06/09")  


##Return a statement: is a statement used to end a function and send the results bsck to the caller

# def add (x,y):
#     z = x + y
#     return z

# def subtract (x,y):   
#     return x+Y


# def multiply(x,y):
#     return x* y
# result = multiply(7,5)
# print(result)

#      ##OR
# def divide (x,y):
#     return x/y
# print(divide(7,2))
 

# print(3)
# print(subtract(1,2))
# print(multiply(1,2))
# print(divide(1,2))




# def create_name ( first, last):
#     first = first.capitalize()
#     last = last.capitalize()
#     return first +"" + last
# full_name = create_name ('felistus' ,  'gomba')
# print (full_name)



#POSITIONAL ORDER OF FUNCTIONS

# def power(base, exponent):
#     return base**exponent #this return function cannot print the value 
# print(power(2,3))





#Default value when we dont know the name of all people
# def greet(name="Guest"):
#     print(f'hello,{name}')
# greet ()   

# def greet(name):
#     print(f'Hello,{name}')  #this line print the invisible ouput if tisina ku caller the output
# greet("John")    


#global is outer #NESTED FUNCTIONS
# def outer():
#     print("This is outer function")
#     def inner():
#         print("This inner function")
#     outer()    
#     inner()
# outer()       

#GLOBAL FUNCTION INSIDE THE LOCAL
def global_function():
    print('This is global function')
global_function()    

def another_function():
    global_function()
another_function()   