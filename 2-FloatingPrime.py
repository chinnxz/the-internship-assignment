x = float(input())
num_str = []

def isPrime(num) :
    if num > 1:
        for i in range(2, num):
            if ((num % i) == 0):
                return False
        return True
    else:
        return False

while(x != 0.0):
    x_str = str(x)
    num_str = x_str.split(".")
    if(len(num_str[1])>3):
        temp = num_str[1]
        #case 1
        num_str.pop(1)
        num_str.insert(1,temp[0:1])
        full_str = num_str[0] + num_str[1]
        cal_num = int(full_str)
        if(isPrime(cal_num) == True):
            print("TRUE")
        else:
            #case2
            num_str.pop(1)
            num_str.insert(1,temp[0:2])
            full_str = num_str[0] + num_str[1]
            cal_num = int(full_str)
            if(isPrime(cal_num) == True):
                print("TRUE")
            else:
                #case3
                num_str.pop(1)
                num_str.insert(1,temp[0:3])
                full_str = num_str[0] + num_str[1]
                cal_num = int(full_str)
                if(isPrime(cal_num) == True):
                    print("TRUE")
                else:
                    print("FALSE")
    else:
        full_str = num_str[0] + num_str[1]
        cal_num = int(full_str)
        if(isPrime(cal_num) == True):
            print("TRUE")

    x = float(input())