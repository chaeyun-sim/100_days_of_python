print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
tips = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
split_people = int(input("How many people to split the bill? "))

tips_calculate = total_bill / 100 * tips
result = (total_bill + tips_calculate) / split_people
result_round = round(result, 2)

print(f"Each person should pay: ${result_round}")


# 강의 풀이
#tips_calculate 로 하지 말고 1.12를 곱하기
(total_bill / split_people) * 1.12

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill?"))

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount}")