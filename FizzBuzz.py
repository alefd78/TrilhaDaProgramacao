def fizzbuzz(num):
    num1 = num
    if(num1 % 3 == 0 and num1 % 5 != 0 ):
        return("Fizz")
    elif(num1 % 3 != 0 and num1 % 5 == 0):
        return("Buzz")
    elif(num1 % 3 == 0 and num1 % 5 == 0):
         return("FizzBuzz")
    elif(num1 % 3 != 0)  and (num1 % 5 != 0):
         return(num1)
