name=input("Enter your name:")
print(f"Good Afternoon {name}")

print("Good Afternon "+name)

#problem 2
letter=''' Dear <|Name|>,You are selected! <|Date|>'''
print(letter.replace("<|Name|>","Neeraj").replace(" <|Date|>","24 March 2024"))
#pro3-check double space detect
n="harry is a good  boy"
print(n.find("  "))#if ouput is -1 then no double space is present
print(n.find("good"))
#problem4--replace double space to single space
print("replace double space to single space",n.replace("  "," "))
 
 