import math
days = 375
weeks = days/7

print("total days:",days)
daysrem = days % 365
years = math.floor(days/365)
days = daysrem
daysrem = daysrem % 7
weeks = math.floor(days/7)
print("years:",years," weeks:",weeks,"days:",daysrem)
