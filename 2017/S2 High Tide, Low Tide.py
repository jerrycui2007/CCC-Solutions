# https://dmoj.ca/problem/ccc17s2
number_of_measurements = int(input())
measurements = list(map(int, input().split()))

measurements.sort()

high_tide_measurements = []
low_tide_measurements = []

while len(measurements) > 0:
    low_tide_measurements.append(measurements.pop(0))
    try:
        high_tide_measurements.append(measurements.pop(-1))
    except IndexError:
        break

high_tide_measurements.reverse()
low_tide_measurements.reverse()

output_string = ""

for _ in range(len(high_tide_measurements)):
    output_string += str(low_tide_measurements.pop(0)) + " "
    output_string += str(high_tide_measurements.pop(0)) + " "

if len(low_tide_measurements) > 0:
    output_string += str(low_tide_measurements[0]) + " "

print(output_string[:-1])  # ignore last character which is empty space
