# https://dmoj.ca/problem/ccc00j1
start_day, days_in_month = list(map(int, input().split()))

# Header which is always the same
print("Sun Mon Tue Wed Thr Fri Sat")

for i in range(start_day - 1):
    print("    ", end="")  # empty spots before dates

for day in range(1, days_in_month + 1):
    print("%3d" % day, end="")

    if ((day + start_day - 1) % 7 == 0) or day == days_in_month:  # end of week/month
        print()  # newline
    else:
        print(" ", end="")