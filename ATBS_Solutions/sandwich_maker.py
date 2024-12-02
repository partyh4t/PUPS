
# sandwich maker

import pyinputplus as pyip

breads = {
    'white': 3.15,
    'wheat': 3.15,
    'sourdough': 4.00
}

proteins = {
    'chicken': 5.15,
    'ham': 5.30,
    'turkey': 5.20,
    'tofu': 6.00
}

cheeses = {
    'mozarella': 1.75,
    'cheddar': 1.00,
    'american': 1.00,
    'swiss': 1.50
}

total = 0

bread_choice = pyip.inputMenu(list(breads.keys()))
total += breads[bread_choice]
protein_choice = pyip.inputMenu(list(proteins.keys()))
total += proteins[protein_choice]
with_cheese = pyip.inputYesNo('With cheese? ')

if with_cheese == 'yes':
    cheese_choice = pyip.inputMenu(list(cheeses.keys()))
    total += cheeses[cheese_choice]

print('Your total is $' + str(total))