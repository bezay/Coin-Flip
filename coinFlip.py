
import random

num  = random.randint(0,1)

input =str.lower(input("Head or Tail ?"))

if(input =="head" and num > 0.5):
    if(num > 0.5):
        print ("You Win 👍")

    elif(num == 0.5):
        print("Coin in Middle")
    else:
        print("You Loose 👎")

elif(input =="tail"):
    if(num < 0.5):
        print("You Win 👍")

    elif(num == 0.5):
        print("Coin in Middle")
    else:
        print("You Loose 👎")

else:
    print("Invalid input")

