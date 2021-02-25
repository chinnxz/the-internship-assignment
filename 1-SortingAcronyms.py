n = int(input())
i = 0
j = 0
k = 1
sentence = ""
caps = []
fin = []

while i<n: #get input from user
    word = input()
    sentence = sentence + "\n" + word
    i = i+1

words = sentence.split("\n")
words.remove("")

def check_cap(words): #check the first character of word
    cap = words.split()
    sent_cap = ""
    result = ""
    for i in cap:
        if(i.istitle() == True):
            sent_cap = i
            result = result + sent_cap[0]
    return result

while j < n:
    word = check_cap(words[j])
    caps.append(word)
    j = j+1

def sortFunc(e):
    return len(e)
caps.sort(reverse=True, key=sortFunc)

while k < len(caps): #sorting the result by length
    if(len(caps[k-1]) > len(caps[k])):
        fin.append(caps[k-1])
    else:
        if(caps[k-1] < caps[k]):
            fin.append(caps[k-1])
        else:
            fin.append(caps[k])
            temp1 = caps[k-1]
            temp2 = caps[k]
            caps.pop(k-1)
            caps.insert(k-1,temp2)
            caps.pop(k)
            caps.insert(k,temp1)
    if(k == len(caps) - 1):
        fin.append(caps[k])
    k = k+1

for i in fin:
    print(i)

