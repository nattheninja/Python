Name: Nathalie Agustin - nagusti1
Module 6: Mathematical Sequences	Due: March 6, 2022 11:59 PM

Approach:
Catalan.py
- Define main method to call catalan function
- Ensure file itself is run as script rather than module
- Define catalan method
- Calculate Order by inputted sides - 2
- Create variable for result
- Iterate through order, previous result always multiplied to new result
- Return result and ensure main prints 

Pascal.py
- Define method to call pascal function to generate first 10 rows of Pascal's triangle
- Ensure file itself is run as script rather than module
- Define pascal method
- Create base case for the first row to return 1
- If not base case, create new row which always starts as 1
- Store previous row results by having pascal call itself with the previous row n-1
- Iterate until elements from previous row are exhausted 
- With the previous row, add the adjacent elements above the current row element
- Append sum as new element of current row
- Last element of row is always 1, append to end of row
- Return current row

Known Bugs:
File does not run without statement if dundername == dundermain. 
Must keep statement in both Python files. 