# # ================== Taking Input and Finding the Greatest Number ==================

# firstNumber = int(input("Enter first number: "))
# secondNumber = int(input("Enter second number: "))
# thirdNumber = int(input("Enter third number: "))

# if firstNumber > secondNumber and firstNumber > thirdNumber:
#     print("First number is greatest")
# elif secondNumber > firstNumber and secondNumber > thirdNumber:
#     print("Second number is greatest")
# elif thirdNumber > firstNumber and thirdNumber > secondNumber:
#     print("Third number is greatest")
# else:
#     print("All numbers are equal")

# # ================== Check if a Number is Divisible by 7 ==================

# number = int(input("Enter a number: "))
# if number % 7 == 0:
#     print(f"The {number} is divisible by 7")
# else:
#     print(f"The {number} is not divisible by 7")

# # ================== Unpacking a Tuple ==================

# fruits = ["apple", "banana", "cherry"]
# x, y, z = fruits

# print(x)
# print(y)
# print(z)

# # ================== Create a Student List ==================

# student = ["Farhan", 44, "Pakistan", 44.3]

# # ================== Append a Number to List ==================

# list1 = [1, 2, 3, 4]
# list1.append(6)
# print(list1)

# # ================== Find Index of a Number in Tuple ==================

# tup = (1, 11, 34, 1, 22, 2, 2)
# print(tup.index(2))

# # ================== Adding Movies to a List ==================

# Movie1 = input("Enter first movie name: ")
# Movie2 = input("Enter second movie name: ")
# Movie3 = input("Enter third movie name: ")

# movieList = []
# movieList.append(Movie1)
# movieList.append(Movie2)
# movieList.append(Movie3)

# print("Movie List:", movieList)

# # ================== Check if a List is a Palindrome ==================

# list2 = [1, 2, 2, 1]

# copy_list = list2.copy()
# copy_list.reverse()

# if copy_list == list2:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# # ================== Count Number of Students Starting with 'A' ==================

# grades = ('B', 'B', 'C', 'A', 'A', 'A', 'D', 'D', 'D', 'F')

# print("Count of 'A':", grades.count('A'))
# print("Count of 'B':", grades.count('B'))

# # ================== Store Tuple in List and Sort ==================

# grades_list = list(grades)
# grades_list.sort()
# print("Sorted Grades:", grades_list)




#Lesson-4
#  <===============================Dictionary & Set in Python==========================>

# Dictoniary are used to store data values in key:value paris.They are unordered and mutable and dont allow duplicate key:


# Simple Disctoniary:with all data types 

# dict = {

# "name" : "Farhan Yousafzau",
# "roll_no" : 4404,
# "subject" :['Computer_Science','English'],
# "Awards" : ('Full Stack Developer',"Generative Ai master","CEO of techNino"),
# "Batch_no": 17
# }

# print(dict.items())
# # Nested Distionary:


# nest_Dict = {
#  " school_name" : 'Gurus Tech Hub',
#  "branches" : {
#      "nowshera" :"Frontend",
#      "islamabad" : "Backend",
#      "Lahore" : "Devops"
#  }

# }






#Dictoniary Methods
# .keys() --> return all the keys but not the nested key
# .values() -----> return all the values of keys 
# .items() --->   return all the (key,values) as tuple -->();
# .get() ---> return the the key according to the values
# .update() -->insert the specified items in the dict.                                        #




#SET IN PYTHON: DF
# SET IN THE COLLECTIONS OF UNORDERED ITEMS,EACH ELEMENT IN THE SET MUST BE UNIQUE AND MUTABLE.


set = {1,2,3,4,5,5,'Hello World','Hello World', 99.9,99.9}

set2 = {9 ,7 ,8 ,10, 1} 

# new = set.union(set2)
# new =  set.intersection(set2)
# print(new); #{1, 2, 3, 4, 5, 99.9, 'Hello World'} so the repeated values only stores onces 


#Set Methods:   
#     .add() -->use to add values in the set
# .remove() --> use to remove values from the set
# .pop()  ---> remove the reandom value
#   .clear() --use to empites the set .
#.union() --> combine both set values and return new 
#.intersection() --> combine common values and return 




#Practice Questions:

words = {
    "table" : {
        "a peice of furtinure",
        "list of facts and figures"
    } ,
    "cat" : "a small animal"
}

print(words)


# to find the number of classes need for number of courses are avaiable:

language = {
    'python','java','C++','python','javascript','java','python','java','c++','c'
    }

print(len(language))




# 
marks = {}
phy = input("Enter Physics marks:")

marks.update({"phy":phy})

eng = input("Enter english marks:")
marks.update({"eng":eng})

maths = int(input("Enter your maths marks:"))
marks.update({"maths":maths})
#Lesson-5:


print(marks) #Ans -->{'phy': '89', 'eng': '09', 'maths': 800}
#=======================Loops in Python:====================================>