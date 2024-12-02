
import sys

my_list = []

while True:
    try:
        food = input('\nEnter your desired fruit or vegetable: \nEnter \"Done\" when finished. \n')
        if food.isdigit():
            print("Please enter a valid fruit or vegetable.")
        elif food == "Done":
            break
        else:
            my_list.append(food)
    except KeyboardInterrupt:
        sys.exit()

        
def stringer(list):
    string = ''
    if list:
        for i in list:
            if len(list) == 1:
                print(i)
            elif i == list[-1]:
                string += 'and ' + i
            else:
                string += i + ', '
        print(string)
    else:
        print("You've provided an empty list!")


stringer(my_list)
