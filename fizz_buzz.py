print('This is the program of fizz buzz')
number = int(input('Enter a number: '))
def fizz_buzz(number):
     if (number%3==0) and (number%5==0):
          print('FizzBuzz')
     elif (number%5==0):
          print('Buzz')
     elif (number%3==0):
          print('fizz')
     else:
          print('Just a number')

fizz_buzz(number)
