def compound_interest(p,r,t):
    return p * ((1 + r/ 100) ** t) - p
p=int(input("Enter principal amount:"))
r=int(input("Enter rate:"))
t=int(input("Enter time:"))
print("Compound Interest is:", compound_interest(p,r,t))