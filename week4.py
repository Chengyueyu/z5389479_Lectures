#functions def keyword
#def func_name (para):
    #function body
    #return
def qan_tic():
    tic = "QAN.AX"
    print(tic)
    return tic   #will produce a result
#res = qan_tic()
#print(res)
qan_tic()

def qan_tic():
    tic = "QAN.AX"
    return tic
    print(tic)    #will not be produce since any thing after return will not be excuted

#print(QAN.AX)   give the location
def qan_tic():
    tic = "QAN.AX"
    print(tic)
    return tic
# print (tic) no global define, error
#local scope avalible inside the region
#legb

list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 22, 23, 25, 29, 30, 31]
def even_number(list):
    even = []
    for n in list:
     if n % 2 == 0:
         even.append(n)
    return even
print(even_number(list))
#dic pairs.append

list1 = [2, 3, 10, 14, 20, 21, 25, 13, 15]
def new_list(list1):
    greaterthan = []
    for a in list1:
        if a ** 2 > 150:
            greaterthan.append(a)
    return greaterthan
print(new_list(list1))

lst = [2, 3, 10, 14, 20, 21, 25, 13, 15]
new_list1 = [c for c in lst if c ** 2 > 150]
print(new_list1)

numbers = [0, 1, 1, 2, 5, 6, 8, 2, 4, 6, 8]
new_number = [b for b in set(numbers) if b % 2 == 0]
print(new_number)

print("the value of_name_ is '{__name__}'")

s = "This is my test String"
 def process_string(s):
     words = s.split()
     words = s.lower()
     return words
