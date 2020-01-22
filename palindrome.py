p1.py:
#This is the first file, which takes the input from the user:
def takeInput():
    num=int(input("Enter a number to check whether it is a palindrome number or not. "))
    return num
    
   
p2.py:
#This is the second file, which contains the main code
import p1
def palindrome(number):
    temp=number
    rev=0
    while(number>0):
        dig=number%10
        rev=rev*10+dig
        number=number//10
    if(temp==rev):
        return True
    else:
        return False
        
        
   p3.py:
#This file will show the output:
from p1 import takeInput
from p2 import palindrome
if palindrome(takeInput()):
    print("Yes,the number is a palindrome number.")
else:
    print("It is not a palindrome number.")
