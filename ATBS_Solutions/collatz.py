
while True:
    try:
        number = int(input("Enter your number: "))
        break
    except:
        print("Please enter an integer.")

def collatz(number):
    while number > 1:
        if number % 2 == 0:
            number = number // 2
            print(number)
        elif number % 2 == 1:
            number = 3 * number + 1
            print(number)

collatz(number)
