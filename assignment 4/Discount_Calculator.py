# Assignment 4: Discount Calculator

# Function to calculate discount
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:  # Only apply if discount is 20% or more
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price  # Return original price if discount < 20%


# --- Main Program ---
# Ask user for inputs
price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

# Call function
final_price = calculate_discount(price, discount_percent)

# Print results
if discount_percent >= 20:
    print(f"✅ Discount applied! Final price: {final_price:.2f}")
else:
    print(f"No discount applied. Price remains: {final_price:.2f}")
