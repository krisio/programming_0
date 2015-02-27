def calculate_coins(summ):
    counted_coins = {}

    coins = [100, 50, 20, 10, 5, 2, 1]

    summ = round(summ * 100)

    for coin in coins:

        coin_used = summ // coin

        counted_coins[coin] = coin_used

        summ = summ - coin_used * coin

    return counted_coins

print(calculate_coins(8.94))
print(calculate_coins(0.53))
