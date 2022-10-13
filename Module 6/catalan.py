def main():
    for i in range(4, 18):
        #  Print Order 2-15
        print(f"Order {i - 2} Catalan number = {catalan(i)}")


def catalan(sides):
    order = int(sides - 2)
    # Initialize variable of result
    result = 1
    for i in range(2, order + 1):
        # Calculates Catalan number by multiplying previous Catalan number
        result = result * (order + i) / i
    return int(result)


# Run file as script rather than module
if __name__ == "__main__":
    main()
