# Flow control statements can decide which python instructions to execute under which condition
# Boolean values in python
# While the integer , floating - point and string data types have an unlimited number of possible values
# the boolean data type has only two value: true or false
# When typed as python code the boolean values True and False lack the quotes you place around strings
# Boolean values always start with a capital T or F with the rest of the word in lowercase
# Like any other value , boolean value are used in expression and can  be stored in variables


# Comparison operator compare two values and evaluates down  to a single boolean value
# These operators evaluate to True or False depending on the values you give them.

# Eg:: a==b
#      a<b
#      a>b
#      a != b
#      a<= b
#      a>=b

# The comparison operators evaluates to boolean values , you can use them in expression with the boolean operators.
# Recall that  the and , or  and not operators are called boolean operators because they always opearte on boolean values True and False

# NOTE : The boolean operators have an order of operations just like the math operators do
# Python evaluates the not operators first then the and operators and then the or operators


# var = True
# print(var)

#print(True=10)  ##will throw an error(SyntaxError: cannot assign to True)

# print(True and True)
# print(True and False)
# print(not True)
# print(not False)
#
# print((1<2) and (3<4))  # true
#
# print((10<5) or(50>10)) # true

##Elements of Flow Control

#Flow Control statements often starts with a part called the condition and all are followed by a block of code called the clause


# num = 20
# if(num<10):
#     print("the  number is less than 10")
# else:
#     print("The number is greater than 10")


# nested if condition
# num = 3
# if num <10:
#     print('less than 10')
#     if num < 5:
#         print('less than 5')

## FLOW CONTROL STATEMENTS
# if statement
# The most common type of flow control statemnet is the if statement
# An if statement's clause will execute if the statement's condition is true.
# The caluse is skipped if the condition is False . In python statement consist of the following:
# 1> The if keyboard
 # 2> A condition (that is an expression that evalusates to true or false)
 # 3> a colon
 # 4> starting on the next line , an indented block of code(called the if clause)

