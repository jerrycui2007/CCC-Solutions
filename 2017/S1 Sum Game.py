# https://dmoj.ca/problem/ccc17s1
days = int(input())

swift_runs = list(map(int, input().split()))
semaphore_runs = list(map(int, input().split()))

swift_runs_total = 0
semaphore_runs_total = 0

# Check the running total of the runs on every day and update k when they are equal
k = 0
for i in range(days):
    swift_runs_total += swift_runs[i]
    semaphore_runs_total += semaphore_runs[i]

    if swift_runs_total == semaphore_runs_total:
        k = i + 1

print(k)