from fractions import Fraction


# Constructs recursion tree for given recursion function
def build_tree(function):
    print(f"Recursion Function: {function}")
    start = function.find("(", 16)
    if start == -1:
        nr_cost = function[17:len(function) - 1]
    if function.find("lgn") != -1:
        nr_cost = "lgn"
    else:
        end = function.find(")", start)
        nr_cost = "c" + function[start + 1:end]
    print(nr_cost)
    # Finding value of a and b
    if (function[7]).isnumeric():
        a = int(function[7])
        b = int(function[12])
        if "1" in nr_cost:
            f = "c"
        else:
            f = nr_cost
    else:
        a = 1
        b = int(function[11])
        if "1" in function[16:]:
            f = "c"
        else:
            f = nr_cost

    # if f is a polynomial, extract the degree of the polynomial
    if f.find("^") != -1:
        degree = int(f[f.find("^") + 1:])
    else:
        degree = 1

    print(f"Depth = 0: [T(n) | {f}]\n")
    if function[7:14].find("/") != -1:
        divide_conquer(degree, a, b, f)
    else:
        chip_conquered(degree, a, b, f)


# For recursion functions of the form T(n) = aT(n/b) + f(n)
def divide_conquer(degree, a, b, f):
    for i in range(3):
        print(f"Depth = {i + 1}: ", end="")
        b_update = (b ** (i + 1))
        a_update = (a ** (i + 1))
        for j in range(a_update):
            if degree == 1:
                print(f"[T(n/{b_update}) | {f}(1/{b_update})] ", end="")
            else:
                print(f"[T(n/{b_update}) | {f}(1/{b_update})^{degree}] ", end="")
        print()
        total_cost = Fraction(a_update, b_update ** degree)
        if f == "c":
            print(f"Sum of nonrecursive cost at Depth {i + 1} = {a_update}")
        elif total_cost == 1:
            print(f"Sum of nonrecursive cost at Depth {i + 1} = {f}")
        else:
            print(f"Sum of nonrecursive cost at Depth {i + 1} = {total_cost}{f}")
        print()


# For recursion functions of the form T(n) = aT(n-b) + f(n)
def chip_conquered(degree, a, b, f):
    for i in range(3):
        print(f"Depth = {i + 1}: ", end="")
        b_update = -b * i - b
        a_update = a ** (i + 1)
        for j in range(a_update):
            if f == "c":
                print(f"[T(n{b_update}) | 1]  ", end="")
            if f == "lgn":
                print(f"[T(n{b_update}) | lg(n{b_update})] ", end="")
            elif degree == 1:
                print(f"[T(n{b_update}) | (n{b_update})] ", end="")
            else:
                print(f"[T(n{b_update}) | (n{b_update})^{degree}] ", end="")
        print()
        if f == "c":
            print(f"Sum of nonrecursive cost at Depth {i + 1} = {a ** (i + 1)}")
        elif f == "lgn":
            print(f"Sum of nonrecursive cost at Depth {i + 1} = {a ** (i + 1)}clg(n{b_update})")
        elif degree == 1:
            print(f"Sum of nonrecursive cost at Depth {i + 1} = c(n{b_update})")
        else:
            print(f"Sum of nonrecursive cost at Depth {i + 1}  = c(n{b_update})^{degree}")
        print()


if __name__ == '__main__':
    test_cases = open("test_cases.txt")
    for line in test_cases:
        build_tree(line)
        print("----------------------------------------------")
