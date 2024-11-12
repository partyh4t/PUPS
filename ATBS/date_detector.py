
import re

# Date Format Detector

date_input = input("Enter date here: (Format: DD/MM/YYYY) ")


def dateRegex(date):
    regex = re.compile(r'([0-3][0-9])/([0-1][0-9])/([1-2][0-9]{3})')
    day = regex.search(date).group(1)
    month = regex.search(date).group(2)
    year = regex.search(date).group(3)
    
    if day[0] == '3' and int(day[1]) > 1:
        print('False date!')
        return
    if month == '02' and int(year) % 4 != 0 and int(day) > 28:
        print(f'{year} is not a leap year to have 29 days during {month}!')
        return
    if month in ['04', '06', '09', '11'] and int(day) > 30:
        print(f'{month} does not have 31 days!')
    else:
        print('Valid Date!')
    

dateRegex(date_input)
