daily_balances=[107.92, 108.67, 109.86, 110.15]
show_balances(daily_balances)

def show_balances(daily_balances):
 # do not include -1 because that slice will only have 1 balance, yesterday
 x=len(daily_balances)
 for day in range(x-3,x-1):
  balance_slice = daily_balances[day : day + 2]
  # use positive number for printing
  days_ago=x-day
  print("slice starting %d days ago: %s" % (abs(day), balance_slice))
