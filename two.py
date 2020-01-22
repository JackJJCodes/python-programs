import one 
def armstrong(num):
    length = len(str(num))
    sum = 0
    temp = num
    while(temp != 0):
	    sum = sum + ((temp % 10) ** length)
	    temp = temp // 10
    if sum==num:
        return True
    else:
        return False
