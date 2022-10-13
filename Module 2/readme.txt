Name: Nathalie Agustin	nagusti1
Module 2: Compound Interest		Due: February 6, 2022 11:59 PM

Approach:
After attending the Office Hours session this week and reading the assignment, I went throught the following steps to complete the assignment.

Part 1: 
For each variable in the formula, I created a variables and assigned them to whatever user input was provided. Once the variables were entered and assigned, they had to be converted from a string to a integer/float depending on the formula value. Since Python is strongly typed, I did that. I rewrote the provided formula in terms of the arithmetic operators Python understands to solve for the toal amount paid. To solve for interest, I just subtracted the total with the principal amount and assigned it to a variable. Lastly, I used f-strings to print the final result so that the variables that were integers and floats could still be concatenated in the output.

Part 2:
Prior to any coding, I flexed math skills I have not used in years to solve for the rate of interest from the originally provided formula. 
	A=P(1+(r/n))^(nt)
	A/P=(1+(r/n))^(nt)
	(A/P)^(1/(nt))= 1 + (r/n)
	(A/P)^(1/(nt)) - 1 = r/n
	r = n((A/P)^(1/(nt)) - 1)

Once I had that prepared, I assigned each variable to whatever the user was prompted to input and converted them to the proper data type as I did in Part 1. I rewrote my formula in terms of Python arithmetic operators and used f-strings for the output as I did in Part 1 as well.

The answer for Part 2 will be provided with the screenshots PDF submission.

Known Bugs:
Output is printed as expected.

