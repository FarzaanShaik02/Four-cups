
l=["Red","Green","White","Black"]
print("Let's play Four cups I have a message for you...")
print(l)
One="you are so cute"
Two="smile"
Three="Regrets are the best lesson"
Four="All it need is;A change!"
Five="You are doing good,Go ahead with confidence"
Six="Shine until you shine"
Seven="Soul beauty >>> Face beauty"
Eight="Self Love gives you peace;"
user=input("Select a Colour=")
if user=="Red":
     n=input("Select Your choice [One,Three,Seven,Eight]:")
     if n=="One":
         print(One)
     if n=="Three":
         print(Three)
     if n=="Seven":
         print(Seven)
     if n=="Eight":
         print(Eight)
elif user=="Green":
    n=input("Select Your Choice [Two,Three,Six,Four]:")
    if n=="Two":
        print(Two)
    if n=="Three":
        print(Three)
    if n=="Six":
        print(Six)
    if n=="Four":
        print(Four)
elif user=="White":
    n=input("Select Your Choice [Seven,Four,Six,Five]:")
    if n=="Seven":
         print(Seven)
    if n=="Four":
        print(Four)
    if n=="Six":
        print(Six)
    if n=="Five":
        print(Five)
elif user=="Black":
    n=input("Select Your Choice [Two,One,Eight,Four,Five]:")
    if n=="Two":
        print(Two)
    if n=="One":
         print(One)
    if n=="Eight":
         print(Eight)
    if n=="Five":
        print(Five)
    
else:
    print("Enter Appropriate input")
    
    
