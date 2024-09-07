#write tables
n=int(input("Enter a number: "))

for i in range (1,11):
    print(f"{n}x{i} = {n*i}")
#
l=["Harry","Sonu","Shubham","Sangita","Neeraj"]
for name in l:
    if(name.startswith("S")):
        print(f"Hello {name}")