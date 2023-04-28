def even_numbers():
    x = range(10)
    for i in x:
        if i % 2 == 0:
          print(i)

def even_numbers():
    x = range(10)
    for i in x:
        if i % 2 != 0:
          print(i) 

def divisible_by_five():
    x = range(30)
    for i in x:
        if i % 5 == 0:
          print("{:}is a divisible of five") 
        else:
          print("{:}is not divisible by five")       


def multiple_comparisons():
    x = range(30)
    for i in x:
        if i % 2 == 0:
            print("{:}is divisible by 2")
        elif i % 3 == 0:
              print("{:}is divisible by 3") 
        elif i % 5 == 0:
              print("{:}is divisible by 5") 
        else:
              print("{:}is not divisible by 2,3 or 5") 

def divisible_by_two_and_three():
    x = range(30)
    for i in x:
        if i % 2==0 and i % 3 == 0:
            print("{:}is divisible by both 2 and 3")
        elif i % 2 ==0 or i % 3 == 0:       
            print("{:}is divisible by both 2 or 3")
        else:
            print("{:}is not divisible by both 2 or 3")


def while_loop():
    x = 1
    while x <10:
            print(x)
            x+=1

def break_statement():
    x = 1
    while x < 10:
        print(x)
        if x == 5:
            break
        x += 1

def continue_statement():
    x = 1
    while x < 10:
          if x%2 != 0:
             continue
        
    print(x)





