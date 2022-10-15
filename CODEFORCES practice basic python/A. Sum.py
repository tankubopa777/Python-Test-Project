x = int(input())
listnum = []

def cheacknum(number):
    if number[0] + number[1] == number[2]:
        return "YES"
    elif number[1] + number[2] == number[0]:
        return "YES"
    elif number[0] + number[2] == number[1]:         
        return "YES"
    else :
        return "NO"
        
for i in range(x):
    num = str(input())
    num = num.split()
    number = [int(i) for i in num]
    listnum.append(cheacknum(number))
for i in listnum:
    print(i)


        

    