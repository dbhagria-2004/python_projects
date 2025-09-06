import random
def main():
    while True:
        user_input = input("Do you want to play? (Y/N)")
        if(user_input == "Y"):
            num1 = random.randint(1, 6)
            num2 = random.randint(1,6)
            print(f"num1:{num1}, num2: {num2}")
        elif(user_input == "N"):
            print("thankyou for playing")
            break
        else:
            print("please enter a correct input")

main()