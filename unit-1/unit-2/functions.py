'''
#defining a function
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

print(add(5, multiply(5,10)))

'''

''''
def print_message():
    print('Hello World')

print_message()
'''
'''
#function with a single argumen4t
def print_msg(message):
    print(message)

#print_msg('Python rocks')

#functions that return a result
def square(value):
    result = value * value 
    return result

answer = square(10)
#print(answer)

print(square(square(3)))

#function with multiple arguments
def greetings(name, job, hobby):
    print(f'Hello {name} your job is {job} and you like {hobby}')

greetings('Eva', 'Student', 'Travelling')
'''

'''
def reverse_list(my_list):
    new_list = []
    #iterate over list in reverse order
    for index in range(len(my_list) - 1, -1, -1):
        #add each element to a new list
        new_list.append(my_list[index])
    #return the reversed list
    return new_list

numbers = [1,2,3,4,5,6,7,8,9,10]

fruits = ['Apple', 'Orange', 'Banana', 'Kiwi']

result = reverse_list(numbers)

print(result)

#print(reverse_list(fruits))
'''
'''
def is_palindrome(word):
    #check if word is the same forwards as backwards
    word = ''
    for i in range(len(word) - 1, -1, -1):
        reversed_word += word[i]
    if word == reversed_word:    
        return True
        
    else:
        return False
        

print(is_palindrome('level'))
'''


    #return True if it is, False otherwise

def reverse_string(my_string):
    reversed_string = ''
    for i in range(len(my_string) - 1, - 1, - 1):
        reversed_string += my_string[i]
    return reversed_string

def is_palindrome(word):
    #check if word is the same forward as backwards
    word_reversed = reverse_string(word)
    if word_reversed == word:
        return True
    return False

print(is_palindrome('level'))

'''
def is_pal(word):
    first, last = 0, len(word) - 1
    while first < last:
        if word[first] != word[last]:
            return False
        first += 1
        last -= 1
        '''








    
 