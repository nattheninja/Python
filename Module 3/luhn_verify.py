cc_num = input("Enter credit card number: ")
cc_length = len(cc_num)
total = 0

for i in range(cc_length):
    current = int(cc_num[i])
    # for every other number in sequence, multiply by 2
    if i % 2 == 0:
        current = current * 2
        # if product is 2-digits, add digits together
        if current > 9:
            current = (current // 10) + (current % 10)
    total = total + current

checksum = total % 10
print(f"Checksum = {checksum}")
if checksum == 0:
    print(f"{cc_num} is a valid CC number")
else:
    print(f"{cc_num} is an invalid CC number")
