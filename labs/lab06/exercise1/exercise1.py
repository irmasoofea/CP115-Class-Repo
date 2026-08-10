# Escape Characters Exercise
# Print the receipt shown in the lab, using \n for new lines and \t for columns.
# Calculate every total, subtotal, and tax in your code. Do not type the money
# amounts in directly. Show every amount with exactly two decimal places.

# Price of each item
#Coffee: $3.50, Muffin: $2.10, Water: $1.05
coffee_price = 3.50
coffee_qty = 2
total_coffee = coffee_price * coffee_qty
muffin_price = 2.10
muffin_qty = 3
total_muffin = muffin_price * muffin_qty
water_price = 1.05
water_qty = 4
total_water = water_price * water_qty

# Calculate subtotal, tax, and total
subtotal = total_coffee + total_muffin + total_water
tax = subtotal * 0.06
total = subtotal + tax

receipt = f"========== RECEIPT ==========\nItem\t\tPrice\tQty\tTotal\nCoffee\t\t$3.50\t2${total_coffee}\nMuffin\t\t$2.10\t3${total_muffin}\nWater\t\t$1.05\t4${total_water}\n------------------------------\nSubtotal\t\t\t${subtotal}\nTax (6%)\t\t\t${tax}\nTotal\t\t\t${total}f\n============================"
print(receipt)