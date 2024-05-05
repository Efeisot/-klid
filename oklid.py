 # Create a list called 'points' containing tuples representing points in 2D space
points = [(1, 2),(7, 8)]

# Define a function for calculating Euclidean distance between two points
def euclideanDistance(point1, point2):
    return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)**0.5

# Calculate Euclidean distance between each pair of points in the 'points' list
distances = []
for i in range(len(points)):
    for j in range(i+1, len(points)):
        distances.append(euclideanDistance(points[i], points[j]))

# Find the minimum distance from the 'distances' list and print it
min_distance = min(distances)
print(f"The minimum distance between points is: {min_distance}")
