stocks = {
    'GOOG': 520.54,
    'FB': 54.23,
    'YHOO': 39.23,
    'AMZN': 304.12,
    'AAPL': 98.23,
}

minValue = min(zip(stocks.values(), stocks.keys()))
maxValue = max(zip(stocks.values(), stocks.keys()))
sortedDict = sorted(zip(stocks.values(), stocks.keys()))
print(minValue)
print(maxValue)
print(sortedDict)