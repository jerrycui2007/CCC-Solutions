# https://dmoj.ca/problem/ccc20s1
number_of_observations = int(input())

positions = []
for _ in range(number_of_observations):
    positions.append(list(map(int, input().split())))  # tuple of (time, position at time)

positions.sort()  # sorts by time

# Go through each time interval and find the one with the highest speed
max_speed = 0
for i in range(number_of_observations - 1):
    delta_time = positions[i + 1][0] - positions[i][0]
    delta_distance = abs(positions[i + 1][1] - positions[i][1])

    speed = delta_distance / delta_time
    max_speed = max(speed, max_speed)

print(max_speed)

