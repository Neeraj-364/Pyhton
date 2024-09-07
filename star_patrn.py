'''
for n=3
  *
 ***
*****
'''
n=int(input("Enter number: "))
for i in range(1,n+1):
    print(" "*(n-1),end="")
    print("*"*(2*i-1),end="") #end="" ignore by defualt new line
    print("\n")

'''
*  
   
** 
   
***
'''
n2=int(input("Enter number: "))
for i in range(1,n2+1):
   
    print("*"*i,end="") #end="" ignore by defualt new line
    print("\n")
'''
***
* *
***
'''

n3=int(input("Enter number: "))
for i in range (1,n+1):
    if(i==1 or i==n):
        print("*"*n,end="")
    else:
        print("*",end="")
        print(" "*(n-2),end="")
        print("*",end="")
    print("")