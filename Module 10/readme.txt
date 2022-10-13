Name: Nathalie Agustin - nagusti1
Module 10: Debugging K-means Clustering	Due: April 10, 2022 11:59 PM

Approach:
To investigate the found bugs, I did a cursory look to find the easily-identifiable lexical, syntax, and some semantic errors in the code. After I found the easily detectable issues, I investigated the errors to be found from the input file. After those issues were addressed, I finally ran the code to investigate whatever issues the IDE ran into until I was successfully able to run the program to completion. 


Known Bugs:
Bugs that could be identified have been included in nagusti1_mod10.pdf, however there were two significant conflicts from the expected outputs and the received outputs.

The final values of all the errors ended up as follows:
Lexical: 1, Syntax: 1, Semantic: 6, Logical: 12, Input: 2
This is contrary to the expected values given from the assignment instructions, and this is likely due to the interpretation of logical versus semantic errors. I attempted to make the distinction between logical and semantic, but further investigation is probably needed to distinguish between the two to address this discrepancy. 

The second discrepancy is a result of the outputs. The example output provided with the assignment includes 100 points distributed across the 4 clusters when in the original assignment, the original centroid clusters were not included. Only 96 values were divided across the 4 clusters. Because of this, my final centroid results do not match the received input. To address this, I would probably re-add the first COVID patient centroids. 