def healthCalculator(age, applesAte, cigsSmoked):
    answer = (100-age) + (applesAte * 3.5) - (cigsSmoked * 2)
    print(answer)

ethansData = [15, 10, 0]


healthCalculator(ethansData[0], ethansData[1], ethansData[2])
# Takes list, and passes each item in one at a time instead of having to write each
healthCalculator(*ethansData)