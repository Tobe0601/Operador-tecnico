print("1")

def test():
    print("2")

print("3")

test()

print("4")


def weekly_pay(daily, weekly, monthly, rate):
    daily * rate
    weekly = daily * 7
    monthly = weekly * 4
    return daily, weekly, monthly

hours = float(input("How many hours do you work per day?: "))
rate = float(input("How much do you get per hour?: "))

day = print ("This is your income per day: ")
week = "This is your income per week: "
month = "This is your income per month: "

day, week, month = weekly_pay(hours, rate, week, month)

