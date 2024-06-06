"""
Enter your billing amount = 

50000 above -> 40% discount
40000 - 49999 -> 30% discount
20000 - 39999 -> 20% discount
0-19999 -> 0% discount

------
Enter your billing amount = 100000
You got 40% discount
Your final bill is 60000.


Enter your billing amount = 20000
You got 20% discount
Your final bill is 16000.
"""

bill_amount=int(input("Enter billing amount = "))

if bill_amount>=50000:
    discount=40
elif bill_amount>=40000 and bill_amount<=49999:
    discount=30
elif bill_amount>=20000 and bill_amount<=39999:
    discount=20
else:
    discount=0

print(f"You got {discount}% on your bill")
final_bill=bill_amount - (bill_amount*discount/100)
print(f"Your final bill is {final_bill}")
    