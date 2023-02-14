# https://dmoj.ca/problem/ccc00j1
# Presentation Error on DMOJ, don't know why

data = input().split(" ")

days = ["Sun", "Mon", "Tue", "Wed", "Thr", "Fri", "Sat"]

starting_day = data[0]
days_in_month = data[1]

offset = int(starting_day) - 1

print("Sun Mon Tue Wed Thr Fri Sat")

row_1 = [1 - offset, 2 - offset, 3 - offset, 4 - offset, 5 - offset, 6 - offset, 7 - offset]
row_2 = [8 - offset, 9 - offset, 10 - offset, 11 - offset, 12 - offset, 13 - offset, 14 - offset]
row_3 = [15 - offset, 16 - offset, 17 - offset, 18 - offset, 19 - offset, 20 - offset, 21 - offset]
row_4 = [22 - offset, 23 - offset, 24 - offset, 25 - offset, 26 - offset, 27 - offset, 28 - offset]
row_5 = [29 - offset, 30 - offset, 31 - offset, 32 - offset, 33 - offset, 34 - offset, 35 - offset]


row_1_str = ""
for date in row_1:
    if date >= 1:
        if len(str(date)) == 1:
            row_1_str += "  " + str(date)
        else:
            row_1_str += " " + str(date)
    elif date > int(days_in_month):
        pass
    else:
        row_1_str += "   "
    row_1_str += " "

row_2_str = ""
for date in row_2:
    if date >= 1:
        if len(str(date)) == 1:
            row_2_str += "  " + str(date)
        else:
            row_2_str += " " + str(date)
    elif date > int(days_in_month):
        pass
    else:
        row_2_str += "   "
    row_2_str += " "

row_3_str = ""
for date in row_3:
    if date >= 1:
        if len(str(date)) == 1:
            row_3_str += "  " + str(date)
        else:
            row_3_str += " " + str(date)
    elif date > int(days_in_month):
        pass
    else:
        row_3_str += "   "
    row_3_str += " "

row_4_str = ""
for date in row_4:
    if date >= 1:
        if len(str(date)) == 1:
            row_4_str += "  " + str(date)
        else:
            row_4_str += " " + str(date)
        row_4_str += " "
    elif date > int(days_in_month):
        row_4_str += " "
    else:
        row_4_str += "   "


row_5_str = ""
for date in row_5:
    if 1 <= date <= int(days_in_month):
        if len(str(date)) == 1:
            row_5_str += "  " + str(date)
        else:
            row_5_str += " " + str(date)
        row_5_str += " "
    elif date > int(days_in_month):
        row_5_str += " "
    else:
        row_5_str += "   "


print(row_1_str.rstrip())
print(row_2_str.rstrip())
print(row_3_str.rstrip())
print(row_4_str.rstrip())
print(row_5_str.rstrip(), end="")
