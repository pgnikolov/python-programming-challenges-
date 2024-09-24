def maxProfit(prices):
    """
    Calculates the maximum profit that can be obtained by making a single buy and sell
    operation on a given list of stock prices.

    Parameters:
    prices (List[int]): A list of integers representing the daily stock prices.

    Returns:
    int: The maximum profit that can be obtained, or 0 if no profitable operation is possible.
    """
    if not prices:
        return 0

    min_price = float('inf')
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price

    return max_profit

#time complexity O(n)