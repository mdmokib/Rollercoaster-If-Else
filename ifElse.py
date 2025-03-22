print("Welcome to the rollercoaster")

height=float(input("Enter your height: "))


if height > 120:
    print("You can ride")
    age=int(input("Enter your age :"))
    if age<12:
         print("Pay $5.")
    elif age <=18:
         print("Pay $7.") 
    else:
         print("pay $12.")               
else:
     print("You can not ride")
