my_string = 'This is a sentence'
reversed_string = ''
for i in range(len(my_string) - 1, -1, -1):
    reversed_string += my_string[i]

print(reversed_string)

#print(reversed_string) - more compact way of doing it 

print(''.join(reversed(my_string)))
