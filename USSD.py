
#start with greeting
greet = int(input("Good day! What service do you require: \n1: Withdraw \n2: Transfer \n3: Airtime recharge \n4: Data subscription "))
print("How much?")
amount = int(input("1: #200 \n2: #500 \n3: #1000 \n4: #1,500 \n5: #2,000 "))
print("To last for how long?")
duration = int(input("1: 24 hours \n2: 1 week \n3: 1 month \n4: 1 year "))
print("Are you sure?")
confirm = int(input("1: Yes \n2: No "))
print("TRANSACTION SUCCESSFUL!")