def calculate_pay(hours_per_day, hourly_rate):
    """Return daily, weekly, and monthly pay based on hours/day and rate/hour."""
    daily = hours_per_day * hourly_rate
    weekly = daily * 7
    monthly = weekly * 4
    return daily, weekly, monthly


# --- Program starts here ---
hours = float(input("How many hours do you work per day? "))
rate = float(input("How much do they pay you per hour? "))

daily_pay, weekly_pay, monthly_pay = calculate_pay(hours, rate)

print(f"Your daily payment is: ${daily_pay: .2f}")
print(f"Your weekly payment is: ${weekly_pay: .2f}")
print(f"Your monthly payment is: ${monthly_pay: .2f}")

if weekly_pay >= 1000:
    print("You're ok in California")
else:
    print("Better you get another job, baboon")
      