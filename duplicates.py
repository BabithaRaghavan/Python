# Removes duplicates in a list

numbers = [2,2,5,6,3,6,8,9,7,8,4]
uniques =[]

for number in numbers:
    if number not in uniques:
        uniques.append(number)

print(uniques)
