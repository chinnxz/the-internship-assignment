num = input().split()
k = 0
count = 0
score = 0
result = []
wrong_ans = []
re_str = ""

while(count < 12):
    result.append("_")
    count = count + 1

for c in result:
    re_str = re_str + " " + c
print(re_str)

while(k < 5):
    result_str = ""
    answer = input()
    check = 0
    j = 0
    for i in num:
        if(answer == i):
            result.pop(j)
            result.insert(j,answer)
            score = score + 1
            check = 1
        j = j+1
    if(check == 0):
        wrong_ans.append(answer)
    for n in result:
        result_str = result_str + " " + n
    for m in wrong_ans:
        result_str = result_str + " " + m

    print(result_str)
    k = k + 1

print(score)