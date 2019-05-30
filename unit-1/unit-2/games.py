#ask user to guess your secret number

#loop as long as users input is not equal to secret nmber

# print a message if it is equal, then end loop

# if the guess is within 2 of actual answer,(greater or less) print almost there
#if guess is greater or less than secret by 2, print too far 
secret = 7
guess = int(input("Guess my secret number: "))

while guess != secret: 
    print ('Not correct')
    guess = int(input("Guess my secret number: "))
print("Yeah you got it")


