# https://dmoj.ca/problem/ccc00s5
# Still does not pass test case 6, due to some bs floating-point imprecision. Better than my previous brute force
# solution, though.

# Basically, for each sheep, calculate the range on the x-axis for which it is the nearest sheep, and mark safe
# the sheep that are safe


class Sheep:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.eaten = True  # assume all sheep are targets first

    def equals(self, other):  # Two sheep are the same if they have the same coordinate
        if (self.x == other.x) and (self.y == other.y):
            return True
        else:
            return False


number_of_sheep = int(input())
sheep = []
for _ in range(number_of_sheep):
    sheep.append(Sheep(float(input()), float(input())))  # x and y coordinates


for current_sheep in sheep:
    # range of x-values in which this sheep is closest to the fence
    left_range = 0
    right_range = 1000

    for other_sheep in sheep:
        if current_sheep.eaten and other_sheep.eaten and (not current_sheep.equals(other_sheep)):
            x_midpoint = (current_sheep.x + other_sheep.x) / 2
            y_midpoint = (current_sheep.y + other_sheep.y) / 2

            try:
                perpendicular_slope = (current_sheep.x - other_sheep.x) / (other_sheep.y - current_sheep.y)
            except ZeroDivisionError:
                continue

            if perpendicular_slope == 0:  # the two sheep have the same x-value
                if current_sheep.y < other_sheep.y:
                    other_sheep.eaten = False
                else:
                    current_sheep.eaten = False
            else:
                intersection_point = -y_midpoint / perpendicular_slope + x_midpoint  # intersection with x-axis

                if other_sheep.x < current_sheep.x:
                    left_range = max(left_range, intersection_point)
                else:
                    right_range = min(right_range, intersection_point)

    if left_range >= right_range:  # no possible range for this sheep to be eaten from
        current_sheep.eaten = False

for current_sheep in sheep:
    if current_sheep.eaten:
        # decimal formatting
        sheep_x = "{:.2f}".format(current_sheep.x)
        sheep_y = "{:.2f}".format(current_sheep.y)

        print("The sheep at ({0}, {1}) might be eaten.".format(sheep_x, sheep_y))