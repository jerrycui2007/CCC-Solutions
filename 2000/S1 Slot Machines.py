# https://dmoj.ca/problem/ccc00s1
# Simulate Marth playing through the machines

quarters = int(input())

machine_1 = int(input())
machine_2 = int(input())
machine_3 = int(input())

current_machine = 1
times_played = 0

while quarters > 0:
    quarters -= 1

    if current_machine == 1:
        machine_1 += 1
        if machine_1 == 35:
            quarters += 30
            machine_1 = 0
        current_machine = 2
        times_played += 1
        continue
    elif current_machine == 2:
        machine_2 += 1
        if machine_2 == 100:
            quarters += 60
            machine_2 = 0
        current_machine = 3
        times_played += 1
        continue
    elif current_machine == 3:
        machine_3 += 1
        if machine_3 == 10:
            quarters += 9
            machine_3 = 0
        current_machine = 1
        times_played += 1
        continue



print("Martha plays {0} times before going broke.".format(times_played))
