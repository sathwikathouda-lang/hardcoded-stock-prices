# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330
}

portfolio = {}
total_value = 0

# Number of stocks to enter
n = int(input("Enter number of stocks: "))

# Input stock details
for i in range(n):
    stock = input("Enter stock symbol: ").upper()

    if stock not in stock_prices:
        print("Stock not found in price list.")
        continue

    quantity = int(input("Enter quantity: "))
    portfolio[stock] = quantity

# Calculate investment value
print("\nPortfolio Summary")
print("-" * 30)

for stock, quantity in portfolio.items():
    value = stock_prices[stock] * quantity
    total_value += value

    print(f"{stock}: {quantity} shares × ${stock_prices[stock]} = ${value}")

print("-" * 30)
print(f"Total Investment Value: ${total_value}")

# Optional: Save to file
save = input("\nSave report to file? (yes/no): ").lower()

if save == "yes":
    with open("portfolio_report.txt", "w") as file:
        file.write("Portfolio Summary\n")
        file.write("-" * 30 + "\n")

        for stock, quantity in portfolio.items():
            value = stock_prices[stock] * quantity
            file.write(
                f"{stock}: {quantity} shares × ${stock_prices[stock]} = ${value}\n"
            )

        file.write("-" * 30 + "\n")
        file.write(f"Total Investment Value: ${total_value}\n")

    print("Report saved as portfolio_report.txt")