# The String value  of the number is considered a completely different value from the integer or floating point version an integer can be equal to a floating point
print(42 =='42') #false
print(42 == 42.0) #true
print(42.0 == 0042.000) #true

# Python makes the distinction because string are text , while  integers and floats are both numbers