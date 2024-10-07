
#! Calculate the restaurant bill using ints and floats

# User inputs 
food_tot = input("Food tot: ")
print("Food total $", food_tot)

bev_tot = input("Bev tot: ")
print("Bev total $", bev_tot)

user_tip = float(input("Tip %: ")) / 100  # Convert tip percentage to a decimal (float)

# Constant declaration for NYC sales tax (or you can declare a tuple)
NYC_SALES_TAX = 0.0875

# Convert to float from string input for calculation
subtotal = float(food_tot) + float(bev_tot)

# Calculate sales tax based on the subtotal
sales_tax = NYC_SALES_TAX * subtotal

# Calculate tip based on the original subtotal (without tax)
tip_amount = subtotal * user_tip

# Calculate total bill with sales tax and tip added
total_bill = subtotal + sales_tax + tip_amount

#! Output the calculations with formatted strings (with ternary operator for formmating to money)
print(f"Subtotal: ${subtotal:.2f}")
print(f"Sales tax (NYC): ${sales_tax:.2f}")
print(f"Tip amount: ${tip_amount:.2f}")
print(f"Total bill (including tax and tip): ${total_bill:.2f}")