#Even/odd & Positive/Negative checker........
number=int(input("choose a number : "))
if number > 0 :
    print("number is positive : ")  
    if number % 2 == 0 :
        print("number is even ")
    else:
        print("number is odd")  
        
elif number < 0 :
    print("number is nevative : ")
    if  number % 2 == 0 :
        print("number is even ")
    else:
        print("number is odd") 
        
else:
    print("number is zero") 
    
