def three_odds(arr: list) -> bool:
    counter = 0
    for num in arr:
        if num % 2 != 0:
            counter += 1
        else:
            counter = 0
        if counter == 3:
            return True
