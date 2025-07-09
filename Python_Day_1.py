
#---------------Numbers-----------#

# character_name = "Farhan"
# character_age = "20"


# print("So my name is " +  character_name + ",")
# print("I am " + character_age + "Old",)
# print("I want to become Ai/Ml enginear at the age of " + character_age + ".")


# print("Lets see who \" Win \"")
# print("Lets see who \n Did a good job. ")




# phrase = "Dreams are so big"




# print(phrase.isalpha())
# print(phrase.isalnum())


# name = input("Enter you name :")


# print("Length", len(name))

# print("Contains 'far,", 'far' in name)

# print("Replace 'a", name.replace('a','@'),)




# name = input("Enter Full Name :")
# print("Username :",name.lower())
# print(name.strip())
# print("Replace Number:",name.replace('a','@'))




# Numbers----------------

# Bulding Basic Calculator:


# a = float(input("Enter the first number :"))
# b = float(input("Enter the second number :"))


# print("Sum",a + b);
# print('Differnce', a -b);
# print("Product",a *b);
# print("Division", a / b);

# # Finding the Area of cirlce:
# radius = float(input("Enter the radius if circle:"));


# area = 3.1416 *(radius ** 2);


# print("The radius of circle is :",area)



# Creating Mad Labs Game:


# color = input("Enter your Color : ")

# plural_noun = input("Enter you Plural_Noun : ")

# celebratiy = input("Enter Celebrity Name :")

# print("\n-- Your Poem --")

# print(f"Roses are {color}")
# print(f"{plural_noun} are blue.")
# print(f"I love {celebratiy}")

# print("\n-- Your Poem --")







# ----------------------Lists----------------#


# friends = ["Farhan","Musa","Hamza","ALi","Haseeb","Me"]
# Numbers = [2,3,7,5,4,3,6,1,]


# Numbers.pop()

# print(Numbers)


# Create a Favorite Movies List


# Favoite_Anime = ["Attack on Titans","Naruto","Bleach","Jutsu Kaisan"]

# Favoite_Anime.append("Full Metal Alchemist");

# Favoite_Anime.insert(2,"Demon Slayers");


# Favoite_Anime.remove("Bleach");


# print(Favoite_Anime)









# Functions:



# def say_hi(name,age):
#           print("Hello " + name + " You are " ,age,)
    


# say_hi("Farhan",21)
# say_hi("Musa",11)



# name = input("Enter your name ")


# def great_user(name):
#     return name

# print(great_user("Hello," + great_user("Farhan") + "Wellcome to pytho."))
        



# def max_number(a,b):
    
#  return 




# is_Male = True
# is_Tall = False


# if is_Male and is_Tall:
#     print("You are Male & tall too.")
# elif not(is_Male) and is_Tall:
#     print("You are not male and tall")
# elif is_Male and not(is_Tall):
#     print("You are short male.")    
# else:
#     print("You are niether a male or tall.")    


# Num1 = input("Enter the first number :")
# Num2 = input("Enter the second number :")
# Num3 = input("Enter the third number :")



# def max_number(Num1,Num2,Num3):
#     if  Num1 >= Num2 and Num1 >= Num3:
#         return Num1
#     elif Num2 >= Num1 and Num2 >= Num3:
#         return Num2
#     else:
#         return Num3

# print(max_number(Num1,Num2,Num3))


# Print the Greatest Markes


# def max_marks(marks):
#     if marks >= 100 or marks <= 0:
#         return "Invalied Marks"
#     elif marks >= 90:
#         return "Grade A+"
#     elif marks >= 80:
#         return "Grade: A"
#     elif marks >= 70:
#         return "Grade: B"
#     else:
#         return "Grade: C or below"


# marks = int(input("Enter your marks please: "))


# print(max_marks(marks))




# Building The actual Calculator:


# def calculator():
#     num1 = float(input("Enter the first number :"))
#     op = input("Enter the operator :")
#     num2 = float(input("Enter the second number :"))

#     if op == "+":
#         print(num1 + num2)
#     elif op == "-":
#         print(num1 - num2)
#     elif op == "*":
#         print(num1 * num2)        
#     elif op == "/":
#         if num2 != 0:
#             print(num1 / num2)
#         else:
#             print("❌ Cannot divide by zero")
#     else:
#         print("Invalid operator")

# calculator()



#----------------------Dictionary---------------#




# month_Coverstion = {

#     "Jan" : "January",
#     "Fab" :"Febrauary",
#     "Mar" : "March",
#     "Ap":"April"
# }



# for key in month_Coverstion:
#     print(key," : ", month_Coverstion[key])





# Person 



# Person = {

#     "name" :"Farhan",
#     "age" :"20",
#     "city": "Nowshera",
# }


# Person["Skills"] = ["Python","Mern"]

# for key in Person:
#     print(key, ": ",Person[key])
# print(Person)



# i = 100

# while i >= 1:
#     print(i)
#     i -= 1


# print("Loop Finished!")




#---------------Build Guesing Game------------#


# secret_word = "Boss"
# guess = ""
# guess_count = 0
# guess_limit = 3
# out_of_guess = False



# difficulty = input("Choose difficulty (easy/hard): ").lower()


# if difficulty == "easy":
#     guess_limit = 5
# elif difficulty == "midium":
#     guess_limit = 3
# else:
#     print("Invalied difficulty Level:")        

# while guess != secret_word and not out_of_guess:
#     if guess_count < guess_limit:
#         guess = input("Enter Guess: ")
#         guess_count += 1
#     else:
#         out_of_guess = True  


# if out_of_guess:
#     print("❌ You lose the game! Try again.")
# else:
#     print("✅ You win, Boss!")





#-----------------For Loops-------



# friends = ["Haseeb","ALi","Musa","Hamza"]

# for index in range(len(friends)):
#     print(friends[index])



#---------------exponent Functions----------#



# Base = float(input("Enter Base Number :"))
# Power = float(input("Enter Power Number :"))



# result = pow(Base,Power)
# print(result)



# 



# def raise_to_power(base_num, power_num):
#     result = 1
#     for index in range(power_num):
#         result = result * base_num  # Multiply again and again
#     return result  # ✅ Return after loop ends

# print(raise_to_power(3, 4))  # Output: 81




# _-------------------2D Lists-------------#

# A 2D list is simply list ,including another list .Known as 2 Dimensional List.

# number_grid = [

#     [1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12],
#     [0]
# ]


# for row in number_grid:
#         for num in row:
#                 print(num)



# names = [
#     ["Ali", "Hamza", "Sara"],
#     ["Farhan", "Haseeb", "Musa"],
#     ["Usman", "Sana", "Amna"]
# ]


# print(names[2][1])
# print(names[2])

# for name in names:
#     for each in name:
#         print(each)




# grades = [
#     ["Farhan", 90],
#     ["Ali", 85],
#     ["Musa", 78],
#     ["Eren", 10],
#     ["Jin", 25],
#     ["Puke", 33]
# ]



# for student in grades:
#     print(f"{student[0]} scored {student[1]}")





# def Translator(phrase):
#     translattion = ""
#     for letter in phrase:
#         if letter in "AEIOUaeiou":
#             translattion = translattion + "~~~~"
#         else:
#             translattion = translattion + letter
#     return translattion


# print(Translator(input("Enter a word Please :")))



#---------------try......except---------#

# try:
#     num = int(input("Enter a number: "))
#     print(100 / num)
# except ZeroDivisionError as err:
#     print(err)
# except ValueError as err :
#     print(err)    




# try:
#     age = int(input("Kindly, enter you age please :"))


#     print(age)

# except ValueError as err:
#     print(err)

import pyjokes

print("Here's a random dev joke, Boss:")
print(pyjokes.get_joke())
