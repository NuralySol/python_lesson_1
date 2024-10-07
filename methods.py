
#! User input method in Python
# Need to store in the variable

first_name = input("First name: ")
last_name = input("Last name: ")
team_num = input("Team num: ")

# cannot conc. the 'int' into string
name_tag = "\nHello!\n my name is \n" + first_name + " " + last_name + " and I am in team " + team_num

# Print the concatenated name tag
print(name_tag)
