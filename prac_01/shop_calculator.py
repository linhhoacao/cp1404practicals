# Initialize variables
num_items = 0
total_price = 0
# Prompt for number of items
while True:
    num_items = int(input("Number of items: "))
    if num_items >= 0:
        break
    else:
        print("Invalid number of items!")

# Calculate total price
for i in range(num_items):
    price = float(input("Price of item: "))
    total_price += price
    
# Apply discount if total price is over $100
if total_price > 100:
    discount = total_price * 0.10
    total_price -= discount
# Display the total price
print("Total price for", num_items, "items is ${:.2f}".format(total_price))