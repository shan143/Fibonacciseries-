import math

def fibonacciSeries(n):
    '''
    (int) -> list
    n: the number of fibonacci sequence terms to be generated, a positive integer
    
    Returns a list of the first n Fibonacci numbers
    '''    
    #Making sure that the input is a positive integer. Else, return an AssertionError
    assert type(n) == int and n>=1, "Please enter a positive integer"      
    fibonacciList = []
    
    if n == 1:
        fibonacciList = [0]
    else :
        firstNum = 0        #Initializing the first term in Fibonacci Sequence
        nextNum = 1         #Initializing the next term in Fibonacci Sequence
        ans = 0             #Temporary variable ans
        fibonacciList = [0,1]
        for i in range(n-2): #Generating the list of fibonacci numbers
            ans = firstNum + nextNum
            firstNum = nextNum
            nextNum = ans
            fibonacciList.append(nextNum)
    return fibonacciList
    

def prime(num):
    '''
    (int) -> boolean
    num: a positive integer
    
    Returns True if the number is a prime number. Returns False otherwise"
    '''
    assert type(num) == int and num>=0, "Please enter a positive integer"  #Not necessary for the current program,
                                                                         #but may be helpful if the function is reused elsewhere
    if num == 1:
        return False
    
    if (num!=2) and (num%2 == 0):  #Prime number check for 2 and even numbers
        return False
    
    for i in range(3,int(math.ceil(math.sqrt(num)))+1,2):  #Prime number check for numbers greater than 2
        if num%i == 0:                                     #Optimized by checking division only by odd numbers
            return False                                  #upto square root of input 
    return True

                
def F(n):
    '''
    (int) -> int/str
    n: the number of fibonacci sequence terms to be generated, a positive integer
    
    Iterates throught the list generated by the function fibonacciSeries(n) and prints "Buzz" if the number is divisible by 3, 
    "Fizz" if number is divisible by 5, "BuzzFizz" if the number is prime and prints the number itself otherwise
    '''
    assert type(n) == int and n>0, "Please enter a positive integer"  #Not necessary for the current program,
                                                                         #but may be helpful if the function is reused elsewhere
    for number in fibonacciSeries(n):
        isPrime = prime(number)       #This step is done to reduce the number of calls to the function prime
        if number%3 == 0:
            print "Buzz"
        if number%5 == 0:
            print "Fizz"
        if isPrime == True:
            print "BuzzFizz"
        if (number%3 != 0) and (number%5 != 0) and (isPrime == False):
            print numberobbiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiibbbbbbbbbiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiibgggo;n
