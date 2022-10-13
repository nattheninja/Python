def main():
    # Call first 10 rows of Pascal's triangle
    for i in range(1, 11):
        # str converts given output list to string
        # join and map combines elements separated by spaces
        print(" ".join(map(str, pascal(i))))


def pascal(n):
    # Base case, for only first row
    if n == 1:
        return [1]
    else:
        # Beginning of row always 1
        current_row = [1]
        # Get previous row through recursive call
        previous_row = pascal(n - 1)
        # Iterate until elements from previous row are exhausted
        for i in range(len(previous_row) - 1):
            # Sum of adjacent elements from previous row is appended to new row
            current_row.append(previous_row[i] + previous_row[i + 1])
        # End of row always 1
        current_row += [1]
    return current_row


# Run file as script rather than module
if __name__ == "__main__":
    main()
