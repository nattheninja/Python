# gather values
print("Let's compute your interest rate.")
P = input("Principal: ")
A = input("Total: ")
t = input("Term (Years):  ")
n = input("Payments per year: ")

# convert str to int or float
P = int(P)
A = float(A)
t = int(t)
n = int(n)

# formula for compound interest
r = n * ((A / P)**(1 / (n * t)) - 1)

# result
print(f"The interest rate for {P} that cost {A} over {t} years is: {r} ")
