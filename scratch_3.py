def calcCharge(elapsedTime):
    hours = elapsedTime.seconds/3600
    days = elapsedTime.days
    if(days >= 1):
        dayFee = days * 10

    if(hours >= 1 and hours <5):
        hourFee = hours * 2
    elif(hours >= 5):
        hourFee = 10

    totalFee = dayFee + hourFee
    totalFee = "%.2f" % totalFee

    return totalFee