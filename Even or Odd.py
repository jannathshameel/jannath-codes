number=int(input("Enter number"))
if number%2==0:
    print("EVEN")
else:
    print("ODD")
progress=input("DO YOU WANT TO CONTINUE? TYPE YES/NO")
while progress=="yes":
    newnumber=int(input("Enter a new number"))
    if newnumber%2==0:
        print("EVEN")
    else:
        print("ODD")
    progress=input("DO YOU WANT TO CONTINUE? TYPE YES/NO")
print("END")
