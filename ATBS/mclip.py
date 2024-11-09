#! python3

# A multi-clipboard program

import sys, pyperclip

dict = {'agree':"""Yup, sounds good to me.""",
        'busy':"""Sorry, can we do this later this week or next week?""",
        'upsell':"""Would you consider making this a monthly donation?"""
        }


if len(sys.argv) < 2:
    print('Usage: mclip.py <keyphrase>')
    sys.exit()

keyphrase = sys.argv[1]

if keyphrase in dict:
    pyperclip.copy(dict[keyphrase])
    print(f'Text for {keyphrase} has been copied to your clipboard.')
else:
    print(f'There is no text for {keyphrase}.')


