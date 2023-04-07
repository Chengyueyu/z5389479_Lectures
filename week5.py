s = "This is my test String"
def process_string(s):
    words = s.split()
    #"for a in words:
         #if words.index(a) % 2 == 0:
             # words[words.index(a)] = words[words.index(a)].lower()
         #else:
            # words[words.index(a)] = words[words.index(a)].upper()
    #return words"
    for i in range(len(words)):
        if (i+1)%2 == 0:
            words[i] = words[i].upper()
        else:
            words[i] = words[i].lower()
    return words
print(process_string(s))

def process_string(s):
    words = s.split()
    for a, word in enumerate(words):
        if a % 2 == 0:
            words[a] = words.lower()
        else:
            words[a] = words.upper()
    return words

def fizz_buzz_sumz(i):
    sum = 0
    for x in range(i, i+1):
        if x % 3 == 0 and x % 5 == 0:
            continue
        elif x % 3 == 0:
            sum += 3 * x
        elif x % 5 == 0:
            sum += 5 * x
        else:
            sum += x
        return sum