# https://dmoj.ca/problem/ccc02s5
width = int(input())
height = int(input())

ball_x = int(input())
ball_y = int(input())


finished = False

slope = ball_y / (width - ball_x)

k = 1
while True:
    y = slope * ((k * width) - ball_x)
    x = (k * height) / slope + ball_x

    heights = int(((y - (height / 2)) / height) + 1)
    widths = int(((x - (width / 2)) / width) + 1)

    horizontal_edge = heights * height
    vertical_edge = widths * width

    if (abs(horizontal_edge - y) < 5) or (abs(vertical_edge - x) < 5):  # pocket
        if abs(horizontal_edge - y) < 5:
            if horizontal_edge != y:
                bounces = k - 1 + int(y / height)
            else:  # ball bounces directly into pocket
                bounces = k - 2 + int(y / height)
        else:
            if vertical_edge != x:
                bounces = k - 1 + int(x / width)
            else:
                bounces = k - 2 + int(x / width)

        print(bounces)
        finished = True
        break

    k += 1
    if k == 1000000: # Assume that the ball will just never hit a corner.
        break

if not finished:
    print(0)
