import random
def main():
    random_number = random.randint(1, 100) 
     
    tries = 0
    while True:
        try:
            user_input = int(input("Enter your guess"))
        except Exception as e:
            print(f"entered input wasn't integer {e}")
        if(user_input == random_number):
            break
        if(user_input > random_number):
            print("Too high")
            tries = tries + 1
        elif(user_input < random_number):
            print("Too low")
            tries = tries + 1
    
    print(f"you won the game in {tries} tries")

main()


