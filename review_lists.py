fruits = ["apples", "banana", "watermelon", "pear", "strawberry"]
print("fruits that are in the list: ", fruits, type(fruits), len(fruits))

# List methods and operations
print("\n### LIST OPERATIONS ###")

# Append
fruits.append("orange")
print("After append:", fruits)

# Extend
more_fruits = ["mango", "papaya"]
fruits.extend(more_fruits)
print("After extending with more fruits:", fruits)

# Insert
fruits.insert(2, "blueberry")
print("After inserting 'blueberry' at index 2:", fruits)

# Remove
fruits.remove("banana")
print("After removing 'banana':", fruits)

# Pop
popped_fruit = fruits.pop()
print("After popping the last fruit:", fruits)
print("Popped fruit:", popped_fruit)

# Sorting
fruits.sort()
print("Sorted fruits:", fruits)

# Reverse sorting
fruits.sort(reverse=True)
print("Sorted fruits in reverse:", fruits)

# Count
apple_count = fruits.count("apples")
print(f"Number of apples in the list: {apple_count}")

# Index
index_of_pear = fruits.index("pear")
print(f"Index of 'pear': {index_of_pear}")

# Copy
fruits_copy = fruits.copy()
print("Copied list of fruits:", fruits_copy)

# Clear
fruits_copy.clear()
print("Cleared copy of fruits list:", fruits_copy)

# Slicing
fruit_slice = fruits[1:4]
print(f"Sliced fruits (index 1 to 3): {fruit_slice}")

# Length of the list
fruit_length = len(fruits)
print(f"Total number of fruits: {fruit_length}")

# List Comprehension
fruits_with_e = [fruit for fruit in fruits if "e" in fruit]
print("Fruits containing 'e':", fruits_with_e)

# Map
fruits_upper = list(map(str.upper, fruits))
print("Fruits in uppercase:", fruits_upper)

# Filter
long_fruits = list(filter(lambda fruit: len(fruit) > 5, fruits))
print("Fruits with more than 5 characters:", long_fruits)

# Deleting elements
del fruits[1]
print("After deleting the element at index 1:", fruits)

# Nested lists
nested_list = [["apples", "banana"], ["orange", "pear"], ["watermelon", "grapes"]]
print("\n### NESTED LIST OPERATIONS ###")
print("First fruit in the first list:", nested_list[0][0])
print("Second fruit in the second list:", nested_list[1][1])

# Iterating over a nested list
for inner_list in nested_list:
    for fruit in inner_list:
        print(fruit, end=", ")
    print()