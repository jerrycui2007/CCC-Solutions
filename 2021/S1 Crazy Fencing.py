# https://dmoj.ca/problem/ccc21s1
fences = int(input())
fence_lengths = list(map(int, input().split()))
fence_widths = list(map(int, input().split()))

total_area = 0

for fence in range(fences):
    # trapezoid area formula
    total_area += ((fence_lengths[fence] + fence_lengths[fence + 1]) / 2) * fence_widths[fence]

print(total_area)
