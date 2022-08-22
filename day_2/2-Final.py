age = input("What is your current age? ")
age = int(age)
days = (90 * 365) - (age * 365)
weeks = (90 * 52) - (age * 52)
months = (90 * 12) - (age * 12)
print(f"You have {days} days, {weeks} weeks and {months} months left.")


# 강의 풀이
age = input("What is your current age? ")
age_as_int = int(age)

years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

print(f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left")