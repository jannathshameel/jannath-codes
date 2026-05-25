password=input("Enter password")
while len(password)<8:
    print("WEAK. MORE STRONGER")
    password=input("Enter password")
    if len(password)>=8:
        print("STRONG")
