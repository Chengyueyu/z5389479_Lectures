lst1 = ['a']
#print(f'this is lst1:{lst1}')
lst1.append('c')
print(lst1)

#if statement
#none false 0 empty strings
#is identical symbol, == compare equal
#else statement,elif statement
#input(name = 'who are you')
#print('welcome to class, name')
#working_hours = input('your_working_hours')
#if working_hours <= '35':
    #print(float(working_hours) * 51.45)
#else:
    #print(float(working_hours) * 88.9)
#loop:for in
#range(start, stop[, step])

number = [3, 9, 1, 5, 7, 2, 11, 0, 3, 12, 3, 15]
max = number[0]
for largest_number in number:
    if largest_number > max:
        max = largest_number
print(max)

a = [1, 2, 3]
for i in a:
    for j in a:
        if i <= j:
    print(i, j)



