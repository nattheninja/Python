cc_id = input("Enter identifier: ")
id_length = len(cc_id)
total = 0

# parse sequence, <stride> -1 to iterate in reverse order
for i in range(-1, -id_length - 1, -1):
    current = int(cc_id[i])
    # For every other number, multiply by 2
    if i % -2 == -1:
        current = current * 2
        # If product is 2-digits, add digits together
        if current > 9:
            current = (current // 10) + (current % 10)
    total = total + current

check_digit = 10 - (total % 10)
print(f"The valid credit card number is: {cc_id}{check_digit}" + \
      f" and the newly computed check digits is: {check_digit}")
