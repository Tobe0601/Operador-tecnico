print("1")

def test():
    print("2")

print("3")

test()

print("4")


def weekly_pay(hours_per_day,rate):
    return hours_per_day * rate * 7

hours = float(input("How many hours do you work per day?: "))
rate = float(input("How much do you get per hour?: "))

result = weekly_pay(hours, rate)

print(result)