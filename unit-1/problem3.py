#how i did it 
'''
user_entry = input('Enter a word or sentence please:\n')

for character in reversed(user_entry):
    print(character, end="")
'''
#strings are immutable
'''
my_string = 'This is a sentence'
reversed_string = ''
for i in range(len(my_string) - 1, -1, -1):
    reversed_string += my_string[i]

print(reversed_string)
'''


my_string = 'This is a sentence'

for i in range(len(my_string) - 1, -1, -1):
    print(my_string[i], end='')