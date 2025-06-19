"""
Define a list 'candles' and fill it with hardcoded values, later on we can add input functionality.

"""

def birthdayCakeCandles(candles):
    if not candles:
        return False
    else:
        count = 0 
        tallest = candles[0]
        for candle in candles:
            if candle > tallest:
                tallest = candle
            if candle == tallest:
                count += 1
        return count    

# candles = [4,4,1,3]
# output = birthdayCakeCandles(candles)
test_cases = [[1, 1, 1, 1], [4,4,1,3], []]

for candles in test_cases:
    output = birthdayCakeCandles(candles)
    if not output:
        print("There are no candles to blow!")
    else:
        print(f"There are {output} candles on the cake.")