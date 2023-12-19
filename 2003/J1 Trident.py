# https://dmoj.ca/problem/ccc03j1
tine_height = int(input())
tine_spacing = int(input())
handle_height = int(input())

tine_string = "*" + " " * tine_spacing + "*" + " " * tine_spacing + "*"
for _ in range(tine_height):
    print(tine_string)

print("*" * len(tine_string))

handle_string = " " * (tine_spacing + 1) + "*"
for _ in range(handle_height):
    print(handle_string)
