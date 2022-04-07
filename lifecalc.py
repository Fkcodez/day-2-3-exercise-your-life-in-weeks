# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
ageint = int(age)
death = 90
daysleft = (death - ageint) * 365
monthsleft = (death - ageint) * 12
weeksleft = (death - ageint) * 52


print(f"You have {daysleft} days,  {weeksleft} weeks, and {monthsleft} months left.")

#solution
#years = 90 - int(age)
#months = round(years * 12)
#weeks = round(years * 52)
#days = round(years * 365)

#print(f"You have {days} days, {weeks} weeks, and {months} months left.")
