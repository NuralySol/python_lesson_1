#! data structures

fruits = ["apples", "banana", "watermelon", "pear", "strawberry"]
print("fruits that are in the list: ", fruits, type(fruits), len(fruits))

start_index = 0  # starting at index 0
end_index = (
    2  #! ending at index 2 (range excludes the last index can not get the last index)
)

# List the index of each fruit use the for loop
for index, fruit in enumerate(fruits):
    print(f"Index of the fruits list are {fruit}: {index}")

for index in range(start_index, end_index):
    print(f"Range of {fruits[index]}: {index}")

# get the first one and the last one before in a range function
#! some variable declarations for list of fruits with total indices of 0-4

first_fruit = 1
last_fruit = 3

#! Different ways of looping through an list object all are viable depends on the style
# for loop to pass into an index for ranges

for index in range(first_fruit, last_fruit):
    print(f"Range of first fruit and the last fruit {fruits[index]}: {index}")

# Using list comprehension for iteration
[print(f"List comprehension fruit: {fruit}") for fruit in fruits]

# 'while' loop using indices
index = 0
while index < len(fruits):
    print(f"While loop fruit: {fruits[index]}")
    index += 1

# Looping through the list in reverse order
for fruit in fruits[::-1]:
    print(f"Fruit in reverse: {fruit}")
colors = ["red", "yellow", "green", "blue", "pink"]

# 'zip()' to loop through two lists
for fruit, color in zip(fruits, colors):
    print(f"The fruit {fruit} is {color}")

# Conditional 'for' loop
for fruit in fruits:
    if "a" in fruit:
        print(f"Fruit containing 'a': {fruit}")

# pop an item from the list
last_fruit_item = fruits.pop()
print(last_fruit_item)

# append to the last index of the fruits list
fruits.append("orange")
print("new fruits are: ", fruits)

# targetted removal
fruits[1] = "blueberry"
print(fruits)

# insert itself and becomes itself a new index 3
fruits.insert(3, "grapes")
print(fruits)

fruits.insert(4, "kiwi")
print("New fruits list is ", fruits)



