n=5
for i in range(n):
   for j in range(n):
      print("*",end=" ")
   print()
##################
n=5
for i in range(1,n+1):
    for j in range(i):
        print("*",end=" ")
    print() 

############
n=5
for i in range(n,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()           
#########
# n=5
for i in range(1,n+1):
    for k in range(n-i):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    print() 
#########
# n=5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(2*i-1):
        print("*",end=" ") 
    print()   
#######diamond
n=5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(2*i-1):
        print("*",end=" ") 
    print() 
for i in range(n-1,0,-1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(2*i-1):
        print("*",end=" ")   
    print()                        
#hollow pyramid
n=5
for i in range(n):
    for j in range(n-i-1):
        print(" ",end=" ")
    for k in range(2*i+1):
        if k==0 or i==n-1 or k==2*i :
            print("*",end=" ")
        else:
            print(" ",end=" ") 
    print()                  
#hollow inverted pyramid
n=5
for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(2*i-1):
        if k==0 or i==n or k==2*(i-1):
            print("*",end=" ")
        else:
            print(" ",end=" ") 
    print()                  
#hollow diamond
n=5
for i in range(n):
    for j in range(n-i-1):
        print(" ",end=" ")
    for k in range(2*i+1):
        if k==0 or k==2*i :
            print("*",end=" ")
        else:
            print(" ",end=" ") 
    print()       
for i in range(n-1,0,-1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(2*i-1):
        if k==0  or k==2*(i-1):
            print("*",end=" ")
        else:
            print(" ",end=" ") 
    print()                  
#hollow square
n=5
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")    
    print()  
#hollow triangke
n=5
for i in range(1,n+1):
    for j in range(i):
        if j==0 or i==n or j==i-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")    
    print()     