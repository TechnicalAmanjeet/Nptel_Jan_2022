# idea is to take => cost and discount from user => as an output return cost after subtracting discount prize.

print("Hii, I hope you are doing well. let me compute the discount for you!!!")
total_cost = int(input("What is total cost : "))
discount = float(input("Enter discount ( in % ) : "))

cost_after_discount = total_cost - ( total_cost * ( discount / 100))

print(f"You have to pay Rs. {cost_after_discount} .")

print("\n ***** hay! Enjoy your day. *****")
