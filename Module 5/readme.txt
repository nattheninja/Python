Name: Nathalie Agustin - nagusti1
Module 5: K-means Clustering	Due: February 27, 2022 11:59 PM

Approach:
1. Opened given file (points1.txt OR points2.txt)
2. Assigned file values for number of iterations, patients, and clusters to local variables. Calculated number of patients that needed to be clustered. 
3. Created variables for needed lists, cluster sizes, and number of iterations until stable
4. Created frame of nested data structures for centroids and clusters. 
Grabbed centroid points from file, split the x and y components, converted them to integer values, and placed them into the nested centroid list.
6. Split the x and y components of the remaining patients, converted them to integer, placed them in nested patient list. 
7. Closed file since all needed values were stored in lists
8. Began clustering by ensuring the size of the clusters started at 0
9. Compared distance of remaining patients in the list to centroids using the distance formula. All distances were placed in a list. The index of the smallest distance was the index of the cluster the patient would be placed in. The size of that cluster is incremented by one. 
10. After all patients are placed in clusters, a new centroid is calculated by finding the mean of each cluster's x and y components. The sum of all x/y components of a specific cluser is divided by the size of that cluster.
11. If the cluster sizes are the same from the previous iteration, quit the for loop. 
12. If the cluster sizes are not the same, copy over the cluster_size values to previous_cluster_sizes variable to store for later comparison. Increment iterations until stable by 1, clear all contents of cluster and cluster_size. 
13. Loop continues until previous cluster size and current cluster size are the same. 
14. Final results are printed to match given output 

Sources:
https://www.w3schools.com/python/ref_string_split.asp
https://www.geeksforgeeks.org/python-map-function/

Known Bugs:
Lines 60 and 61 will raise a warning but the program will still run. This is because line 22 maps the centroids as an integer rather than a float. I left the centroids as integers initially to print them as close as possible to the expected output. To remove these warnings, line 22 may be re-written centroids[i] = list(map(float, point_list)). 

Question Answers:
a.) The number of k-means is inefficient in terms of the number of overall iterations because the maximum number of iterations is provided. With this information provided, we can iterate to the maximum number and still get the expected final outcomes. To address this, I put a break statement once stability is achieved, but you can do this also by creating a while loop. The condition of the while loop would iterate until no changes in the cluster size from the previous iteration is detected. 
b.) This implementation may also yield incorrect answers because we are only iterating until the cluster sizes are unchanged. We are not verifying that the points in those clusters are actually the same as the previous iteration. There is a chance, that the size of the cluster remained the same, but the points did change. This can be fixed by maintaining a nested data structure with the previous cluster contents, and comparing it with the current clusters to inspect all elements are the same. 