print("Welcome to the rollercoaster")

height=float(input("Enter your height: "))

bill=0

if height > 120:
    print("You can ride")
    age=int(input("Enter your age :"))
    if age<12:
         bill=5
    elif age <=18:
         bill=7
    else:
         bill=12 
    want_photo=input("Do you want to take photo? for YES = Y and No = N")  

    if want_photo== "Y":
       bill +=3

       print(f"Your final bill is ${bill}")                  
else:
     print("You can not ride")
