#strings:textual data
#tic = 'QAN.AX'
#start same as end "" '' ''' ''' """ """
str = "what's that over there"
#triple for many lines
str1 = '''what is
   that over there'''
str2 = '''John said, "let's learn Python together". '''
#use backlash
#integer & float
import math
#compare equality ==
i = 1
test = i == 1
print(test)
f = 0.2 + 0.2 + 0.2
print(f)
print(f == 0.6)   #===> false  without import math
#boolean
# 1 = 1 false, cannot start as a number
# T & T ==> T   T & F ==> F   F & T ==> F   F & F ==> F
# T or T ==> T    T or F ==> T    F or T ==> T    F or F ==> F
# none means a null value
# upper is not a global function
#x = str('abc')
#xup = str.upper(x)
#print(xup)
#y = 'abc'.upper()
#print(y)
#formation a string
a = True
b = 5
print(f'The value of a is {a} and the value of b is {b}')
print("The value of a is {} and the value of b is {}".format(a , b))   #可以"，也可以'，但是不可以''

#str.strip('c')     去除字符串头部尾部c的字符，regardless order,None和不写，默认去除空格

w = "What"
i = "IS"
c = "CamelCase?"
print('{} {} {}'.format(w, i, c).lower())

x = 1
y = 2
y = x
x = y
print(x)

import datetime
date = datetime.datetime(2021, 1, 1)
print(date)

#str4 = 'very bad idea'
#print(str4)
length = 56
width = 33
height = 30.5
volume = length * width * height
print(f"the volume is {volume} cm.")

#data structure: list tuple set dictionary
#list:can be odered, mutable
lst = [1,2,3]
#index 0 1 2 3...., from back......-3, -2,-1
print(lst[1:3])  #from 1 but 3 not included, 1 and 2
#tuples: immutable
t = ('word', 5, False)
#set: object appears only once
a = {1, 2, 3}   #cannot be empty
# to creat empty set:
#dictionary: appear at once, link keys to values,different key can have same value,key lefy,value right
#dictionay keys immutable
l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
print(l[2:11])
t =('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')
print(l[-7:10])
dic0 = {'a': 1, 'b': 2, 'c': 3}
dic1 = dic0.update({'a': 0, 'd': 4})
#print(dic0[0])
#tup = (1, 2, ['a', 'b'])
#dic = {tup: 'value'}   not valid
tup = (1, 2, ('a', 'b'))
dic3 = {tup: 'value'}
print(dic3)

