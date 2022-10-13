# gather values
print("Let's compute your total loan payment with interest. ")
P = input("Principal: ")
r = input("Rate: ")
t = input("Term (Years): ")
n = input("Payments per year:  ")

# convert str to int or float
P = int(P)
r = float(r)
t = int(t)
n = int(n)

# formula for compound interest
A = P * (1 + (r / n)) ** (n * t)
total_interest = A - P

# result
print(f"Total paid after {t} years: {A}")
print(f"Interest paid after {t} years: {total_interest}")
