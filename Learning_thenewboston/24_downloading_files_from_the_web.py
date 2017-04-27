from urllib import request

goog_url = "http://chart.finance.yahoo.com/table.csv?s=GOOG&a=2&b=23&c=2017&d=3&e=23&f=2017&g=d&ignore=.csv"

def downloadStockData(csvUrl):
    response = request.urlopen(csvUrl)
    csv = response.read()
    csvStr = str(csv)
    lines = csvStr.split("\\n")
    destUrl = r"goog.csv"
    fx = open(destUrl, "w")
    for line in lines:
        fx.write(line + "\n")
    fx.close()

downloadStockData(goog_url)

