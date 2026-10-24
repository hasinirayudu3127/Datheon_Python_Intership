import csv
from pathlib import Path

# Sample stock portfolio
portfolio = {
    "AAPL": {"buy_price": 180.00, "shares": 5, "current_price": 225.00},
    "GOOGL": {"buy_price": 150.00, "shares": 3, "current_price": 175.00},
    "MSFT": {"buy_price": 400.00, "shares": 2, "current_price": 420.00},
    "AMZN": {"buy_price": 170.00, "shares": 4, "current_price": 190.00},
}

total_invested = 0
total_current_value = 0
results = []

print("=" * 75)
print("           STOCK PORTFOLIO PERFORMANCE TRACKER")
print("=" * 75)

print(
    f"{'Ticker':<10}{'Shares':>8}{'Invested':>15}"
    f"{'Current Value':>18}{'Profit/Loss':>15}"
)
print("-" * 75)

for ticker, details in portfolio.items():
    buy_price = details["buy_price"]
    shares = details["shares"]
    current_price = details["current_price"]

    invested = buy_price * shares
    current_value = current_price * shares
    profit_loss = current_value - invested
    percentage = (profit_loss / invested) * 100

    total_invested += invested
    total_current_value += current_value

    results.append({
        "Ticker": ticker,
        "Buy Price": f"{buy_price:.2f}",
        "Shares": shares,
        "Current Price": f"{current_price:.2f}",
        "Invested": f"{invested:.2f}",
        "Current Value": f"{current_value:.2f}",
        "Profit/Loss": f"{profit_loss:.2f}",
        "Return (%)": f"{percentage:.2f}"
    })

    print(
        f"{ticker:<10}{shares:>8}"
        f"{invested:>15.2f}{current_value:>18.2f}"
        f"{profit_loss:>15.2f}"
    )

total_profit_loss = total_current_value - total_invested
overall_return = (
    (total_profit_loss / total_invested) * 100
    if total_invested else 0
)

print("-" * 75)
print(f"Total Invested:       {total_invested:.2f}")
print(f"Total Current Value:  {total_current_value:.2f}")
print(f"Total Profit/Loss:    {total_profit_loss:.2f}")
print(f"Overall Return:       {overall_return:.2f}%")
print("=" * 75)

# Save the results to a CSV file
csv_path = Path(__file__).with_name("portfolio_summary.csv")

with csv_path.open("w", newline="", encoding="utf-8") as file:
    fieldnames = [
        "Ticker", "Buy Price", "Shares", "Current Price",
        "Invested", "Current Value", "Profit/Loss", "Return (%)"
    ]

    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(results)

print(f"\nPortfolio report saved to: {csv_path.name}")