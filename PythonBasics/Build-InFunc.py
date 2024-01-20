#print() function: it displays the string value inside the parentheseis on the screen

print("hello")
print("what is your name")

## NOTE
# we can also use print function to put a blank line on the screen ;
# just call print() with nothing in between the parenthesis

# print(5+10)
# print("PrepInsta")
# print()  # to add blank line
# print("Helps students")


# input() helps us to externally communicate with the user and take values from them
# input() function waits for the user to type some text on the keyboard and press ENTER
# print("What is your name?")
# myName = input()  # enter your name

# we can think of an input() function call as an expression that evaluates to whatever string the user typed in

# len()
# if you pass a string to the len() function it will evaluate to the integer value of the number of characters in the string.

# print("The length of your name is: ")
# print(len(myName))

## NOTE: Notice the print() allows you to pass it either integer values or string values.

## int() function: converts the passed value into integer format.

# print(int('200'))
# If you pass a value to int() that it can not evaluates as an integer, python will display an error message


# num1 = int(input("Enter the first number"))
# num2 = int(input("Enter the second number"))
# print(num1 + num2)

# Float() Function
# Float values are those which contains decimal points
# myValue = float(84)
# print(myValue)

print(int(10.95))

print(int('200'))
# print(int('200.20')) # ValueError: invalid literal for int() with base 10: '200.20'
print(len(" "))  # len function even counts the blank spaces
print(len("  "))




