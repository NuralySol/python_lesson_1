# Python data science introduction (All of the basics all over again)
# Declare two variables: on in single quotes, the other in double
import os
from PIL import Image

# Path to your image file
image_path = "assets/food-bev-calculator.jpg"

# Check if the file exists before trying to display it
if os.path.exists(image_path):
    # Open the image file
    img = Image.open(image_path)

    # Show the image
    img.show()
else:
    print(f"File not found: {image_path}")

first_name = "Nuraly"
last_name = "Soltonbekov"

# print your name
print(f"Hello, {first_name}!")
print(f"And my last name is -> {last_name}")

#  math and integers and it is a bad practice to make x and y variable names
x = 5
print(f"integer variable is {x}")
print(x**2)  # squaring is different in python than Javascript
print(x**5)  # to the power of five
print(x / 2)  # diviision operator
print(type(x))  # type of a variable to see the type of a variable <class 'int'>
print(type(first_name))  # type of <class 'str'>
print(type(True))  # type of a True a boolean

# declare a boolean

is_monday = True
print(f"today is monday, {is_monday}")  # f-string with a boolean

# declare a list

pets = ["cat", "dog", "parrot"]
print(f"these are the pets , {pets}")
print(type(pets))  # list akin to an array in Javascript

y = 3.5  # float even 3.0 is a float in python
print(
    "y:", y, "\ndatatype of:", type(y)
)  # print the var and the type in a single print statement

pet = "iguana"
pet = "bunny"  # declaration and overwritten the variable 'iguana' is gone
print(pet)  # print the new pet
print("pet:", pets, type(pets))

print(
    len(pet)
)  # method to see how many characaters in a string: spaces count towards the length of a string
print(len(pets))  # a list return statement with 'len' method

# concatenation
# print a greeting as a name tag

name_tag = "Hello! my name is " + first_name + " " + last_name

print("name_tag: ", name_tag)  # print the concatenation of a name tag connect a string

# useful methods for python data science

veg = "carrot"
print("veg:", veg, type(veg))

lucky_num = 7
print("lucky_number: ", lucky_num, type(lucky_num))
# print(len(lucky_num)) cannot print len of integers
lucky_digit = str(lucky_num)
print("lucky_digit", lucky_digit, type(lucky_digit), "len is:", len(lucky_digit))

nums = [1, 3, 5, 7]
print("nums printed:", nums, type(nums))

score = 80.532
print("round the score:", round(score))

# int method on an object floors the argument
print(int(score))

# round to 3 decimal places
big_score = 88.23123123
print(round(big_score, 3))  # round to 3 decimal places needs a second argument

# turn a stringy number into a real one
lucky_str = "888"
print("lucky_str", lucky_str, type(lucky_str))
# asssign the lucky_str to lucky_int to make it into a 'int'
lucky_int = int(lucky_str)
print("lucky_int", lucky_int)

# + operater only work with math in relation to 'int' type of data
double_luckey = lucky_int + lucky_int
print(double_luckey)  # prints 1776 which

