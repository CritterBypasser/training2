n = int(input())
stock = list(map(int, input().split()))

min_price = stock[0]
max_profit = 0

for price in stock[1:]:
    profit = price - min_price
    if profit > max_profit:
        max_profit = profit
    if price < min_price:
        min_price = price

print(max_profit)