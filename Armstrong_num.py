print("This program checks whether the given program is armstrong or not.")

A = input("Enter any number : ")
G = int(0)

for i in A:
    C = pow(int(i),3)
    G = G + C

if G == int(A):
    print(A + " is a armstrong number.")
else :
    print(A + " is not a armstrong number.")
    
    
    #This has a range from 1 to 999
