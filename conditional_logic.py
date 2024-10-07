#! conditional logic in Python

# Conditional logic demo
age = int(input("Enter your age: "))

if age < 18:
    print("You are too young to vote.")
elif 18 <= age < 65:
    print("You are eligible to vote.")
else:
    print("You are a senior citizen and also eligible to vote.")

# Check if a number is positive, negative, or zero
number = int(input("Enter a number: "))

if number > 0:
    print(f"{number} is positive.")
elif number == 0:
    print(f"{number} is zero.")
else:
    print(f"{number} is negative.")

# Check if the number is even or odd using modulus logic
if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")

# Convert movie runtime (in minutes) to IMDb format (hours and minutes)

movie_minutes = int(input("Enter the movie duration in minutes: "))

# Ternary operation to calculate hours and minutes
hours = movie_minutes // 60  # Integer division to get the hours
minutes = movie_minutes % 60  # Modulus to get the remaining minutes

#! IMDB format: "Xh Ym" (X hours and Y minutes)
imbd_time = f"{hours}h {minutes}m" if hours > 0 else f"{minutes}m"

print(f"Movie runtime: {imbd_time}")
