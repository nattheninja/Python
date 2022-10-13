points_file = open("points1.txt")

# Initialize variables
num_iterations = int(points_file.readline())
total_patients = int(points_file.readline())
num_clusters = int(points_file.readline())
pending_patients = total_patients - num_clusters
centroids = []
clusters = []
patients = []
cluster_size = []
previous_cluster_sizes = []
iterations = 0  # Iterations till stability

# Prepare nested data structures,
for i in range(num_clusters):
    centroids.append([])
    clusters.append([])
    points = points_file.readline().strip()
    # Convert line to integer and place in centroid list
    point_list = points.split(",")
    centroids[i] = list(map(int, point_list))
print(f"Initial COVID-19 Patients: {centroids}\n")

# Prepare patients for clustering
for i in range(pending_patients):
    patients.append([])
    points = points_file.readline().strip()
    # Convert line to integer and place in patients list
    point_list = points.split(",")
    patients[i] = list(map(int, point_list))

# Necessary values from file have been placed in local variables
points_file.close()

for i in range(num_iterations):
    #  Start each iteration with cluster sizes as 0
    for j in range(num_clusters):
        cluster_size.append(0)
    for j in range(pending_patients):
        centroid_distance = []
        closest = 0
        for k in range(num_clusters):
            # Calculate the shortest distance between patient and centroids
            # delta_x/y is the delta of the x/y components squared
            delta_x = (patients[j][0] - centroids[k][0]) ** 2
            delta_y = (patients[j][1] - centroids[k][1]) ** 2
            centroid_distance.append((delta_x + delta_y) ** (1 / 2))
            closest = centroid_distance.index(min(centroid_distance))
        clusters[closest].append(patients[j])
        cluster_size[closest] += 1

    # Calculate new centroids
    for j in range(num_clusters):
        sum_x = 0
        sum_y = 0
        for k in range(len(clusters[j])):
            sum_x += clusters[j][k][0]
            sum_y += clusters[j][k][1]
        centroids[j][0] = sum_x/len(clusters[j])
        centroids[j][1] = sum_y/len(clusters[j])

    # check if any patients have changed clusters
    if previous_cluster_sizes == cluster_size:
        break
    else:
        # save copy of current cluster sizes for comparison
        previous_cluster_sizes = cluster_size[:]
        # empty clusters
        cluster_size.clear()
        iterations += 1
        clusters.clear()
        for j in range(num_clusters):
            clusters.append([])
            cluster_size.append(0)

print(f"Iterations to achieve stability: {iterations} \n")
print("Final Centroids:")
for i in range(len(centroids)):
    print(f"{centroids[i]}")
print()
for i in range(len(clusters)):
    print(f"Number of patients in Cluster {i}: {cluster_size[i]}")
    print(f"{clusters[i]} \n")
