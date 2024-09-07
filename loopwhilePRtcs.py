#write tables
n=int(input("Enter a number: "))
i=1
while (i<11):
    print(f"{n}x{i} = {n*i}")
    i=i+1

#prime or not
for i in range(2,n):
    if(n%i)==0:
        print("Number is not prime")
        break
else:
    print("Number is prime")
#sum of n natural no.
j=1
sum=0
while(j<=n):
    sum +=j
    j +=1

print(sum)  
