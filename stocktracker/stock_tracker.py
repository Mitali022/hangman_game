# Stock Portfolio Tracker

# Step 1: Predefined stock prices (dictionary)
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 2800,
    "MSFT": 300
}

# Step 2: Total investment variable
total_investment = 0

print(" Welcome to Stock Portfolio Tracker")

# Step 3: Loop for multiple entries
while True:
    # Take stock name input
    stock = input("Enter stock name (or 'done' to finish): ").upper()
    
    # Exit condition
    if stock == "DONE":
        break
    
    # Check if stock exists
    if stock in stock_prices:
        # Take quantity
        quantity = int(input("Enter quantity: "))
        
        # Calculate value
        price = stock_prices[stock]
        total = price * quantity
        
        print(f"{stock} = {price} x {quantity} = {total}")
        
        # Add to total investment
        total_investment += total
    else:
        print("❌ Stock not found!")

# Step 4: Final result
print("\n Total Investment Value:", total_investment)