#sorting the prime and non-prime number

#start = int(input("enter the starting range:"))
#end = int (input("enter the end range:"))

for i in range (0, 21):
    
    count =0
    
    for j in range (1,i+1):
        
        if(i%j==0):
            
            count +=1
            
    if(count == 2):
        
        print("the prime number between 0 and 21 are:",i)


for k in range (0,21):

    count = 0

    for l in range (2,k):

        if(k%l == 0) :

            count +=1

            print("non-prime numbers are:",k)
            break
            
    
        



   
            
