list_1 = [1, 2, 3, 4]
list_2 = [2, 3]

def list_intersection(list_1, list_2):
    new_list = []
    for item in list_1:
        if item in list_2:
            new_list.append(item)
    return new_list

print(list_intersection(list_1, list_2))

var = 3

def item_count(var, list_1):
    count = 0
    for item in list_1:
        if item == var: 
            count = count + 1
    return count

print(item_count(var, list_1))