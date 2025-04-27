# ================== Taking Input and Finding the Greatest Number ==================

firstNumber = int(input("Enter first number: "))
secondNumber = int(input("Enter second number: "))
thirdNumber = int(input("Enter third number: "))

if firstNumber > secondNumber and firstNumber > thirdNumber:
    print("First number is greatest")
elif secondNumber > firstNumber and secondNumber > thirdNumber:
    print("Second number is greatest")
elif thirdNumber > firstNumber and thirdNumber > secondNumber:
    print("Third number is greatest")
else:
    print("All numbers are equal")

# ================== Check if a Number is Divisible by 7 ==================

number = int(input("Enter a number: "))
if number % 7 == 0:
    print(f"The {number} is divisible by 7")
else:
    print(f"The {number} is not divisible by 7")

# ================== Unpacking a Tuple ==================

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits

print(x)
print(y)
print(z)

# ================== Create a Student List ==================

student = ["Farhan", 44, "Pakistan", 44.3]

# ================== Append a Number to List ==================

list1 = [1, 2, 3, 4]
list1.append(6)
print(list1)

# ================== Find Index of a Number in Tuple ==================

tup = (1, 11, 34, 1, 22, 2, 2)
print(tup.index(2))

# ================== Adding Movies to a List ==================

Movie1 = input("Enter first movie name: ")
Movie2 = input("Enter second movie name: ")
Movie3 = input("Enter third movie name: ")

movieList = []
movieList.append(Movie1)
movieList.append(Movie2)
movieList.append(Movie3)

print("Movie List:", movieList)

# ================== Check if a List is a Palindrome ==================

list2 = [1, 2, 2, 1]

copy_list = list2.copy()
copy_list.reverse()

if copy_list == list2:
    print("Palindrome")
else:
    print("Not Palindrome")

# ================== Count Number of Students Starting with 'A' ==================

grades = ('B', 'B', 'C', 'A', 'A', 'A', 'D', 'D', 'D', 'F')

print("Count of 'A':", grades.count('A'))
print("Count of 'B':", grades.count('B'))

# ================== Store Tuple in List and Sort ==================

grades_list = list(grades)
grades_list.sort()
print("Sorted Grades:", grades_list)
