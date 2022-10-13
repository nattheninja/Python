Name: Nathalie Agustin - nagusti1
Module 4: N-Body Simulation	Due: February 20, 2022 11:59 PM

Approach:
I began with creating all the objects provided directly from the assignment. 
This includes the values for the heavenly bodies as well as some of the static values from the pseudocode.
I placed the planets in a separate list called body. I ommitted the sun because the sun's values do not change during the simulation. 

Within the while loop with a nested for loop, I calculated the radius, force, acceleration, velocity, and positions in the same order recommended on the psuedocode. When calculating the velocity and position, I updated the values from the original body list since we will need to re-use the values from the previous iterations. Lastly, I incremented the elapsed time for the simulation to continue.

Once all values have been updated, I appended the sun list into the body list to match the example output. 

To print the output, I used a nested for loop learned during Office Hours. Individual values are accessed from a list within a list using two index inputs: body[i][j]. I formatted the decimal points of the floats using the assignment reference, and I added a end="" statement that prevented new lines from being created from a print statement using a different online reference. 

Sources:
https://zetcode.com/python/fstring/
https://www.geeksforgeeks.org/print-without-newline-python/

Known Bugs:
Output is printed as expected.

