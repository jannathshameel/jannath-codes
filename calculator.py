n1=int(input("Enter a number"))
n2=int(input("Enter a number"))
operator=input("Enter operator")
if operator=="+":
    print (n1+n2)
elif operator=="-":
    print (n1-n2)
elif operator=="*":
    print(n1*n2)
elif operator=="/":
    print(n1/n2)
else:
    print("invalid")

