#Write a function that uses while, if and continue statements to print all the even numbers between 0 and 50. 
def even_numbers():
    x = 1
    while x < 50:
        x += 1   
        if x % 2 != 0:
           
           continue
        print(x)
     
#Write a function that takes an integer argument and prints "Prime" if the number is prime, and "Not prime" if the number is not prime.

def is_prime(x):
    if x <= 1:

        print("Not prime")

        return
    
    i = 2
    while i*i <= x:
        if x % i == 0:
            print("Not prime")
            return
        i += 1
    print("Prime")

#Write a function that takes a list of integers as input and prints the sum of all the even numbers in the list.
def sum_even_numbers(numbers):
    total = 0
    
    for num in numbers:
        if num % 2 == 0:
            total += num
    print(total)

#Write a function that takes any two integers as input, and prints the sum of all the numbers between the two integers (inclusive) that are divisible by 3.
def sum_divisible_by_three(start, end):
    total = 0
    
    for num in range(start, end+1):
        if num % 3 == 0:
            total += num
    
    print(total)
