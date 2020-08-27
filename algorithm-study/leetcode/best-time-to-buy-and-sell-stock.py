# from itertools import combinations as c


# def maxProfit(prices):
#     if len(prices) == 1 or not prices:
#         return 0
#     return max(max([b-a for a, b in c(prices, 2)]), 0)


def maxProfit(prices):
    pos, profit = 0, 0
    for i in range(len(prices)):
        if prices[pos] > prices[i]:
            pos = i
        else:
            temp = prices[i] - prices[pos]
            if temp > profit:
                profit = temp
    return profit


prices = [2, 100, 1, 3]


print(maxProfit(prices))
