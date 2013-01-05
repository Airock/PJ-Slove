def isPalindrome(value):
    return value== int(str(value)[::-1])

count=0
for i in range(1,10001):
    data=i
    for j in range(50):
        data+=int(str(data)[::-1])
        if isPalindrome(data):
            break
    else:
        count+=1

print count


