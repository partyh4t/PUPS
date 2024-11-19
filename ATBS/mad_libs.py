
#mad libs

from pathlib import Path
import string

mad_libs = open('C:\\Users\\ray\\OneDrive\\Desktop\\Temporary\\python_scripts\\ATBS\\textfiles\\test-file-1.txt', 'r', encoding='utf-16')

paragraph = mad_libs.read().split()

for i in range(len(paragraph)):
    word = paragraph[i].strip(string.punctuation)
    if word in ('ADJECTIVE', 'NOUN', 'VERB', 'EMOTION', 'PLACE'):
        user_input = input('Enter a(n) ' + word.lower() + ': ')
        paragraph[i] = user_input + paragraph[i][len(word):]
 

paragraph = ' '.join(paragraph)
print(paragraph)
