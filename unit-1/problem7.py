breakfast = ['Froot Loops', 'Wheaties', 'Cap n Crunch']


for index, meal in enumerate(breakfast):
    last_letter = meal[-1]
    if last_letter == "s":
        breakfast[index] += ' are yummy!'
    else:
        breakfast[index] += ' is yummy!'

print(breakfast)





