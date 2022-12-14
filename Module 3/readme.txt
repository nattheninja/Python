Name: Nathalie Agustin - nagusti1
Module 3: Luhn's Algorithm		Due: February 14, 2022 11:59 PM

Approach:
Part 1 - Per Lun's algorithm, to verify the identifier I performed the following steps:
1. Accepted user input 
2. Created a variable to track the index length of the input which would establish how many times the for loop would iterate
3. Created a variable to keep track of the running total
4. Started for loop using index length, multiplying every other number in the sequence by 2. The conditional if statement of i%2 handles this. 
5. Any digit greater than 9 is two digits. Using an if statement, any 2-digit number was separated using floor division for the first digit, and modulo for the second digit. Floor division prevents a float from being derived from the integer operands. 
6. All numbers, modified or not modified, are added to the running total
7. Verifying the total is divisible by 10 is accomplished by the checksum =  total % 10. If the result is zero, it is a valid credit card number.
8. Final results concatenated and printed.

Part 2 
Steps 1-3 repeated above.
4. The for loop uses negative indexing and a stride of -1 to iterate the sequence from right to left rather than left to left. 
Steps 5-6 repeated above. 
7. In accordance with the instructions, the check digit is generated by 10 - (total % 10).
8. Final results concatenated and printed.

Known Bugs:
Output is printed as expected.

