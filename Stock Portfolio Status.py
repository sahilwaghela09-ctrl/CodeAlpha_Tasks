# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140
}

total_investment = 0

print("Available stocks:", stock_prices)

while True:
    stock = input("Enter stock name (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock in stock_prices:
        quantity = int(input("Enter quantity: "))
        cost = stock_prices[stock] * quantity
        total_investment += cost
        print("Added:", stock, "Cost:", cost)
    else:
        print("Stock not found")

print("\nTotal Investment Value:", total_investment)

# Optional: Save to file
file = open("investment.txt", "w")
file.write("Total Investment: " + str(total_investment))
file.close()
